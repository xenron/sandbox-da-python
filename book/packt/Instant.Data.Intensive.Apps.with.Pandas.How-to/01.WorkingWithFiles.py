import pandas as pd #standard convention throughout the book
import numpy as np

#Create a simple DataFrame
my_df = pd.DataFrame([1,2,3])
print my_df

cols = ['A', 'B']
idx = pd.Index(list('name'), name='a')
data = np.random.normal(10, 1, (4, 2))
df = pd.DataFrame(data, columns=cols, index=idx)

print df

print df.A

pan = pd.Panel({'df1': df, 'df2': df})
print pan


df.to_csv('df.csv')
df.to_latex('df.tex') #useful with Pweave
df.to_excel('df.xlsx') #requires extra packages
df.to_html('df.html')
print df.to_string()


pd.read_csv('df.csv')

with open('df.json', 'w') as f:
    json.dump(df.to_dict(),to_dict f)

with open(‘df.json’) as f:
    df_json = json.load(f)
