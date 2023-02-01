
ASK Automated knowledge graph construction,updating and self_reflection
====  
1.Initiation
--
Donwload pre-trained weights of bioBERT and datasets from https://github.com/dmis-lab/biobert.<br> 
Then training the NER and RE models.

2.auto construction and updating
--
Run `python dataclock.py` for auto construction.<br> 
Run `python fusion/get_KG`,`python fusion/alignment_match.py` for knowledge updating.

3.self-reflection
--
Run `python prediction/tranE.py` for link-prediction
Run `python conflict/node2vec.py`,`python conflict/conflict.py`
