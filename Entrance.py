from Bio import Entrez,Medline
Entrez.email = "919474823@qq.com"
import os



handle = Entrez.esearch(db = 'pubmed', term = "Cardiovascular diseases",reldate = 3650,usehistory="y",retmax=100000)
record_cd = Entrez.read(handle)

for i in record_cd['IdList']:
    handle = Entrez.efetch(db="pubmed", id=i,
                           retmode="text", rettype="medline")
    record = Medline.read(handle)

    title = record["TI"]
    title = title.replace('[', '').replace('].', '')#去除标题中[]
    try:
        ab = record["AB"]
    except KeyError:
        continue
    #print(title)

    with open('about/papers.txt', 'a') as f:
        f.write(title + '\n')
        f.write(ab + '\n')

count = int(record_cd["Count"])
print(count)