import re

file_path = r'about/papers.txt'
with open(file_path, "r", encoding='utf-8') as f:  # 打开文件
    text = f.read()  # 读取文件

text.strip('\n')
result_list = re.split('\.\s', text)



with open("about/thepaper1.txt", 'w') as f:
    for i in result_list:
        i = i.lstrip("\n")
        i=i.replace('"','')
        print(i)
        f.write(i + '\n')

