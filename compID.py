import pandas as pd 
from pandas import read_csv
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Loads CSV
df_ex1 = read_csv(r"sorted.csv")
df_ex2 = read_csv(r"UPDATE.csv")

# Checks columns against eachother and strips non-matches
df_final = df_ex1[df_ex1['id'].isin(df_ex2['id'])]

# Strips poles without proposed heights
df_final = df_ex2[df_ex2['proposed_att_height'].isnull()==False]

# Outputs to new CSV file
df_final.to_csv('finalATL.csv')

# Creates a list of non-matched rows to print
not_in_file = df_ex1[~df_ex1['id'].isin(df_ex2['id'])]
# Totals non-matched rows
quan = len(not_in_file)


pp.pprint(not_in_file['id'])
print(quan)
