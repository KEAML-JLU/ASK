import pandas as pd
from itertools import combinations
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description='文件位置及数据作用行数')
parser.add_argument('--nes1', type=str,help='实体文件位置1')
parser.add_argument('--nes1name', type=str,help='实体文件种类1')
parser.add_argument('--paper', type=str,help='文件位置')
parser.add_argument('--fileout_dir', type=str,default='fileout',help='输出文件位置')
args = parser.parse_args()

nes1 = pd.read_table(args.nes1,header=None)
papers = pd.read_table(args.paper,header=None)


nes1 = nes1[0].values.tolist()
papers = papers[0].values.tolist()
name1 = '@' + args.nes1name + '$'
out = []
i = 0
for paper in tqdm(papers):
    words = []
    paper.replace('"','')
    for i,ne in enumerate(nes1):
        ne = str(ne)
        if ne in paper and len(ne)>2:
            for j in range(i+1,len(nes1)):
                ne2 = str(nes1[j])
                if ne2 in paper and len(ne2)>2:
                    paper = paper.replace(ne,name1,1).replace(ne2,name1,1)
                    out.append([i,paper,ne,ne2])
                    i += 1
    # word_len = len(words)
    # print('len:'+str(word_len))
    # if word_len>=2:
    #     for c in combinations(words,2):
    #         sen1 = paper+'\t'+c[0]+'\t'+c[1]
    #         out.append([paper,c[0],c[1]])


outs = pd.DataFrame(out)
outs.to_csv(args.fileout_dir+'/test.tsv',index=None,header=['index','sentence','label','label2'],sep='\t')
