import pandas as pd
import csv
alignment_file_path = 'result/吉大图谱对齐/test.csv'
kg1_path = 'database/cd/'
kg2_path = 'database/KG/'

def get_kg_entity():
    alignment = pd.read_csv(alignment_file_path,header=0,names=['0','1','2'],engine='python',quoting=csv.QUOTE_NONE)
    kg1_entity = pd.read_csv(kg1_path+'nodes.csv')
    kg2_entity = pd.read_csv(kg2_path+'nodes.csv')
    kg2_delete_ids = alignment['1'].values
    for id in kg2_delete_ids:
        kg2_entity = kg2_entity.drop(kg2_entity[kg2_entity[':ID'] == id].index)
    kg1_entity.to_csv('KG/new/nodes.csv',mode='a',index=False)
    kg2_entity.to_csv('KG/new/nodes.csv',mode='a',header=False,index=False)

def get_kg_relation():
    alignment = pd.read_csv(alignment_file_path, header=0, names=['0','1','2'],engine='python',quoting=csv.QUOTE_NONE)
    kg1_relation = pd.read_csv(kg1_path+'edges.csv')
    kg2_relation = pd.read_csv(kg2_path+'edges.csv')
    for i in alignment.values:
        kg2_relation.replace(i[1],i[0],inplace=True)
    kg_relaiton = kg1_relation.append(kg2_relation)
    kg_relaiton.drop_duplicates(subset=[':START_ID',':END_ID'],keep='first',inplace=True)
    kg_relaiton.to_csv('KG/new/edges.csv',mode='a',index=False)

if __name__ == "__main__":
    get_kg_entity()
    get_kg_relation()