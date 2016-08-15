# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 10:21:05 2016

@author: Administrator
"""

####数据类型####
#整数
a = 10
type(a)

a.bit_length()

a = 100000
a.bit_length()


googol = 10 ** 100
googol
type(googol) #长整型

googol.bit_length()

1+4
1/4
type(1 / 4)



#浮点数
1. / 4
type (1. / 4)

b = 0.35
type(b)

b + 0.1

c = 0.5
c.as_integer_ratio()

b.as_integer_ratio()

import decimal
from decimal import Decimal

decimal.getcontext()
d = Decimal(1) / Decimal (11)
d

decimal.getcontext().prec = 4 

e = Decimal(1) / Decimal (11)
e

decimal.getcontext().prec = 50

f = Decimal(1) / Decimal (11)
f

g = d + e + f
g

#字符串
t = 'this is a string object'

t.capitalize()

t.split()

t.find('string')

t.find('Python')

t.replace(' ', '|')

'http://www.python.org'.strip('htp:/')

import re

series = """
'01/18/2014 13:00:00', 100, '1st';
'01/18/2014 13:30:00', 110, '2nd';
'01/18/2014 14:00:00', 120, '3rd'
"""

dt = re.compile("'[0-9/:\s]+'") 

result = dt.findall(series)
result

from datetime import datetime
pydt = datetime.strptime(result[0].replace("'", ""),
                         '%m/%d/%Y %H:%M:%S')
pydt



print pydt

print type(pydt)

#日期与时间
import time;  # This is required to include time module.

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

localtime = time.localtime(time.time())
print "Local current time :", localtime


import calendar

cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal

#布尔型
True
False
3 > 2
3 > 5

True and True
True and False
False and False

True or True
True or False
False or False

not True
not False

#复数
a=3+4j
b=1+2j
c=a+b
c.real
c.imag


####基本数据结构####
#元组
t = (1, 2.5, 'data')
type(t)

t = 1, 2.5, 'data',1
type(t)

t[2]
type(t[2])

t.count('data')
t.index(1)

#列表
l = [1, 2.5, 'data']
l[2]
l = list(t)
l

type(l)

l.append([4, 3])  
l

l.extend([1.0, 1.5, 2.0])  # append elements of list
l

l.insert(1, 'insert')  # insert object before index position
l


l.remove('data')  # remove first occurence of object
l

p = l.pop(3)  # removes and returns object at index
print l, p

l[2:5]

#字典
d = {
     'Name' : 'Angela Merkel',
     'Country' : 'Germany',
     'Profession' : 'Chancelor',
     'Age' : 60
     }
type(d)
print d['Name'], d['Age']

d.keys()

d.values()

d.items()

birthday = True
if birthday is True:
    d['Age'] += 1
print d['Age']

for item in d.iteritems():
    print item
    
for value in d.itervalues():
    print type(value)
    
#集合
s = set(['u', 'd', 'ud', 'du', 'd', 'du'])
s

t = set(['d', 'dd', 'uu', 'u'])
s.union(t)
s.intersection(t)
s.difference(t) 
t.difference(s)  
s.symmetric_difference(t)

from random import randint
l = [randint(0, 10) for i in range(1000)]
    # 1,000 random integers between 0 and 10
len(l) 

l[:20]

s = set(l)
s

####控制结构####
#条件判断
'''
if 判断条件：
    执行语句……
else：
    执行语句……
'''

flag = False
name = 'python'
if name == 'python':         # 判断变量否为'python'
    flag = True              # 条件成立时设置标志为真
    print 'welcome boss'    # 并输出欢迎信息
else:
    print name              # 条件不成立时输出变量名称

'''
if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……
'''

num = 2     
if num == 3:            # 判断num的值
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出

num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print 'hello'


num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine'


num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
    print 'hello'
else:
    print 'undefine'


var = 100  
if ( var  == 100 ) : print "变量 var 的值为100" 
print "Good bye!"

##循环语句
#while语句
'''
while 判断条件：
    执行语句……
'''
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"

# continue 和 break 用法

i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

#死循环
'''
var = 1
while var == 1 :  # 该条件永远为true，循环将无限执行下去
   num = raw_input("Enter a number  :")
   print "You entered: ", num

print "Good bye!"
'''


#while … else 
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

#简单语句组
flag = 1
while (flag): print 'Given flag is really true!';flag=0;
print "Good bye!"

#for语句
'''
for iterating_var in sequence:
   statements(s)
'''
for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前水果 :', fruit

print "Good bye!"

#序列索引迭代
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print '当前水果 :', fruits[index]

print "Good bye!"

#for...else
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

#嵌套循环
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1

print "Good bye!"

#break语句
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break

print "Good bye!"

#continue语句
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print '当前字母 :', letter

var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print '当前变量值 :', var
print "Good bye!"

#pass语句
# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

print "Good bye!"



####自定义函数####
'''
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]		
'''

def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print str
   return

#函数调用
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "函数内取值: ", mylist
   return
 
# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print "函数外取值: ", mylist


#参数
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;
 
#调用printme函数
printme();

printme( str = "My string");



def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age ", age;
   return;
 
#调用printinfo函数
printinfo( age=50, name="miki" );


def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age ", age;
   return;
 
#调用printinfo函数
printinfo( age=50, name="miki" );
printinfo( name="miki" );

#不定长参数
'''
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return;
 
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );


#匿名函数
'''
lambda [arg1 [,arg2,.....argn]]:expression
'''

sum = lambda arg1, arg2: arg1 + arg2;
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )


#return语句
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print "函数内 : ", total
   return total;
 
# 调用sum函数
total = sum( 10, 20 );
print "函数外 : ", total 


#变量的作用范围
total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2; # total在这里是局部变量.
   print "函数内是局部变量 : ", total
   return total;
 
#调用sum函数
sum( 10, 20 );
print "函数外是全局变量 : ", total 


####numpy数据结构####
v = [0.5, 0.75, 1.0, 1.5, 2.0] 
m = [v, v, v]  # matrix of numbers
m

m[1]

m[1][0]

v1 = [0.5, 1.5]
v2 = [1, 2]
m = [v1, v2]
c = [m, m]  # cube of numbers
c

c[1][1][0]

v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = [v, v, v]
m

v[0] = 'Python'
m

from copy import deepcopy
v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = 3 * [deepcopy(v), ]
m

v[0] = 'Python'
m

import numpy as np

a = np.array([0, 0.5, 1.0, 1.5, 2.0])
type(a)

a[:2]
 
a.sum()
a.std()
a.cumsum()
a * 2
a ** 2
np.sqrt(a)

b = np.array([a, a * 2])
b
b[0]
b[0, 2]  # third element of first row

b.sum()
b.sum(axis=0)
b.sum(axis=1)

c = np.zeros((2, 3, 4), dtype='i', order='C')  # also: np.ones()
c

d = np.ones_like(c, dtype='f', order='C')  # also: np.zeros_like()
d

import random
I = 5000 

get_ipython().magic('time mat = [[random.gauss(0, 1) for j in range(I)] for i in range(I)]')
get_ipython().magic('time reduce(lambda x, y: x + y,  [reduce(lambda x, y: x + y, row)  for row in mat])')
get_ipython().magic('time mat = np.random.standard_normal((I, I))')
get_ipython().magic('time mat.sum()')

dt = np.dtype([('Name', 'S10'), ('Age', 'i4'),
               ('Height', 'f'), ('Children/Pets', 'i4', 2)])
s = np.array([('Smith', 45, 1.83, (0, 1)),
              ('Jones', 53, 1.72, (2, 2))], dtype=dt)
s

s['Name']
s['Height'].mean()
s[1]['Age']

####向量化编程####
r = np.random.standard_normal((4, 3))
s = np.random.standard_normal((4, 3))
r + s
2 * r + 3

s = np.random.standard_normal(3)
r + s

np.shape(r.T)

def f(x):
    return 3 * x + 5
    
f(0.5)
f(r)

np.sin(r)
np.sin(np.pi)

x = np.random.standard_normal((5, 10000000))
y = 2 * x + 3  # linear equation y = a * x + b
C = np.array((x, y), order='C')
F = np.array((x, y), order='F')
x = 0.0; y = 0.0 


C[:2].round(2)
get_ipython().magic('timeit C.sum()')
get_ipython().magic('timeit F.sum()')
get_ipython().magic('timeit C[0].sum(axis=0)')
get_ipython().magic('timeit C[0].sum(axis=1)')
get_ipython().magic('timeit F.sum(axis=0)')
get_ipython().magic('timeit F.sum(axis=1)')

F = 0.0; C = 0.0 


####numpy金融函数####
#终值
import numpy as np
from matplotlib.pyplot import plot, show

print "Future value", np.fv(0.03/4, 5 * 4, -10, -1000)

fvals = []

for i in xrange(1, 10):
   fvals.append(np.fv(.03/4, i * 4, -10, -1000))

plot(fvals, 'bo')
show()

#现值
print "Present value", np.pv(0.03/4, 5 * 4, -10, 1376.09633204)

#净现值
cashflows = np.random.randint(100, size=5)
cashflows = np.insert(cashflows, 0, -100)
print "Cashflows", cashflows

print "Net present value", np.npv(0.03, cashflows)

#内部收益率irr
print "Internal rate of return", np.irr([-100, 38, 48, 90, 17, 36])

print "Modified internal rate of return", np.mirr([-100, 38, 48, 90, 17, 36], 0.03, 0.03)

#分期付款
print "Payment", np.pmt(0.01/12, 12 * 30, 10000000) 

#付款期数
print "Number of payments", np.nper(0.10/12, -100, 9000)

#利率
print "Interest rate", 12 * np.rate(167, -100, 9000, 0)

#