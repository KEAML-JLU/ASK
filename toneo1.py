#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import time


spo = pd.read_csv('./fileout/tri/cddata1.tsv',sep='\t').dropna()
spo1 = pd.read_csv('./fileout/tri/cgdata1.tsv',sep='\t').dropna()
spo2 = pd.read_csv('./fileout/tri/gddata1.tsv',sep='\t').dropna()
spo3 = pd.read_csv('./fileout/tri/ggdata1.tsv',sep='\t').dropna()

di1 = spo[":END_ID"]
di3 = spo2[":END_ID"]
di1.columns=["DI"]
di3.columns=["DI"]
di = di1
di = di.append(di3, ignore_index = True).unique().tolist()

ch1 = spo[":START_ID"]
ch2 = spo1[":START_ID"]
ch1.columns=["CH"]
ch2.columns=["CH"]
ch = ch1
ch = ch.append(ch2, ignore_index = True).unique().tolist()

ge1 = spo1[":END_ID"]
ge2 = spo2[":START_ID"]
ge3 = spo3[":START_ID"]
ge4 = spo3[":END_ID"]
ge1.columns=["GE"]
ge2.columns=["GE"]
ge3.columns=["GE"]
ge4.columns=["GE"]
ge = ge1
ge = ge.append(ge2, ignore_index = True).append(ge3, ignore_index = True)\
    .append(ge4, ignore_index = True).unique().tolist()

# di = spo[":START_ID"].unique().tolist()
# ge = spo[":END_ID"].unique().tolist()

date = time.strftime('%Y%m%d',time.localtime(time.time()))

diids = ['PMDDI'+date+'-'+str(a) for a in range(len(di))]
geids = ['PMDGE'+date+'-'+str(a) for a in range(len(ge))]
chids = ['PMDCH'+date+'-'+str(a) for a in range(len(ch))]

dinodes = pd.DataFrame({":ID":diids,'name':di,":LABEL":'Disease'})
genodes = pd.DataFrame({":ID":geids,'name':ge,":LABEL":'Gene'})
chnodes = pd.DataFrame({":ID":chids,'name':ch,":LABEL":'Chemical'})

spo[':START_ID'] = spo[':START_ID'].map(lambda x :chnodes[chnodes['name']==x][':ID'].iloc[0] )
spo[':END_ID'] = spo[':END_ID'].map(lambda x :dinodes[dinodes['name']==x][':ID'].iloc[0] )

spo1[':START_ID'] = spo1[':START_ID'].map(lambda x :chnodes[chnodes['name']==x][':ID'].iloc[0] )
spo1[':END_ID'] = spo1[':END_ID'].map(lambda x :genodes[genodes['name']==x][':ID'].iloc[0] )
#gd
spo2[':START_ID'] = spo2[':START_ID'].map(lambda x :genodes[genodes['name']==x][':ID'].iloc[0] )
spo2[':END_ID'] = spo2[':END_ID'].map(lambda x :dinodes[dinodes['name']==x][':ID'].iloc[0] )

spo3[':START_ID'] = spo3[':START_ID'].map(lambda x :genodes[genodes['name']==x][':ID'].iloc[0] )
spo3[':END_ID'] = spo3[':END_ID'].map(lambda x :genodes[genodes['name']==x][':ID'].iloc[0] )

spo = pd.concat([spo,spo1],ignore_index=True)
spo = pd.concat([spo,spo2],ignore_index=True)
spo = pd.concat([spo,spo3],ignore_index=True)

spo.to_csv('./about/edges.csv',index=None)

nodes = pd.concat([dinodes,genodes],ignore_index=True)
nodes = pd.concat([nodes,chnodes],ignore_index=True)

nodes.to_csv('./about/nodes.csv',index=None)







