# TCM
Calculating shannon's information content (IC) Based on topic models using LDA algorithm.

The tool is language-independent, and it can deal with texts in any language.

Users should preprocess their texts and prepare them. That gives more freedom to the users to apply different preprocessing steps.

The tool accepts two file formats as input:
- JSON: the json objects contains a set of documents/sentences and their ids. Each document/sentence is an array of tokens.
```json
{
  "1": ["beginning", "god", "created", "heavens", "earth"],
  "2": ["earth", "formless", "empty", "darkness", "surface", "deep", "spirit", "god", "hovering", "waters"], 
  "3": ["god", "said", "let", "light", "light"], 
  "4": ["god", "saw", "light", "good", "separated", "light", "darkness"], 
  "5": ["god", "called", "light", "day", "darkness", "called", "evening", "first", "day"], 
  "6": ["god", "said", "let", "vault", "waters", "separate", "water", "water"]
}
```

- TXT:
Each line contains a sentence/document, tokens are separated with white space.
```
beginning god created heavens earth
earth formless empty darkness surface deep spirit god hovering waters
god said let light light
god saw light good separated light darkness
god called light day darkness called evening first day
god said let vault waters separate water water
```


### Recommended Preprocessing Steps:
- Lowercasing
- Stop words removal
- Punctuation marks, non-alphabetic characters removal
- High-frequency words removal (common words not in the stopwords list that do not add any meaning overall) 
- Lemmatization and Stemming

### How to use
- Install requirments.txt
```commandline
$ pip install -r requirements.txt
```
- Run tcm.py
```commandline
$ python tcm.py -i examples/input/sample1.json -t 10 -o examples/output/test1.csv 
```

### Parameters:
- ```-i, --input```: path to the input file.
- ```-o, --output```: path to the out file where the IC values should be saved.
- ```-t, --topics```: number of topics.
- ```-v, --verbose```: verbose output.


### Note:
- Since LDA training is not deterministic, the results over multiple training could slightly differ.

### Future work:
- Adding support for LSI algorithm.