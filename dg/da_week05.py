# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import sys
from pandas import Series, DataFrame


###pandas
#Series
obj = Series([4, 7, -5, 3])
obj

obj.values
obj.index

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2

obj2.index

obj2['a']

obj2['d'] = 6
obj2[['c', 'a', 'd']]

obj2[obj2 > 0]
obj2 * 2
np.exp(obj2)

'b' in obj2
'e' in obj2

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
obj3

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
obj4

pd.isnull(obj4)
pd.notnull(obj4)

obj4.isnull()

obj3
obj4
obj3 + obj4

obj4.name = 'population'
obj4.index.name = 'state'
obj4

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj

#dataframe
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)

frame

DataFrame(data, columns=['year', 'state', 'pop'])

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
frame2
frame2.columns

frame2['state']
frame2.year
frame2.ix['three']

frame2['debt'] = 16.5
frame2

frame2['debt'] = np.arange(5.)
frame2

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2

frame2['eastern'] = frame2.state == 'Ohio'
frame2
del frame2['eastern']
frame2.columns

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
frame3

frame3.T

DataFrame(pop, index=[2001, 2002, 2003])

pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
DataFrame(pdata)

frame3.index.name = 'year'; frame3.columns.name = 'state'
frame3
frame3.values
frame2.values

#索引对象
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
index

index[1:]

index[1] = 'd'

index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
obj2.index is index

frame3
'Ohio' in frame3.columns
2003 in frame3.index

###数据读取
#读取文本格式数据
df = pd.read_csv('d:data/ex1.csv')
df

pd.read_table('d:data/ex1.csv', sep=',')

pd.read_csv('d:data/ex2.csv', header=None)
pd.read_csv('d:data/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])

names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('d:data/ex2.csv', names=names, index_col='message')

parsed = pd.read_csv('d:data/csv_mindex.csv', index_col=['key1', 'key2'])
parsed

list(open('d:data/ex3.txt'))
result = pd.read_table('d:data/ex3.txt', sep='\s+')
result

pd.read_csv('d:data/ex4.csv', skiprows=[0, 2, 3])

result = pd.read_csv('d:data/ex5.csv')
result
pd.isnull(result)

result = pd.read_csv('d:data/ex5.csv', na_values=['NULL'])
result

sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('d:data/ex5.csv', na_values=sentinels)

#逐行读取文本文件
result = pd.read_csv('d:data/ex6.csv')
result
pd.read_csv('d:data/ex6.csv', nrows=5)
chunker = pd.read_csv('d:data/ex6.csv', chunksize=1000)
chunker

chunker = pd.read_csv('d:data/ex6.csv', chunksize=1000)

tot = Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.order(ascending=False)

tot[:10]

#文件写出
data = pd.read_csv('d:data/ex5.csv')
data
data.to_csv('d:data/out.csv')

data.to_csv(sys.stdout, sep='|')

data.to_csv(sys.stdout, na_rep='NULL')

data.to_csv(sys.stdout, index=False, header=False)

data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])

dates = pd.date_range('1/1/2000', periods=7)
ts = Series(np.arange(7), index=dates)
ts.to_csv('tseries.csv')

Series.from_csv('tseries.csv', parse_dates=True)

#手工处理分隔符格式
import csv
f = open('d:data/ex7.csv')

reader = csv.reader(f)

for line in reader:
    print(line)

lines = list(csv.reader(open('d:data/ex7.csv')))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
data_dict

class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL

with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))
pd.read_table('mydata.csv', sep=';')

#Excel数据
#生成xls工作薄
import xlrd, xlwt
path = 'd:data/'

wb = xlwt.Workbook()
wb

wb.add_sheet('first_sheet', cell_overwrite_ok=True)
wb.get_active_sheet()

ws_1 = wb.get_sheet(0)
ws_1

ws_2 = wb.add_sheet('second_sheet')

data = np.arange(1, 65).reshape((8, 8))
data

ws_1.write(0, 0, 100)

for c in range(data.shape[0]):
    for r in range(data.shape[1]):
        ws_1.write(r, c, data[c, r])
        ws_2.write(r, c, data[r, c])

wb.save(path + 'workbook.xls')

#生成xlsx工作薄

#从工作薄中读取
book = xlrd.open_workbook(path + 'workbook.xls')
book

book.sheet_names()

sheet_1 = book.sheet_by_name('first_sheet')
sheet_2 = book.sheet_by_index(1)
sheet_1
sheet_2.name

sheet_1.ncols, sheet_1.nrows

cl = sheet_1.cell(0, 0)
cl.value

cl.ctype

sheet_2.row(3)

sheet_2.col(3)

sheet_1.col_values(3, start_rowx=3, end_rowx=7)

sheet_1.row_values(3, start_colx=3, end_colx=7)

for c in range(sheet_1.ncols):
    for r in range(sheet_1.nrows):
        print '%i' % sheet_1.cell(r, c).value,
    print

#使用pandas读取
xls_file=pd.ExcelFile(path + 'workbook.xls')
table=xls_file.parse('first_sheet')


#JSON数据

obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
              {"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""

import json
result = json.loads(obj)
result

asjson = json.dumps(result)

siblings = DataFrame(result['siblings'], columns=['name', 'age'])
siblings


#二进制数据格式
#pickle
frame = pd.read_csv('d:data/ex1.csv')
frame
frame.to_pickle('d:data/frame_pickle')

pd.read_pickle('d:data/frame_pickle')

#HDF5格式
store = pd.HDFStore('mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame['a']
store

store['obj1']

store.close()
os.remove('mydata.h5')

#使用HTML和Web API
import requests
url = 'https://api.github.com/repos/pydata/pandas/milestones/28/labels'
resp = requests.get(url)
resp

data=json.loads(resp.text)

issue_labels = DataFrame(data)
issue_labels


#使用数据库
import sqlite3

query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
);"""

con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()

cursor = con.execute('select * from test')
rows = cursor.fetchall()
rows

cursor.description

DataFrame(rows, columns=zip(*cursor.description)[0])

import pandas.io.sql as sql
sql.read_sql('select * from test', con)
