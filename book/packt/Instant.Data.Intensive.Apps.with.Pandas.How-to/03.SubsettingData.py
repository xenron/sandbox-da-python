import pandas as pd
import numpy as np

d = {'Cost': np.random.normal(100, 5, 100),
     'Profit': np.random.normal(50, 5, 100),
     'CatA': np.random.choice(['a', 'b', 'c'], 100),
     'CatB': np.random.choice(['e', 'f', 'g'], 100)}

df = pd.DataFrame(d)

print df[df.CatA == 'a'][:5]

mask = np.logical_and(df.CatA=='a', df.CatB=='e')
df[mask][:5]
a_e = ['a', 'e']
CatA_a_e = df[df.CatA.isin(a_e)]
print CatA_a_e

only_a_e = CatA_a_e[CatA_a_e.CatB.isin(a_e)]

print only_a_e[:5]
