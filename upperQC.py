import pandas as pd 
from pandas import read_csv
import pprint

pp = pprint.PrettyPrinter(indent=4)

df = read_csv(r"UPDATE.csv")

df['mr_desc1'] = df['mr_desc1'].fillna('').apply(lambda x: str(x).upper()) 
df['mr_desc2'] = df['mr_desc2'].fillna('').apply(lambda x: str(x).upper()) 
df['mr_desc3'] = df['mr_desc3'].fillna('').apply(lambda x: str(x).upper()) 
df['mr_desc4'] = df['mr_desc4'].fillna('').apply(lambda x: str(x).upper()) 
df['mr_desc5'] = df['mr_desc5'].fillna('').apply(lambda x: str(x).upper()) 

cols = ['mr_desc1','mr_desc2','mr_desc3','mr_desc4','mr_desc5']
df = df[cols]

pp.pprint(df.tail())

df.to_csv('upperOutput.csv')
