from gensim.models import fasttext
from gensim.models import word2vec
import pandas as pd
import logging
import jieba
from tqdm import tqdm
import numpy as np
from pysat.formula import CNF
from pysat.solvers import Solver


vecs = pd.read_csv("vecs.csv")
entities =pd.read_csv("entities.csv")

vecs_old = vecs[0:243675]
vecs_new = vecs[243679:]
vecs_new1 = vecs_new.copy()

vecs_o1=np.array(vecs_old[['start','mid']]).tolist()
vecs_o2=np.array(vecs_old[['mid','end']]).tolist()
vecs_n1 =np.array(vecs_new[['start','mid']]).tolist()
vecs_n2 =np.array(vecs_new[['mid','end']]).tolist()
vecs_l1 =vecs_o1+vecs_o2+vecs_n1+vecs_n2

vecs_np = np.array(vecs_l1)
vecs_np[vecs_np==0] = 1
cnt_array = np.where(vecs_np,0,1)
print(np.sum(cnt_array))

vecs_l1 =vecs_np.tolist()


cnf = CNF(from_clauses=vecs_l1)

# create a SAT solver for this formula:
with Solver(bootstrap_with=cnf) as solver:
    # 1.1 call the solver for this formula:
    print('formula is', f'{"s" if solver.solve() else "uns"}atisfiable')

    # 1.2 the formula is satisfiable and so has a model:
    #print('and the model is:', solver.get_model())

    # 2.1 apply the MiniSat-like assumption interface:
    print('formula is',
        f'{"s" if solver.solve(assumptions=[1, 2]) else "uns"}atisfiable',
        'assuming x1 and x2')

    # 2.2 the formula is unsatisfiable,
    # i.e. an unsatisfiable core can be extracted:
    print('and the unsatisfiable core is:', solver.get_core())