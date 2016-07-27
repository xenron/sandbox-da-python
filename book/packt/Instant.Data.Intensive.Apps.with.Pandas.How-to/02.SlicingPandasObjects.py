
dim = (10, 3)
df = DataFrame(np.random.normal(0, 1, dim), columns ['one', 'two', 'three'])

print df['one'][:2]

print df[['one', 'two']][:2]

print df[['one', 'two']][-3:-2]

print df[::5]
print df.head(2)
