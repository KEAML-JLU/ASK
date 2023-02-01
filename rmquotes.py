import pandas as pd
file = pd.read_csv('./about/test1.tsv',sep='\t',header=None,quoting=3, quotechar = '"')

file[0][0] = file[0][0].replace('"','')
file.drop(file.tail(1).index,inplace=True) # drop last n rows

file.to_csv('./about/test1.tsv',sep='\t',header=None)