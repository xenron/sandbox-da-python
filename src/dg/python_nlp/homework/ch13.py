# -*- coding: utf-8 -*-

from os import path
import os
import re
import codecs
import pandas as pd
import numpy as np

rootdir = 'D:/tmp/SogouC.mini.20061102/Sample'
dirs = os.listdir(rootdir)
dirs = [path.join(rootdir,f) for f in dirs if f.startswith('C')]
dirs

def load_txt(x):
    with open(x) as f:
        res = [t.decode('gbk','ignore') for t in f]
        return ''.join(res)

print load_txt('D:/tmp/SogouC.mini.20061102/Sample/C000024/10.txt')

text_t = {}
for i, d in enumerate(dirs):
    files = os.listdir(d)
    files = [path.join(d, x) for x in files if x.endswith('txt') and not x.startswith('.')]
    text_t[i] = [load_txt(f) for f in files]

flen = [len(t) for t in text_t.values()]
labels = np.repeat(text_t.keys(),flen)

# flatter nested list
import itertools
merged = list(itertools.chain.from_iterable(text_t.values()))

df = pd.DataFrame({'label': labels, 'txt': merged})
df.head()

df['ready_seg'] =df['txt'].str.replace(ur'\W+', ' ',flags=re.U)  # 非正常字符转空格
df['ready_seg'] =df['ready_seg'].str.replace(r'[A-Za-z]+', ' ENG ')   # 英文转ENG
df['ready_seg'] =df['ready_seg'].str.replace(r'\d+', ' NUM ')   # 数字转NUM

# cut word
import jieba
def cutword_1(x):
    words = jieba.cut(x)
    return ' '.join(words)

df['seg_word'] = df.ready_seg.map(cutword_1)

df.head()

textraw = df.seg_word.values.tolist()
textraw = [line.encode('utf-8') for line in textraw] # 需要存为str才能被keras使用

# keras处理token
maxfeatures = 50000 # 只选择最重要的词
from keras.preprocessing.text import Tokenizer
token = Tokenizer(nb_words=maxfeatures)
token.fit_on_texts(textraw) #如果文本较大可以使用文本流
text_seq = token.texts_to_sequences(textraw)

np.median([len(x) for x in text_seq]) #  每条新闻平均400个词汇

y = df.label.values # 定义好标签
nb_classes = len(np.unique(y))
print(nb_classes)

from __future__ import absolute_import
from keras.optimizers import RMSprop
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.embeddings import Embedding
from keras.layers.convolutional import Convolution1D, MaxPooling1D
from keras.layers.recurrent  import SimpleRNN, GRU, LSTM
from keras.callbacks import EarlyStopping
from keras.utils import np_utils, generic_utils

maxlen = 600 # 定义文本最大长度
batch_size = 32 # 批次
word_dim = 100 # 词向量维度
nb_filter = 200  # 卷积核个数
filter_length = 10 # 卷积窗口大小
hidden_dims = 50  # 隐藏层神经元个数
nb_epoch = 10      # 训练迭代次数
pool_length = 50   # 池化窗口大小

from sklearn.cross_validation import train_test_split
train_X, test_X, train_y, test_y = train_test_split(text_seq, y , train_size=0.8, random_state=1)

# 转为等长矩阵，长度为maxlen
print("Pad sequences (samples x time)")
X_train = sequence.pad_sequences(train_X, maxlen=maxlen,padding='post', truncating='post')
X_test = sequence.pad_sequences(test_X, maxlen=maxlen,padding='post', truncating='post')
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

# 将y的格式展开成one-hot
Y_train = np_utils.to_categorical(train_y, nb_classes)
Y_test = np_utils.to_categorical(test_y, nb_classes)

# CNN 模型
print('Build model...')
model = Sequential()

# 词向量嵌入层，输入：词典大小，词向量大小，文本长度
model.add(Embedding(maxfeatures, word_dim,input_length=maxlen)) 
model.add(Dropout(0.25))
model.add(Convolution1D(nb_filter=nb_filter,
                        filter_length=filter_length,
                        border_mode="valid",
                        activation="relu"))
# 池化层
model.add(MaxPooling1D(pool_length=pool_length))
model.add(Flatten())
# 全连接层
model.add(Dense(hidden_dims))
model.add(Dropout(0.25))
model.add(Activation('relu'))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

earlystop = EarlyStopping(monitor='val_loss', patience=1, verbose=1)
result = model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch, 
            validation_split=0.1, show_accuracy=True,callbacks=[earlystop])

score = earlystop.model.evaluate(X_test, Y_test, batch_size=batch_size)
print('Test score:', score)
classes = earlystop.model.predict_classes(X_test, batch_size=batch_size)
acc = np_utils.accuracy(classes, test_y) # 要用没有转换前的y
print('Test accuracy:', acc)

