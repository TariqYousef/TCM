"""This file contains the necessary functions to calculate IC values"""
import math
from collections import defaultdict, Counter
from gensim import corpora
from gensim.models import ldamodel
import logging
import csv


def TCM(documents, num_of_topics, output_path):
    """This function calculate the IC values for each token based on Shannon' Information
    content formula and topic models as context"""
    # 1. preprocessing
    # - create _wdm and _lda_docs arrays
    _wdm, _lda_docs = preprocessing(documents)
    logging.debug("== 1. Preprocessing finished!")

    # 2. LDA
    trained_model = LDA(lda_docs=_lda_docs, num_of_topics=num_of_topics)

    # 3. calculate Information Content (IC) values
    ic_values = get_IC(trained_model, _lda_docs, _wdm)

    # 4. normalize and sort IC values
    max_ic_val = max(ic_values.items(), key=lambda x: x[1])[1]
    normalized_ic_values = {key: round(val / max_ic_val, 5)
                            for key, val in ic_values.items()}
    save_csv(sorted(normalized_ic_values.items(), key=lambda x: x[1], reverse=True), output_path)


def save_csv(data, output_path):
    """Save IC values to the output file in csv format"""
    try:
        with open(output_path, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["Token", "IC"])
            writer.writeheader()
            for row in data:
                writer.writerow({"Token": row[0], "IC": row[1]})
            logging.debug(f"== 5. Saving to {output_path} is done!")
    except (IOError, TypeError):
        logging.error("I/O error: IC values couldn't be saved to output file ")
        print(data)
        exit(0)


def preprocessing(documents):
    _wdm = defaultdict(lambda: [])
    _lda_docs = {}
    for idx, document in documents.items():
        _lda_docs[idx] = document
        for token in document:
            _wdm[token].append(idx)
    return _wdm, _lda_docs


def LDA(lda_docs, num_of_topics=None, passes=15):
    dictionary = corpora.Dictionary(lda_docs.values())
    # convert to bag-of-words corpus
    corpus = [dictionary.doc2bow(text) for text in lda_docs.values()]
    # save the dictionary and corpus for future use
    logging.debug("== 2. Training LDA model started!")
    ldaModels = {}
    # run LDA
    ldaModel = ldamodel.LdaModel(corpus, num_topics=num_of_topics, id2word=dictionary, passes=passes)
    logging.debug("== 2. Finished training the topic model!")
    return ldaModel


def get_IC(trainedModel, documents, wdm, output="/"):
    documents_topic = dict()
    # 1. get the main topics for each document
    for doc_id, tokens in documents.items():
        bow = trainedModel.id2word.doc2bow(tokens)
        doc_topics, word_topics, phi_values = trainedModel.get_document_topics(bow, per_word_topics=True)
        documents_topic[doc_id] = doc_topics

    logging.debug("== 3. Documents topics are saved!")
    # 2. get distinct documents ids for each word
    wdm = {key: Counter(doc).most_common() for key, doc in wdm.items() if len(doc) > 0}
    wordIC = dict()
    for token in wdm:
        temp = [(topic, probability) for doc, freq in wdm[token]
                for i in range(freq)
                for topic, probability in documents_topic[doc]
                ]
        wt_ = defaultdict(lambda: 0)
        for topic, pr in temp:
            wt_[topic] += pr
        if len(wt_) > 0:
            wordIC[token] = ICFormula([(a, b) for a, b in wt_.items()])
        else:
            wordIC[token] = -1
    logging.debug("== 4. Calculating IC values is done!")
    return wordIC


# Information Content Formula
def ICFormula(vec):
    vec = [val for (k, val) in vec]
    s = sum(vec)
    if s == 0 or len(vec) == 0:
        return -1
    else:
        return sum([-math.log2(val / s) for val in vec]) / len(vec)
