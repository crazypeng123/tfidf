# encoding=utf-8
import jieba
import input_mysql as im

jieba.load_userdict("userdict.txt")


def __FenCi1__(content=im.content):
    fenci1 = []
    for i in range(200):
        fenci1.append(jieba.cut(content[i]))
    return fenci1


fenci1 = __FenCi1__()
# print(" ".join(fenci[2]))
sep = list()
for i in fenci1:
    sep.append(" ".join(i))
# print(sep[1])
