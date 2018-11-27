# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:05:04 2018

@author: xubing
"""
import jieba.posseg as psg
sent = '词性标注是自然语言处理中不可或缺的一步！'
seg_list = psg.cut(sent)

print(''.join(['{0}/{1} '.format(w,t) for w,t in seg_list]))
