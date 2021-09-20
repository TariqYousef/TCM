# TCM
Calculating shannon's information content (IC) Based on topic models using LDA (Latent Dirichlet Allocation) algorithm.

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
- Adding support for LSA (Latent Semantic Analysis) algorithm.

### Related Publications:
- [Keyword extraction in German: Information-theory vs. deep learning (2020)](https://www.scitepress.org/Papers/2020/93747/93747.pdf)
- [The Semantic Level of Shannon Information: Are Highly Informative Words Good Keywords? A Study on German (2020)](https://books.google.de/books?hl=en&lr=&id=Oe4lEAAAQBAJ&oi=fnd&pg=PA139&dq=info:b-PqG87toREJ:scholar.google.com&ots=pK3aij8JVY&sig=eKUeHMdAQSs511q_chTlmSn8arE&redir_esc=y#v=onepage&q&f=false)
- [Information from topic contexts: the prediction of aspectual coding of verbs in Russian (2020)](https://www.researchgate.net/publication/345636663_Information_from_topic_contexts_the_prediction_of_aspectual_coding_of_verbs_in_Russian)
