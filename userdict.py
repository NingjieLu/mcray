#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-16 11:07:53
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

#构造词典
import os
import jieba
#停用词
stopkey=[line.strip() for line in open('E://mc//StopWordTable2.txt','r', encoding='UTF-8').readlines()]
jieba.load_userdict("userdict.txt")
#指南数据
limit = 164
filecount = 0

file = open("E://mc//book//jiebabook.txt", 'a', encoding='utf-8')
while filecount<limit:
    print(filecount)
    f = open("E://mc//book//z"+str(filecount)+".txt", 'r', encoding='utf-8')
    text = f.read()
    f.close()
    words = list(jieba.cut(text))
    for word1 in words:
        if word1 not in stopkey:
            file.write(word1+" ")
    filecount += 1
file.close()
print("book done 164")
#住院诊疗数据
limit = 99053
filecount = 0

file = open("E://mc//emri//jiebaemri.txt", 'a', encoding='utf-8')
while filecount<limit:
    print(filecount)
    f = open("E://mc//emri//"+str(filecount)+"5.txt", 'r', encoding='utf-8')
    text = f.read()
    f.close()
    words = list(jieba.cut(text))
    for word1 in words:
        if word1 not in stopkey:
            file.write(word1+" ")
    filecount += 1
file.close()
print("emri done 99053")
#门诊诊疗数据
limit = 6092
filecount = 0

file = open("E://mc//emr//jiebaemro.txt", 'a', encoding='utf-8')
while filecount<limit:
    print(filecount)
    f = open("E://mc//emr//r"+str(filecount)+"5.txt", 'r', encoding='utf-8')
    text = f.read()
    f.close()
    words = list(jieba.cut(text))
    for word1 in words:
        if word1 not in stopkey:
            file.write(word1+" ")
    filecount += 1
file.close()
print("emro done 6092")
#门诊诊疗数据
limit = 6092
filecount = 0

file = open("E://mc//emr//jiebaemro.txt", 'a', encoding='utf-8')
while filecount<limit:
    print(filecount)
    f = open("E://mc//emr//r"+str(filecount)+"5.txt", 'r', encoding='utf-8')
    text = f.read()
    f.close()
    words = list(jieba.cut(text))
    for word1 in words:
        if word1 not in stopkey:
            file.write(word1+" ")
    filecount += 1
file.close()
print("emro done 6092")

#住院xray数据
limit = 682
filecount = 0

file = open("E://mc//xray//jiebaxrayi.txt", 'a', encoding='utf-8')
while filecount<limit:
    print(filecount)
    f = open("E://mc//xray//i"+str(filecount)+".txt", 'r', encoding='utf-8')
    text = f.read()
    f.close()
    words = list(jieba.cut(text))
    for word1 in words:
        if word1 not in stopkey:
            file.write(word1+" ")
    filecount += 1
file.close()
print("xrayi done 682")

#门诊xray数据
limit = 1172
filecount = 0

file = open("E://mc//xray//jiebaxrayo.txt", 'a', encoding='utf-8')
while filecount<limit:
    print(filecount)
    f = open("E://mc//xray//o"+str(filecount)+".txt", 'r', encoding='utf-8')
    text = f.read()
    f.close()
    words = list(jieba.cut(text))
    for word1 in words:
        if word1 not in stopkey:
            file.write(word1+" ")
    filecount += 1
file.close()
print("xrayo done 1172")


file = open("E://AA//word2vec//corpus.txt",'a', encoding='utf-8')

file1 = open("E://mc//book//jiebabook.txt",'r', encoding='utf-8')
text=file1.read()
file.write(text)
file1.close()
file2 = open("E://mc//emri//jiebaemri.txt",'r', encoding='utf-8')
text=file2.read()
file.write(text)
file2.close()
file3 = open("E://mc//emr//jiebaemro.txt",'r', encoding='utf-8')
text=file3.read()
file.write(text)
file3.close()
file4 = open("E://mc//xray//jiebaxrayi.txt",'r', encoding='utf-8')
text=file4.read()
file.write(text)
file4.close()
file5 = open("E://mc//xray//jiebaxrayo.txt",'r', encoding='utf-8')
text=file5.read()
file5.close()
file.write(text)

file.close()
print ("done")
