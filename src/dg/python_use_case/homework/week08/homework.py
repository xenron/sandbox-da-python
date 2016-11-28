# -*- coding: utf-8 -*-

###评论提取###
import pandas as pd

inputfile = 'd:/data/example08/huizong.csv' #评论汇总文件
outputfile = 'd:/data/example08/meidi_jd.txt' #评论提取后保存路径
data = pd.read_csv(inputfile, encoding = 'utf-8')
data = data[[u'评论']][data[u'品牌'] == u'美的']
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')


###数据预处理###
#文本去重
inputfile = 'd:/data/example08/meidi_jd.txt' #评论文件
outputfile = 'd:/data/example08/meidi_jd_process_1.txt' #评论处理后保存路径
data = pd.read_csv(inputfile, encoding = 'utf-8', header = None)
data=data.dropna()     
l1 = len(data)
data = pd.DataFrame(data[0].unique())
l2 = len(data)
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')
print(u'删除了%s条评论。' %(l1 - l2))


#机械压缩去词
def cutword(strs,reverse=False):
        s1=[]
        s2=[]
        s=[]
        if reverse :
            strs=strs[::-1]
        s1.append(strs[0])
        for i in strs[1:]:
            if i==s1[0] :
                if len(s2)==0:
                    s2.append(i)
                else :
                    if s1==s2:
                        s2=[]
                        s2.append(i)
                    else:
                        s=s+s1+s2
                        s1=[]
                        s2=[]
                        s1.append(i)
            else :
                if s1==s2 and len(s1)>=2 and len(s2)>=2:
                    s=s+s1
                    s1=[]
                    s2=[]
                    s1.append(i)
                else:
                    if len(s2)==0:
                        s1.append(i)
                    else :
                        s2.append(i)
        if s1==s2:
            s=s+s1
        else:
            s=s+s1+s2
        if reverse :
#            print ''.join(s[::-1])
            return ''.join(s[::-1])
        else:
#            print ''.join(s)
            return ''.join(s)
        
data2 = data.iloc[:,0].apply(cutword)         
data2 = data2.apply(cutword,reverse=True)
          
#短句过滤
data3=data2[data2.apply(len)>=4]
                    
###模型构建###
#情感分析
from snownlp import SnowNLP

coms=[]

coms=data3.apply(lambda x: SnowNLP(x).sentiments)
#for com in data3:
#    coms.append(SnowNLP(com).sentiments)
#coms=pd.Series(coms)
#coms.index=data3.index

data1=data3[coms>=0.5]
data2=data3[coms<0.5]


#分词
import jieba

mycut = lambda s: ' '.join(jieba.cut(s)) #自定义简单分词函数
data1 = data1.apply(mycut) #通过“广播”形式分词，加快速度。
data2 = data2.apply(mycut)

#outputfile1 = 'd:/data/example08/meidi_jd_pos_cut.txt'
#outputfile2 = 'd:/data/example08/meidi_jd_neg_cut.txt'
#data1.to_csv(outputfile1, index = False, header = False, encoding = 'utf-8') #保存结果
#data2.to_csv(outputfile2, index = False, header = False, encoding = 'utf-8')          

#去除停用词
stoplist = 'd:/data/example08/stoplist.txt'

stop = pd.read_csv(stoplist, encoding = 'utf-8', header = None, sep = 'tipdm')
#sep设置分割词，由于csv默认以半角逗号为分割词，而该词恰好在停用词表中，因此会导致读取出错
#所以解决办法是手动设置一个不存在的分割词，如tipdm。
stop = [' ', ''] + list(stop[0]) #Pandas自动过滤了空格符，这里手动添加

pos = pd.DataFrame(data1[:5000])
neg = pd.DataFrame(data2[:5000])

neg[1] = neg[0].apply(lambda s: s.split(' ')) #定义一个分割函数，然后用apply广播
neg[2] = neg[1].apply(lambda x: [i for i in x if i.encode('utf-8') not in stop]) #逐词判断是否停用词，思路同上
pos[1] = pos[0].apply(lambda s: s.split(' '))
pos[2] = pos[1].apply(lambda x: [i for i in x if i.encode('utf-8') not in stop])

#LDA主题分析
from gensim import corpora, models

#负面主题分析
neg_dict = corpora.Dictionary(neg[2]) #建立词典
neg_corpus = [neg_dict.doc2bow(i) for i in neg[2]] #建立语料库
neg_lda = models.LdaModel(neg_corpus, num_topics = 3, id2word = neg_dict) #LDA模型训练
for i in range(3):
    print 'topic',i
    print neg_lda.print_topic(i) #输出每个主题

#正面主题分析
pos_dict = corpora.Dictionary(pos[2])
pos_corpus = [pos_dict.doc2bow(i) for i in pos[2]]
pos_lda = models.LdaModel(pos_corpus, num_topics = 3, id2word = pos_dict)
for i in range(3):
    print 'topic',i
    print pos_lda.print_topic(i) #输出每个主题