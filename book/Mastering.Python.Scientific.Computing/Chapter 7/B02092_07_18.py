import numpy as np
randn = np.random.randn
from pandas import *

user_columns = ['User-ID', 'Location', 'Age']
users = read_csv('c:\BX-Users.csv', sep=';', names=user_columns)

rating_columns = ['User-ID', 'ISBN', 'Rating']
ratings = read_csv('c:\BX-Book-Ratings.csv', sep=';', names=rating_columns)

book_columns = ['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-S']
books = read_csv('c:\BX-Books.csv', sep=';', names=book_columns, usecols=range(6))

books

books.dtypes

users.describe()

print books.head(10)
print books.tail(8)
print books[5:10]

users['Location'].head()
print users[['Age', 'Location']].head()

desired_columns = ['User-ID', 'Age'] 
print users[desired_columns].head()

print users[users.Age > 25].head(4)
print users[(users.Age < 50) & (users.Location == 'chicago, illinois, usa')].head(4)

print users.set_index('User-ID').head()
print users.head()

with_new_index = users.set_index('User-ID')
print with_new_index.head()
users.set_index('User_ID', inplace=True)
print users.head()

print users.ix[62]
print users.ix[[1, 100, 200]]
users.reset_index(inplace=True)
print users.head()