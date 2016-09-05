# -*- coding: utf-8 -*-
from nltk.corpus import wordnet as wn
import nltk
from nltk.corpus import *
from matplotlib import pylab
from nltk import word_tokenize
import re
import jieba
import jieba.posseg
import jieba.analyse
from nltk.corpus import brown
import nltk


# 2. Using any of the three classifiers described in this chapter, and any features you
can think of, build the best name gender classifier you can. Begin by splitting the
Names Corpus into three subsets: 500 words for the test set, 500 words for the
dev-test set, and the remaining 6,900 words for the training set. Then, starting with
the example name gender classifier, make incremental improvements. Use the devtest
set to check your progress. Once you are satisfied with your classifier, check
its final performance on the test set. How does the performance on the test set
compare to the performance on the dev-test set? Is this what you’d expect?
# 使用任何本章所述的三种分类器之一，以及你能想到的特征，尽量好的建立一个名字
性别分类器。从将名字语料库分成3 个子集开始：500 个词为测试集，500 个词为开发
测试集，剩余6900 个词为训练集。然后从示例的名字性别分类器开始，逐步改善。使
用开发测试集检查你的进展。一旦你对你的分类器感到满意，在测试集上检查它的最终
性能。相比在开发测试集上的性能，它在测试集上的性能如何？这是你期待的吗？


# 5. Select one of the classification tasks described in this chapter, such as name
gender detection, document classification, part-of-speech tagging, or dialogue act
classification. Using the same training and test data, and the same feature extractor,
build three classifiers for the task: a decision tree, a naive Bayes classifier, and a
Maximum Entropy classifier. Compare the performance of the three classifiers on
your selected task. How do you think that your results might be different if you
used a different feature extractor?


选择一个本章所描述的分类任务，如名字性别检测、文档分类、词性标注或对话行为
分类。使用相同的训练和测试数据，相同的特征提取器，建立该任务的三个分类器：决
策树、朴素贝叶斯分类器和最大熵分类器。比较你所选任务上这三个分类器的性能。你
如何看待如果你使用了不同的特征提取器，你的结果可能会不同？




# 9.The PP Attachment Corpus is a corpus describing prepositional phrase attachment
decisions. Each instance in the corpus is encoded as a PPAttachment object:
>>> from nltk.corpus import ppattach
>>> ppattach.attachments('training')
[PPAttachment(sent='0', verb='join', noun1='board',
prep='as', noun2='director', attachment='V'),
PPAttachment(sent='1', verb='is', noun1='chairman',
prep='of', noun2='N.V.', attachment='N'),
...]
>>> inst = ppattach.attachments('training')[1]
>>> (inst.noun1, inst.prep, inst.noun2)
('chairman', 'of', 'N.V.')
Select only the instances where inst.attachment is N:
>>> nattach = [inst for inst in ppattach.attachments('training')
... if inst.attachment == 'N']
Using this subcorpus, build a classifier that attempts to predict which preposition
is used to connect a given pair of nouns. For example, given the pair of nouns
team and researchers, the classifier should predict the preposition of. See the corpus
HOWTO at http://www.nltk.org/howto for more information on using the PP Attachment
Corpus.

PP 附件语料库是描述介词短语附着决策的语料库。语料库中的每个实例被编码为PP
Attachment 对象：
>>> from nltk.corpus import ppattach
>>> ppattach.attachments('training')
[PPAttachment(sent='0', verb='join', noun1='board',
prep='as', noun2='director', attachment='V'),
PPAttachment(sent='1', verb='is', noun1='chairman',
prep='of', noun2='N.V.', attachment='N'),
...]
>>> inst = ppattach.attachments('training')[1]
>>> (inst.noun1, inst.prep, inst.noun2)
('chairman', 'of', 'N.V.')
选择inst.attachment 为N 的唯一实例：
>>> nattach = [inst for inst in ppattach.attachments('training')
... if inst.attachment == 'N']
使用此子语料库，建立一个分类器，尝试预测哪些介词是用来连接一对给定的名词。
例如：给定的名词对team 和researchers，分类器应该预测出介词of。更多的使用PP
附件语料库的信息，参阅http://www.nltk.org/howto 上的语料库HOWTO。
