"""Topic Context Model."""

import json
import logging
from algorithm import *
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

__version__ = "0.1.0"

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="tcm", formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s v{__version__}"
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Verbose output."
    )

    parser.add_argument("-i", "--input", help="Input file")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-t", "--topics", help="Number of topics")

    args = parser.parse_args()
    log_format = "%(asctime)s %(levelname)s %(message)s"

    if args.verbose == 0:
        logging.basicConfig(format=log_format, level=logging.WARN)
    elif args.verbose == 1:
        logging.basicConfig(format=log_format, level=logging.INFO)
    elif args.verbose >= 2:
        logging.basicConfig(format=log_format, level=logging.DEBUG)

    try:
        with open(args.input, "r") as f:
            data = f.read()
    except Exception as e:
        logging.error(e)
        exit(0)

    try:
        data = json.loads(data)
    except ValueError:
        data = data.split("\n")
        data = {idx: doc.split() for idx, doc in enumerate(data)}

    if args.topics is not None:
        try:
            num_of_topics = int(args.topics)
        except ValueError:
            logging.error("Number-of-topics (-t, --topic) is not valid, it should be an integer number greater than 0. "
                          "please use -t or --topics to provide a valid number of topics")
            exit(0)
    else:
        logging.error("Number of topics is not provided, please use -t or --topics to provide number of topics")
        exit(0)
        
    output_path = args.output
    TCM(data, num_of_topics, output_path)
