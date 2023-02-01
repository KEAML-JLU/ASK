#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='文件位置及数据作用行数')
parser.add_argument('--data_dir', type=str,help='文件位置')
parser.add_argument('--num', type=int, default=3,help='需要行数')
parser.add_argument('--fileout_dir', type=str,default='fileout/nes.tsv',help='输出文件位置')
args = parser.parse_args()

num = args.num
strs = []
a = pd.read_table(args.data_dir+"/NER_result_conll.txt",header=None,sep='\s',engine='python')
flag = 0#是否是实体
b_flag = 0#是否含'-()'
rel = ''
for row in a.itertuples():
    if flag == 1:
        if row[num] == "I-MISC":
            rel1 = str(row[1])
            string = "~!@#$%^&*()_+-*/<>,.[]\/"
            if b_flag == 1:
                rel = rel+rel1
                b_flag = 0
            elif rel1 in string:
                b_flag = 1
                rel = rel+rel1
            # elif row[1] == '(':
            #     b_flag = 1
            #     rel = rel+rel1
            # elif row[1] == ')':
                b_flag = 1
                rel = rel+rel1
            else:
                rel = rel + ' ' + rel1#拼接字符串
        else:
                strs.append(rel)
                flag = 0
    
    if row[num] == "B-MISC":#标志为B
        if row[1] == '-':
            print('B-')
        flag = 1
        rel = str(row[1])


strs = list(set(strs))#去重

nes = pd.DataFrame(strs)
nes[0] = nes[0].str.replace('--','-')#修改--
nes.to_csv(args.fileout_dir, index=False,header=None,sep='\t')
print('done')

