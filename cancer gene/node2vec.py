from gensim.models import fasttext
from gensim.models import word2vec
import pandas as pd
import logging
import jieba
import numpy as np
import math
from tqdm import tqdm
edges=pd.read_csv("newcd.csv",header=None)
edges0 = pd.read_csv('gddata1.tsv',sep='\t')

ea = np.array(edges)
ea0 = np.array(edges0)
ea = ea.tolist()
ea0 = ea0.tolist()

ea1 = ea + ea0

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = word2vec.Word2Vec(ea1,min_count=1,epochs=20)
model.save("word2vec.model")

start = []
mid = []
end = []
for row in tqdm(ea1):
    if (row[0] is np.nan) or (row[1] is np.nan) or (row[2] is np.nan):
        continue
    start.append(int(np.mean(model.wv[row[0]])*math.pow(10,6)))
    mid.append(int(np.mean(model.wv[row[1]])*math.pow(10,6)))
    end.append(int(np.mean(model.wv[row[2]])*math.pow(10,6)))
vecs =pd.DataFrame({"start":start,"mid":mid,"end":end})
vecs.to_csv("vecs.csv",index=None)
entities = pd.DataFrame(ea1)
entities.to_csv("entities.csv",index=None)