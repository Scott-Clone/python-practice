

import pandas as pd
df = pd.read_csv('/Users/carlonescott/downloads/winequality-red.csv', sep=';')
df.head()

labels = list(df.columns)
for i in labels:
	labels[i] = labels[i].replace(' ', '_')

df.columns = labels

df.head()

 
