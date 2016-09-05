# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:04:24 2016

@author: Administrator
"""
import jieba


def segword(path,output):
    #读取文件
    fil = open(path).read()
    #分词
    seg_list = jieba.cut(str(fil),cut_all=False)
    seg_list2 = "/ ".join(seg_list)
    
    #分词结果导出
    fout = open (output,'w')
    fout.write(seg_list2.encode('utf-8'))
    fout.close()
    
path=r'd:/data/sampledata.txt'
output=r'd:/data/sampledata2.txt'

segword(path,output)