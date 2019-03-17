import pandas as pd 
from pandas import read_csv
import pprint

pp = pprint.PrettyPrinter(indent=4)

df = read_csv(r"UPDATE.csv")
df = df['proposed_att_height']

pp.pprint(df)

height = df.to_string(index=False, na_rep='')


height2 = height.split('\n')

for (i, j) in enumerate(height2):
	if j.endswith("'"):
		height2[i] = j + '0"'



out = []
for i in height2:
	out.append(i)

output = pd.DataFrame(out)

output.to_csv('output.csv', index=False)

