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


2. ○ Write a tag pattern to match noun phrases containing plural head nouns, e.g.,
many/JJ researchers/NNS, two/CD weeks/NNS, both/DT new/JJ positions/NNS. Try
to do this by generalizing the tag pattern that handled singular noun phrases.
2. ○写一个标记模式匹配包含复数中心名词在内的名词短语，如many/JJ researchers
/NNS, two/CD weeks/NNS, both/DT new/JJ positions/NNS。通过泛化处理单
数名词短语的标记模式，尝试做这个。

6. ◑ Write one or more tag patterns to handle coordinated noun phrases, e.g., July/
NNP and/CC August/NNP, all/DT your/PRP$ managers/NNS and/CC supervisors/NNS,
company/NN courts/NNS and/CC adjudicators/NNS.
6. ◑写一个或多个标记模式处理有连接词的名词短语，如：July/NNP and/CC August
/NNP，all/DT your/PRP$ managers/NNS and/CC supervisors/NNS，compa
ny/NN courts/NNS and/CC adjudicators/NNS。


7. ◑ Carry out the following evaluation tasks for any of the chunkers you have developed
earlier. (Note that most chunking corpora contain some internal inconsistencies,
such that any reasonable rule-based approach will produce errors.)
a. Evaluate your chunker on 100 sentences from a chunked corpus, and report
the precision, recall, and F-measure.
b. Use the chunkscore.missed() and chunkscore.incorrect() methods to identify
the errors made by your chunker. Discuss.
c. Compare the performance of your chunker to the baseline chunker discussed
in the evaluation section of this chapter.
7. ◑用任何你之前已经开发的分块器执行下列评估任务。（请注意，大多数分块语料库包
含一些内部的不一致，以至于任何合理的基于规则的方法都将产生错误。）
a. 在来自分块语料库的100 个句子上评估你的分块器，报告精度、召回率和F 量度。
b. 使用chunkscore.missed()和chunkscore.incorrect()方法识别你的分块器的
错误，并讨论它。
c. 与本章的评估部分讨论的基准分块器比较你的分块器的性能。

17. ● An n-gram chunker can use information other than the current part-of-speech
tag and the n-1 previous chunk tags. Investigate other models of the context, such
as the n-1 previous part-of-speech tags, or some combination of previous chunk
tags along with previous and following part-of-speech tags.
17. ●一个n-gram 分块器可以使用除当前词性标记和n-1 个前面的块的标记以外其他信息。
调查其他的上下文模型，如n-1 个前面的词性标记，或一个写前面块标记连同前面和后
面的词性标记的组合。

