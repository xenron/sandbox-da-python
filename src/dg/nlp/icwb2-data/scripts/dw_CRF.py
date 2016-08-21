# -*- coding: utf-8 -*-
import codecs
import sys
import time
from collections import Counter
import numpy as np
import pandas as pd
import math


# 由规则处理的一些特殊符号
numMath = [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9',u'／',u'.']
numMath_suffix = [u'％', u'亿', u'万', u'千', u'百', u'十', u'个']
numCn = [u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'○', u'零', u'十']
numCn_suffix_date = [u'年', u'月', u'日']
numCn_suffix_unit = [u'亿', u'万', u'千', u'百', u'十', u'个']
charEn = [chr(i) for i in range(ord("a"),ord("z")+1)]
charEn.extend([chr(i) for i in range(ord("A"),ord("Z")+1)])
charDot = [u'.']
sentence_end_char = [u'，', u'。', u'、', u'！', u'\r', u'\n', u'《', u'》',u'？',u'(', u')',u'；',u'“',u'（',u'）',u'/',u'\\',u'：',u'——']

def proc_num_math(line, start):
    """ 处理句子中出现的数学符号 """
    oldstart = start
    while line[start] in numMath or line[start] in numMath_suffix:
        start = start + 1
    if line[start] in numCn_suffix_date:
        start = start + 1
    return start - oldstart

def proc_num_cn(line, start):
    """ 处理句子中出现的中文数字 """
    oldstart = start
    while line[start] in numCn or line[start] in numCn_suffix_unit:
        start = start + 1
    if line[start] in numCn_suffix_date:
        start = start + 1
    return start - oldstart

def proc_char_en(line, start):
    """ 处理句子中出现的英文 """
    oldstart = start
    while line[start] in charEn or line[start] in charDot or line[start] in numMath:
        start = start + 1
    return start - oldstart

def rules(line, start):
    """ 处理特殊规则 """
    if line[start] in numMath:
        return proc_num_math(line, start)
    elif line[start] in numCn:
        return proc_num_cn(line, start)
    elif line[start] in charEn:
        return proc_char_en(line, start)
   
def genDict(dict_path):
    f_train = codecs.open(dict_path,'r','utf-8')
    contents = f_train.read() 
    
    """ 统计字频 """
    contents_char = list(contents)
    char_dict_count = Counter(contents_char)
    # 字典
    char_dict = list(set(list(contents)))

    """ 统计词频 """
    contents_word = contents.replace(u'\r', u'')
    contents_word = contents_word.replace(u'\n', u'')
    # 将文件内容按空格分开
    word_dict = contents_word.split(u' ')
    if len(word_dict) == 1:
        word_dict = contents_word.split(u'\u3000')        
    word_dict_count = Counter(word_dict)
    word_set_dict = list(set(word_dict))
    try:
        word_set_dict.remove(u'')
    except:
        word_set_dict = word_set_dict
    f_train.close

    """ 统计发射矩阵"""
    """ 
    一元：当前字的SBME    {'char':[S,B,M,E]} 
    二元及以上：第一个字的BM和最后一个字的ME         {'word':[B1,M1,M2,E2]}
    *基于性能出发，考虑到S比较独立，跟前后关系不大，不做二元以上统计，只对词频库扫描。
    """
    char_matrix = {}
    for char in char_dict:
        char_matrix[char] = [0,0,0,0]
    char_matrix[u'\r'] = [1,0,0,0]
    char_matrix[u'\n'] = [1,0,0,0]
    char_matrix[u' '] = [1,0,0,0]
    for word in word_set_dict:
        lw = len(word)
        if lw == 1:
            #统计'S'
            char_matrix[word][0] = word_dict_count[word]
        elif lw == 2:
            #统计'B'
            char_matrix[word[0]][1] += word_dict_count[word]
            try:
                char_matrix[word[0:2]][0] += word_dict_count[word]
            except:
                char_matrix[word[0:2]] = [0,0,0,0]
                char_matrix[word[0:2]][0] += word_dict_count[word]
            #统计'E'
            char_matrix[word[1]][3] += word_dict_count[word]
            try:
                char_matrix[word[0:2]][3] += word_dict_count[word]
            except:
                char_matrix[word[0:2]] = [0,0,0,0]
                char_matrix[word[0:2]][3] += word_dict_count[word]
        else:
            #统计'B'
            char_matrix[word[0]][1] += word_dict_count[word]
            #统计'E'
            char_matrix[word[lw-1]][3] += word_dict_count[word]
            #统计'M'，及二元以上      
            while lw > 2:
                #一元，M
                char_matrix[word[lw-2]][2] += word_dict_count[word] 
                #二元以上              
                for p in range(1,lw):
                    #统计'B1'
                    try:
                        char_matrix[word[0:p+1]][0] += word_dict_count[word]
                    except:
                        char_matrix[word[0:p+1]] = [0,0,0,0]
                        char_matrix[word[0:p+1]][0] += word_dict_count[word]
                    #统计'M1',M2',中间
                    for l in range(p+1,lw-1):
                        #统计'M1',中间
                        try:
                            char_matrix[word[p:l+1]][1] += word_dict_count[word]
                        except:
                            char_matrix[word[p:l+1]] = [0,0,0,0]
                            char_matrix[word[p:l+1]][1] += word_dict_count[word]
                        #统计'M2',中间
                        try:
                            char_matrix[word[p:l+1]][2] += word_dict_count[word]
                        except:
                            char_matrix[word[p:l+1]] = [0,0,0,0]
                            char_matrix[word[p:l+1]][2] += word_dict_count[word]
                    #统计'M1',到最后
                    try:
                        char_matrix[word[p:lw]][1] += word_dict_count[word]
                    except:
                        char_matrix[word[p:lw]] = [0,0,0,0]
                        char_matrix[word[p:lw]][1] += word_dict_count[word]
                    #统计'M2',到最后
                    try:
                        char_matrix[word[p:lw]][2] += word_dict_count[word]
                    except:
                        char_matrix[word[p:lw]] = [0,0,0,0]
                        char_matrix[word[p:lw]][2] += word_dict_count[word]
                    #统计'E2'
                    try:
                        char_matrix[word[p:lw]][3] += word_dict_count[word]
                    except:
                        char_matrix[word[p:lw]] = [0,0,0,0]
                        char_matrix[word[p:lw]][3] += word_dict_count[word]
                lw = lw - 1
    return char_matrix        

def divideWords(char_matrix,sentence):        
    """
    根据标点符号分句，
    对每个句子，用CRF分词，
    计算S,B,M,E的概率，用维特比算法
    """
    ruleChar = []
    ruleChar.extend(numCn)
    ruleChar.extend(numMath)
    ruleChar.extend(charEn)
    sentence_end_char.extend(numMath)
    sentence_end_char.extend(charEn)
    max_wl = max(len(i) for i in char_matrix.keys())
    char_dict = [i for i in char_matrix.keys() if len(i) == 1]
    char_count = len(char_dict)
    total_chars = sum(sum(char_matrix[i]) for i in char_dict)
    result = u''                        
    start = 0
    senlen = len(sentence)
    while start < senlen:
        curword = sentence[start]
        maxlen = 1
        # 首先查看是否可以匹配特殊规则
        if curword in ruleChar:
            maxlen = rules(sentence, start)

        d_word = sentence[start:start+maxlen]

        # 用CRF 对句子分词
        if maxlen == 1 and curword not in sentence_end_char:
            # 切分下一句
            while curword not in sentence_end_char and (start + maxlen ) < senlen and not(curword in numCn and sentence[start + maxlen] in numCn):
                curword = sentence[start + maxlen]
                maxlen = maxlen + 1
                
            if maxlen > 1 and (start + maxlen ) < senlen:
                maxlen = maxlen - 1

            d_s = sentence[start:start+maxlen]
            lds = len(d_s)
            if lds <= 1:
                d_word = d_s
            else:
                #状态转移矩阵
                st_matrix = np.array([[0.5,0.5,0,0],[0,0,0.5,0.5],[0,0,0.5,0.5],[0.5,0.5,0,0]])
                #初始发射矩阵
                try:
                    if sum(char_matrix[d_s[0]][0:2]) <> 0:
                        max_p += np.array(char_matrix[d_s[0]][0:2] + [0,0])
                        max_p = max_p / sum(max_p)
                    else:
                        max_p = np.array([0.5,0.5,0,0])
                except:
                    max_p = np.array([0.5,0.5,0,0])
                #默认概率
                #如果字符没在词频库出现过，使用默认概率
                default_p = np.array([0.25,0.25,0.25,0.25])
                #用维特比算法
                node_array = np.zeros((4,lds))
                for s in range(1,lds):
                    #当前节点到下一个节点的概率矩阵
                    max_t = st_matrix.T * max_p
                    p_matrix = np.zeros((4))  
                    try:
                        sc = sum(char_matrix[d_s[s]])
                        if sc == 0:
                            p_matrix = default_p
                        else:
                            #一元                        
                            p_matrix += np.array(char_matrix[d_s[s]],float)/sc
                            #二元以上, k 元
                            k = 2
                            while k < max_wl :
                                p_matrix2 = np.zeros((4))
                                #计算B,M 后向
                                if s + k < lds:
                                    try:
                                        p_matrix2[1] += float(char_matrix[d_s[s:s+k]][0])
                                        p_matrix2[2] += float(char_matrix[d_s[s:s+k]][1])
                                    except:
                                        p_matrix2 = p_matrix2

                                #计算M,E,前向
                                if s - k + 2 > 0:
                                    try:
                                        p_matrix2[2] += float(char_matrix[d_s[s-k+1:s+1]][2])
                                        p_matrix2[3] += float(char_matrix[d_s[s+1-k:s+1]][3])
                                    except:
                                        p_matrix2 = p_matrix2                                        
                                #计算S，按平均分布
                                p_matrix2[0] += float(char_matrix[d_s[s]][0])/math.pow(char_count,(k-1))
                                p_matrix = p_matrix/sum(p_matrix)
                                #加权
                                p_matrix2 = p_matrix2 * k #math.e**(k-1)
                                p_matrix += p_matrix2 
                                k = k + 1
                        #平滑,归一化
                        p_matrix = p_matrix/sum(p_matrix)  + 1/char_count
                        p_matrix = p_matrix/sum(p_matrix)
                        max_t = max_t.T * p_matrix
                    except:
                        max_t = max_t.T * default_p
                    #结束判断
                    if s == lds - 1:
                        max_t = max_t * np.array([1,0,0,1])
                    #计算当前节点的最优概率和记录前面节点
                    for j in range(0,4):
                        max_p[j] = max(max_t[:,j])
                        node_array[j,s] = list(max_t[:,j]).index(max_p[j])

                #计算最后最优节点
                last_node = list(max_p).index(max(max_p))
                
                #根据标识分词                
                d_word = u''
                for i in range(lds - 1,0, -1 ):
                    d_word = d_s[i] + d_word
                    last_node = node_array[last_node,i]
                    if last_node in [0,3]:
                        d_word = u' ' + d_word
                d_word = d_s[0] + d_word
        result = result + d_word + u' '
        start = start + maxlen
    return result

def main():
    args = sys.argv[1:]
    if len(args) < 3:
        print 'Usage: python dw.py dict_path test_path result_path'
        exit(-1)
    dict_path = args[0]
    test_path = args[1]
    result_path = args[2]

    print time.asctime( time.localtime(time.time()))
    char_matrix = genDict(dict_path)
  
    print time.asctime( time.localtime(time.time()) )
    fr = codecs.open(test_path,'r','utf-8')
    test = fr.read()
    result = divideWords(char_matrix,test)
    fr.close()
    fw = codecs.open(result_path,'w','utf-8')
    fw.write(result)
    fw.close()
    
    print time.asctime(time.localtime(time.time()) )
if __name__ == "__main__":
    main()
