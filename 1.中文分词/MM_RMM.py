# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:34:03 2018

@author: xubing
"""

class MM_RMM(object):
    def __init__(self):
        self.window_size = 3
        
    def MM_cut(self,text):
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
        
    def RMM_cut(self,text):
        result = []
        index = len(text)
        dic = ['研究','研究生','生命','命','的','起源']
        while index > 0:
            for size in range(index - self.window_size,index):
                piece = text[size:index]
                if piece in dic:
                    index = size + 1
                    break
            index -= 1
            result.append(piece + '---')
        result.reverse()
        return result
    def result_cut(self,text):
        result1 = self.MM_cut(text)
        result2 = self.RMM_cut(text)
        if result1 == result2:
            return result2
        else:
            if len(result1) >= len(result2):
                return result2
            else:
                return result1
if __name__ == '__main__':
    text = '研究生命的起源'
    tokenizer = MM_RMM()
    print(tokenizer.result_cut(text))
        