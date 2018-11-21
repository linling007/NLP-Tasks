# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:19:35 2018

@author: xubing
"""

class MM(object):
    def __init__(self):
        self.window_size = 3
    
    def cut(self,text):
        result = []
        index = 0
        text_length = len(text)
        dic = ['研究','研究生','生命','命','的','起源']
        while text_length > index:
            for size in range(self.window_size + index,index,-1):
                piece = text[index:size]
                #print(piece)
                if piece in dic:
                    index = size - 1
                    break
            index += 1
            result.append(piece + '---')
        return result
        
if __name__ == '__main__':
    text = '研究生命的起源'
    tokenizer = MM()
    print(tokenizer.cut(text))
        