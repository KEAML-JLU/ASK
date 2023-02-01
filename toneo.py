#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import time


spo = pd.read_csv('./about/data1.tsv',sep='\t')

di = spo[":START_ID"].unique().tolist()
ge = spo[":END_ID"].unique().tolist()

date = time.strftime('%Y%m%d',time.localtime(time.time()))

diids = ['PMDDI'+date+'-'+str(a) for a in range(len(di))]
geids = ['PMDGE'+date+'-'+str(a) for a in range(len(ge))]

dinodes = pd.DataFrame({":ID":diids,":TYPE":'disease','name':di})
genodes = pd.DataFrame({":ID":geids,":TYPE":'gene','name':ge})

spo[':START_ID'] = spo[':START_ID'].map(lambda x :dinodes[dinodes['name']==x][':ID'].iloc[0] )
spo[':END_ID'] = spo[':END_ID'].map(lambda x :genodes[genodes['name']==x][':ID'].iloc[0] )

spo.to_csv('./about/edges.csv',index=None)
nodes = pd.concat([dinodes,genodes],ignore_index=True)
nodes.to_csv('./about/nodes.csv',index=None)







