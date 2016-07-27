import numpy as np
randn = np.random.randn
from pandas import *

user_columns = ['User-ID', 'Location', 'Age']
users = read_csv('c:\BX-Users.csv', sep=';', names=user_columns)

rating_columns = ['User-ID', 'ISBN', 'Rating']
ratings = read_csv('c:\BX-Book-Ratings.csv', sep=';', names=rating_columns)

book_columns = ['ISBN', 'Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-S']
books = read_csv('c:\BX-Books.csv', sep=';', names=book_columns, usecols=range(6))

# create one merged DataFrame
book_ratings = merge(books, ratings)
users_ratings = merge(book_ratings, users)

most_rated = users_ratings.groupby('Title').size().order(ascending=False)[:25]
print most_rated

users_ratings.Title.value_counts()[:17]

book_stats = users_ratings.groupby('Title').agg({'Rating': [np.size, np.mean]})
print book_stats.head()

# sort by rating average
print book_stats.sort([('Rating', 'mean')], ascending=False).head()

greater_than_100 = book_stats['Rating'].size >= 100
print book_stats[greater_than_100].sort([('Rating', 'mean')], ascending=False)[:15]

top_fifty = users_ratings.groupby('ISBN').size().order(ascending=False)[:50]