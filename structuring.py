#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-18 17:18:08
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$
# -*- coding: utf-8 -*-
import os
import jieba

#wordvec获取语料库

jieba.load_userdict("E://mc//fenlei2//userdict.txt")


# words = list(jieba.cut(text))
# print('/'.join(words))


f = open("E://mc//xray//i0.txt", 'r', encoding='utf-8')
text = f.read().replace('，','').replace('：','').replace('。','').replace('；','').replace('【','').replace('】','').replace('及','').replace(',','')
print(text)
words = list(jieba.cut(text))
print(' '.join(words))
from gensim.models import word2vec
import logging


sumsimilarity = 0.0
maxsimilarity = 0.0
sentity = ""
count = 0
# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"E:\\AA\\word2vec\\corpus.txt")  # 加载语料
#初始获取模型
# model = word2vec.Word2Vec(sentences, size=20)  # 默认window=5
# model.save(u"mcjiabamy2.model")
model = word2vec.Word2Vec.load(u"mcjiabamy2.model")


filer = open("E://mc//xray//ri5.txt", 'a', encoding='utf-8')
filenum = 10
filecount = 0

#分类
for word in words:
    word = word.strip()
    print(word)
    if word=='，' or word=='。' or word=='：' or word=='、'or word=='【'or word=='】' or word==',' :
        continue
    maxmaxs = 0.0
    maxavg = 0.0
    jiegou = "实体:"
    filecount = 0
    while filecount < filenum:
        filecount += 1
        print(filecount)
        sumsimilarity = 0.0
        maxsimilarity = 0.0
        sentity = ""
        filename = ""
        count = 0
        avg1 = 0
        filen1 = open('E:/mc/fenlei2/'+str(filecount)+'.txt','r', encoding='UTF-8')
        for index,entity in enumerate(filen1):
            # print("index:"+str(index))
            if index == 0:
                filename = entity.strip()
                # print(str(filecount)+":::"+filename)
            else:
                # print(str(filecount)+"111")
                try:
                    entity = entity.strip()
                    # print(str(filecount)+"222"+entity+"3333"+word)
                    y1 = model.similarity(entity, word)
                    # print(str(filecount)+"333")
                    # print("y22:"+str(y1))
                    count += 1
                    sumsimilarity += y1
                    if maxsimilarity < y1:
                        maxsimilarity = y1
                        sentity = entity
                except KeyError:
                    pass
        filen1.close()
        if count == 0:
            avg1 = 0
        else:
            avg1 = sumsimilarity/count
        print (sentity+":"+"和【"+word+"】的最大相似度为："+str(maxsimilarity)+"平均相似度："+str(avg1))
        print(maxavg)
        print(maxsimilarity)
        if maxsimilarity > 0.99:
            jiegou = filename
            break
        elif maxavg < maxsimilarity:
            jiegou = filename

    filer.write(jiegou+":"+word+"\n")
print("done")

