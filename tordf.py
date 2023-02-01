#!/usr/bin/env python
# coding: utf-8

# In[53]:

import os
import time

import pandas as pd
from pandas import DataFrame
import argparse
parser = argparse.ArgumentParser(description='文件位置')
parser.add_argument('--re_file', type=str,  default="re_outputs_1", help='输入re结果位置')
parser.add_argument('--re_file2', type=str,  default="re_outputs_ch_di", help='输入re结果位置')
parser.add_argument('--re_file3', type=str,  default="re_outputs_ch_ge", help='输入re结果位置')
args = parser.parse_args()
# parser = argparse.ArgumentParser(description='文件位置')
# parser.add_argument('--result_file', type=str,  default="fileout/test_results.tsv", help='输入预测结果')
# parser.add_argument('--entity_file', type=str,  default="fileout/paperword.tsv", help='输入实体文件')
# parser.add_argument('--fileout_dir', type=str,default='fileout/data1.tsv',help='输出文件位置')
# args = parser.parse_args()


# In[75]:


results = pd.read_csv(args.re_file+"/test_results.tsv",sep='\t',header = None)
results2 = pd.read_csv(args.re_file2+"/test_results.tsv",sep='\t',header = None)
files = pd.read_csv('about/di_ge/test.tsv',sep='\t')
# results = pd.read_csv(args.entity_file,sep='\t',header = None)
# results = pd.read_csv(args.files_file,sep='\t',header = None)


# In[79]:


entities_all1=[]
entities_all2=[]
entities_all4=[]
entities_all6=[]
for i,call in enumerate(results[1]):
    if call > 0.1:#应为0.6
        entities = [files.iloc[i,2],files.iloc[i,3]]
        entities_all1.append(entities)
    if call > 0.2:#应为0.6
        entities = [files.iloc[i,2],files.iloc[i,3]]
        entities_all2.append(entities)
    if call > 0.4:#应为0.6
        entities = [files.iloc[i,2],files.iloc[i,3]]
        entities_all4.append(entities)
    if call > 0.6:#应为0.6
        entities = [files.iloc[i,2],files.iloc[i,3]]
        entities_all6.append(entities)
print(len(entities_all6))

# for i,call in enumerate(results2[1]):
#     if call > 0.4:#应为0.6
#         entities = [files.iloc[i][2],files.iloc[i][3]]
#         entities_all2.append(entities)


# In[81]:


a2b = DataFrame(entities_all6)
a2b.insert(1,":TYPE",'gene_disease')
a2b.columns=[":START_ID",":TYPE",":END_ID"]

# a2b2 = DataFrame(entities_all2)
# a2b2.insert(1,":TYPE",'chemical_disease')
# a2b2.columns=[":START_ID",":TYPE",":END_ID"]



date=time.strftime('%Y%m%d',time.localtime(time.time()))
path ='./about/'+date
if not os.path.exists(path):
    os.makedirs(path)
    print('文件夹创建完成  '+path)

# a2b.to_csv(args.fileout_dir, index=False,header=None,sep='\t')
a2b.to_csv('about/'+date+'/data1.tsv', index=False,sep='\t')
a2b.to_csv('about/data1.tsv', index=False,sep='\t')

# a2b2.to_csv('about/'+date+'/data2.tsv', index=False,sep='\t')
# a2b2.to_csv('about/data2.tsv', index=False,sep='\t')








