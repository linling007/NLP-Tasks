# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 18:14:38 2018

@author: xubing
"""

'''
由于gensim和sklearn里都不能很准确地得到此的tf-idf值
'''
from collections import Counter 
import numpy as np
import math
import jieba
class calc_tfidf(object):
     
    def __init__(self):
       
        pass     
    def text_proc(raw_texts):
        '''
        输入数据为一个列表，列表中的每个元素是一个文档。
        输出为分词后的二维列表和二维列表展开后的一维列表。
        这里没有去处停止词。
        '''
        texts_set = set()
        texts_list = []
        texts = []
        for text in raw_texts:
            line = []
            for item in jieba.cut(text):
                line.append(item)
                texts_set.add(item)
                texts_list.append(item)
            texts.append(line)
        #print('不重复的词：',len(texts_set))
        del texts_set
        return texts,texts_list      

    def tfidf_Method(texts):
        '''
        输入为分词后的二维列表。
        '''
        c = 0
        tfidf_list = []
        for text in texts:
            tfidf_line = []
            count = Counter(text)
            for word in text:#计算每篇文章的每个词的tfidf
                tf = count[word]/len(text)#计算tf值，term frequency。计算该词在本篇文章中出现的频率。
                
                n_contain = sum(1 for text in texts if word in text)#计算包含该词的文章数
                idf = math.log(len(texts)+1/n_contain)#inverse document frequency 文章总数/包含该词的文章数 再取对数。
               #分子加1视为了防止出现log1=0的情况，被包含的数量总是小于总数+1的。
                tfidf = tf*idf
                
                tfidf_line.append(tfidf)
                c+=1
            tfidf_list.append(tfidf_line)
            tfidf_array = np.array(tfidf_list)
        return tfidf_array

#一个简单的例子理解
if __name__ == '__main__':
    raw_texts = ['TF-IDF是一种统计方法，用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。',
                 '字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降。',
                 'TF-IDF加权的各种形式常被搜索引擎应用，作为文件与用户查询之间相关程度的度量或评级。',
                 '除了TF-IDF以外，因特网上的搜索引擎还会使用基于链接分析的评级方法，以确定文件在搜寻结果中出现的顺序。']            
    texts,texts_list = calc_tfidf.text_proc(raw_texts)
    tfidf_array  = calc_tfidf.tfidf_Method(texts)
