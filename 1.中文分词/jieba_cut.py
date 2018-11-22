# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:14:09 2018

@author: xubing
"""
import jieba
sent = '中文分词是文本处理不可或缺的一步'

seg_list = jieba.cut(sent,cut_all = True)
print('全模式：','/'.join(seg_list))#所有可能词扫描出来，速度快，但不能解决歧义。

seg_list = jieba.cut(sent,cut_all = False)
print('精确模式：','/'.join(seg_list))#试图将句子最精确地分开，适合文本分析。也是默认的模式。

seg_list = jieba.cut_for_search(sent)
print('搜索引擎模式：','/'.join(seg_list))#在精确的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
