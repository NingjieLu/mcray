#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from gensim.models import word2vec
import chardet
import sys
from hashlib import md5
import hashlib

model = word2vec.Word2Vec.load(u"mcjiabamy2.model")
category_shiti=""
category_zhengzhuang=""
category_xibu=""
count = 2
for x in range(1,4):
    category_file = open('E:/mc/fenlei2/'+str(x)+'.txt','r', encoding='utf-8')
    if x == 1:
        category_shiti = category_file.readline().strip()
        # print("category_shiti"+category_shiti)
    elif x == 2:
        category_zhengzhuang = category_file.readline().strip()
        # print("category_zhengzhuang"+category_zhengzhuang)
    elif x == 3:
        category_xibu=category_file.readline().strip()
        print("category_xibu"+category_xibu)
    category_file.close()


def getCategory(word):
    print(word)
    maxmaxs = 0.0
    maxavg = 0.0
    jiegou = category_shiti
    filenum = 10
    filecount = 0
    while filecount < filenum:
        filecount += 1
        sumsimilarity = 0.0
        maxsimilarity = 0.0
        sentity = ""
        filename = ""
        count = 0
        avg1 = 0
        filen1 = open('E:/mc/fenlei2/'+str(filecount)+'.txt','r', encoding='utf-8')
        for index,entity in enumerate(filen1):
            if index == 0:
                filename = entity.strip()
            else:
                try:
                    entity = entity.strip()
                    y1 = model.similarity(entity, word)
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
        if maxsimilarity > 0.99:
            jiegou = filename
            break
        elif maxavg < maxsimilarity:
            jiegou = filename
    # if jiegou == category_zhengzhuang:
    #     print("aaaaaaaaa"+entity)
    return jiegou

if __name__ == '__main__':
    file = open('E://mc//xray//rei01.txt','r', encoding='UTF-8')
    filen = open('E://mc//xray//rei02.txt','a', encoding='UTF-8')


    for line in file:
        words = line.strip('\n').strip('\ufeff').strip(' ').split(" ")
        # print(words)
        # print(sys.getdefaultencoding())

        entities = []
        count_entity = 0
        xibu = ""
        for word in words:
            category = str(getCategory(word))
            # print("category22222"+category)

            # m2 = hashlib.md5()
            # m2.update(category.encode('utf-8'))
            # print(m2.hexdigest())
            # m2.update(category_zhengzhuang.encode('utf-8'))
            # print(m2.hexdigest())

            if category == category_shiti:
                entities.append(word)
                count_entity = count_entity+1
                # print("entity"+entity)
            elif category == category_xibu:
                xibu=word
                for num in range(0,count_entity):
                    filen.write(entities[num]+" 细部 "+word+"\n")
                # print(entities[num]+" 细部 "+word+"\n")
            elif category == category_zhengzhuang and xibu != '':
                filen.write(xibu+" 症状 "+word+"\n")
                # print(xibu+" 症状 "+word+"\n")
            elif category == category_zhengzhuang:
                for num in range(0,count_entity):
                    filen.write(entities[num]+" 症状 "+word+"\n")
                # print(entity+" 症状 "+word+"\n")

    filen.close()
    file.close()
    print("done")
