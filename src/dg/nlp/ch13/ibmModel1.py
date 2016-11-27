#coding=utf-8
import os

#Read File to pairs
fp_en = open('D:/tmp/data.e','r')
fp_cn = open('D:/tmp/data.f','r')
iters = 1
pairDic = {}

#生成原始序对字典
countPair = 0
for line_cn,line_en in zip(fp_cn,fp_en):
    f = line_cn.split()
    e = line_en.split()
    for word1 in f:
        for word2 in e:
            pairDic[countPair] = (word1, word2)
            countPair += 1
    iters += 1
fp_en.close()
fp_cn.close()


#先将序对字典一次性去重
lst = list(set(pairDic.values()))
#print "lst=",lst
NewpairDic = {}
i = 0
foreign,english = [],[]
for _tuple in lst:
    #生成新的序对字典
    NewpairDic[i] = _tuple
    i += 1
#print "pairs=",NewpairDic

# run ibm-model-1(EM)
t = {}
for key in NewpairDic.values():
    t[key]=0.25  #initialize t(e|f) uniformly

print "Initial="
for k,v in t.items():
    print str((k[1], k[0])) + " : " + str(v)

K = 0
# while not converged
while K <= 4:
    fp_en = open('D:/tmp/data.e', 'r')
    fp_cn = open('D:/tmp/data.f', 'r')
    count, total = {}, {}
    for key in NewpairDic.values():
        count[key] = 0
    for _tuple in NewpairDic.values():
        total[_tuple[0]] = 0
    s_total = {}
    for ee, ff in zip(fp_en,fp_cn):
        # compute normalization
        for e in ee.split():
            s_total[e] = 0
            for f in ff.split():
                s_total[e] += t[(f, e)]
        # collect counts
        for e in ee.split():
            for f in ff.split():
                count[(f, e)] += t[(f, e)]/s_total[e]
                total[f] += t[(f, e)]/s_total[e]
    # estimate probabilities
    for f,e in NewpairDic.values():
        t[(f,e)] = count[(f,e)]/total[f]
    # end of while
    K += 1
    fp_en.close()
    fp_cn.close()
    print "it %d= " %K
#    for it in t.items():
#        print it
    for k, v in t.items():
        print str((k[1], k[0])) + " : " + str(v)
