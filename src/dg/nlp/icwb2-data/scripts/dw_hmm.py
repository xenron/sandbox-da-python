#!/usr/bin/python
# encoding: utf-8
from __future__ import division
import codecs
import sys

def cleanASCII(contents):
    # 训练文本清洗，删除不必要的ascii字符等

    return contents

#学习训练文本
def HMMpara(tf):
    f = codecs.open(tf, 'r',' utf-8')
    contents = f.read()
    f.close()

    # 清洗、分词、存入列表
contents = cleanASCII(contents)
    tblWords = contents.split()

    # 建立字表、标注BMES、求转移矩阵、求发射矩阵
tblChar = []
    State = ["B", "M", "E", "S"]
    matrixA = [[0 for col in range(0, 4)] for row in range(0, 4)]
    matrixB = []
    # 对未学习到的字符，赋予通用概率    matrixB.append([0.3, 0.3, 0.1, 0.3])
    tblChar.append(u' ')

    return matrixA, zip(*matrixB) , tblChar

# 维特比算法

def viterbi_proc(O, Pi, A, B, K):
    N = len(A)
    T = len(O)

    path = [-1 for i in range(0, T)]

    return path

# 分词、写入结果

def divideWords(matrix, test_file, result_file):
    fr = codecs.open(test_file, 'r', 'utf-8')
    test = fr.read()
    fr.close()

    pi = [0.3, 0.1, 0.3, 0.3]
    A = matrix[0]
    B = matrix[1]
    K = matrix[2]


    fw = codecs.open(result_file,'w','utf-8')
     for c in test:
          #利用标点分句

          #调用维特比算法

          #保存句子分词结果
    fw.close()

def main():
    """
    args = sys.argv[1:]
    if len(args) < 3:
        print 'Usage: python dw.py dict_path test_path result_path'
        exit(-1)
    dict_path = args[0]
    test_path = args[1]
    result_path = args[2]
    """
train_file = "pku_training.utf8"
test_file = "pku_test.utf8"
result_file = "pku_result.utf8"
matrix = HMMpara(train_file)
    divideWords(matrix, test_file, result_file)

if __name__ == "__main__":
    main()
