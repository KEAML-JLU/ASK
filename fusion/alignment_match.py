import pandas as pd
from tqdm import tqdm
kg1_path = 'database/cd/'
kg2_path = 'database/KG/'

label_path = 'predefined/'

def compare_label(l1,l2):
    if l1 == l2:
        return True
    else:
        pairs = pd.read_csv(label_path+'label.csv').values
        for pair in pairs:
            if l1 in pair and l2 in pair:
                return True
        return False

def similarity(e1,e2):
    if len(e1)!=3:
        print(e1)
    assert len(e1) == 3
    assert len(e2) == 3
    if str(e1[1]).lower() == str(e2[1]).lower() and compare_label(e1[2].lower(),e2[2].lower()):
    # if str(e1[1]).lower() == str(e2[1]).lower() :
        return 1
    else:
        return 0

def entity_alignment():
    with open('result/吉大图谱对齐/test.csv', 'a',encoding='utf-8') as file:
        # kg1_entity = pd.read_csv(kg1_path+'银Jnodes - 副本.csv').values
        kg1_entity = pd.read_csv(kg1_path + 'nodes.csv').values
        kg2_entity = pd.read_csv(kg2_path+'nodes.csv').values
        # print(kg1_entity)
        # print(kg2_entity)
        for e1 in tqdm(kg1_entity):
            # print(e1[0])
            for e2 in kg2_entity:
                if similarity(e1,e2) == 1:
                    # print('yes')
                    # file.writelines(str(e1[0])+'\t'+str(e2[0])+'\n')
                    file.writelines('"'+str(e1[0])+'","'+str(e2[0])+'","1"\n')
# def entity_alignment_GNBR_DB_HE_LABEL():
#     with open('result/吉大图谱对齐/new_LABELGNBR_DB_HE.csv', 'a',encoding='utf-8') as file:
#         # kg1_entity = pd.read_csv(kg1_path+'银Jnodes - 副本.csv').values
#         kg1_entity = pd.read_csv(kg1_path + 'nodes.csv').values
#         kg2_entity = pd.read_csv(kg2_path+'nodes.csv').values
#         # print(kg1_entity)
#         # print(kg2_entity)
#         for e1 in tqdm(kg1_entity):
#             # print(e1[0])
#             for e2 in kg2_entity:
#                 if similarity(e1,e2) == 1:
#                     # file.writelines(str(e1[0])+'\t'+str(e2[0])+'\n')
#                     file.writelines('"'+str(e1[0])+'","'+str(e2[0])+'","'+str(e1[2])+'","'+str(e2[2])+'"\n')
# def entity_alignment_ent_links():
#     with open('result/吉大图谱对齐/kg1_kg2_ent_link', 'a',encoding='utf-8') as file:
#         # kg1_entity = pd.read_csv(kg1_path+'银Jnodes - 副本.csv').values
#         kg1_entity = pd.read_csv(kg1_path + 'nodes.csv').values
#         kg2_entity = pd.read_csv(kg2_path+'nodes.csv').values
#         # print(kg1_entity)
#         # print(kg2_entity)
#         for e1 in tqdm(kg1_entity):
#             # print(e1[0])
#             for e2 in kg2_entity:
#                 if similarity(e1,e2) == 1:
#                     file.writelines(str(e1[0])+'\t'+str(e2[0])+'\n')
#                     # file.writelines('"'+str(e1[0])+'","'+str(e2[0])+'","1"\n')
if __name__ == "__main__":
    entity_alignment()
    # entity_alignment_GNBR_DB_HE_LABEL()
    # entity_alignment_ent_links()