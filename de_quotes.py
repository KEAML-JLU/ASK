import os

ss = "./about/test0.tsv"  # 源文件地址
s2 = "./about/test.tsv"  # 复制的文件地址


def modify():
    with open(ss, "r", encoding='UTF-8-sig')as fr, open(s2, "w", encoding='UTF-8-sig')as fw:
        file_data = fr.readlines()
        for row in file_data:  # 读取每一行
            tmp = str(row).strip("\n\r").split(',')  # 以","为分界符，分成数组
            print(tmp)
            b = eval(tmp[9])  # eval为python自带函数，可以去掉数组值两边引号，具体可查
            l = row.replace(tmp[9], b)
            fw.write(l)
    os.remove(ss)
    os.rename(s2, ss)


if __name__ == '__main__':
    modify()