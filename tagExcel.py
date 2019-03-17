import os
import csv
import re
import pandas as pd
from math import pi


pt = []
ad = []

def tag(directory, filename):
	file = open(directory, "r+")

	if '_' in filename:
		polename = filename.split("_")[0]
	else:
		polename = filename.split(".")[0]

	pole = polename.split("-")[2]
	print(pole)

	lines = file.readlines()
	
	file.seek(0)
	
	for line in lines:
		if "<VALUE NAME=\"Pole Number\" TYPE=\"String\">" in line:
			l2 = line.split('>')[1].split('<')[0]
			pt.append(l2)
			# print(l3)
		elif "          <VALUE NAME=\"Aux Data 1\" TYPE=\"String\">" in line:
			l2 = line.split('>')[1]l3 = l2.split('<')[0]
			ad.append(l2)
			# print(l3)
	
	file.close()
	
	df = pd.DataFrame(pt, columns=['Pole Tag'])
	df.to_csv('output.csv', index=False)

print("Enter the directory to recurse:", end='', flush=True)
rootdir = input()


for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		if file.endswith('.pplx'):
			tag(os.path.join(subdir,file), file)

