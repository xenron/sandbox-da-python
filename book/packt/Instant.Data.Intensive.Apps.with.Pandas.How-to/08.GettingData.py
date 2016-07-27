import pandas as pd

url = 'http://s3.amazonaws.com/trenthauck-public/book_data.csv'
df = pd.read_csv(url)

print df
