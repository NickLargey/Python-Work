import os
import pandas as pd 
import numpy as np


data = []

def scrapePPLX(directory, filename):
	fname = open(directory, "r+")
	lines = fname.readlines()
	fname.close()

	if '_' in filename:
		polename = filename.split("_")[0]
	else:
		polename = filename.split(".")[0]

	for line in lines:
		if "<VALUE NAME=\"Latitude\" TYPE=\"Double\">" in line:
			lat = line.split(">")[1].split("<")[0]
		elif "<VALUE NAME=\"Longitude\" TYPE=\"Double\">" in line:	
			lon = line.split(">")[1].split("<")[0]
			
	data.append([polename,lat, lon])

def main():
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			if file.endswith('.pplx'):
				scrapePPLX(os.path.join(subdir,file), file)

	cols=['id', 'Latitude','Longitude']
	PPLXdf = pd.DataFrame(data)
	PPLXdf.columns = cols
	PPLXdf['latLong'] = PPLXdf['Latitude'].map(float).round(4).map(str) + ' ' + PPLXdf['Longitude'].map(float).round(4).map(str)
	PPLXdf.to_csv('PPLXcsv.csv',index=False)

	cols = ['id', '_latitude', '_longitude', '_record_id']
	readCSV = pd.read_csv(pdc)
	df = readCSV[cols]
	df['latLong'] = df['_latitude'].map(float).round(4).map(str) + ' ' + df['_longitude'].map(float).round(4).map(str)
	df.to_csv('newPDC.csv', index=False)

	compare(PPLXdf, df)

def compare(PPLXdf, df):

	# PPLXdf['Latitude'] = PPLXdf['Latitude'].astype(float)
	# PPLXdf['Longitude'] = PPLXdf['Longitude'].astype(float)

	# df['_latitude'] = df['_latitude'].astype(float)
	# df['_longitude'] = df['_longitude'].astype(float)

	# PPLXdf['latLong'] = PPLXdf['Latitude'].map(float) + PPLXdf['Longitude'].map(float)

	# PPLXdf.set_index()
	# masterdf = PPLXdf.merge(df, left_on=['Latitude', 'Longitude'], right_on=['_latitude', '_longitude'])
	# masterdf = pd.merge(PPLXdf, df, how='left', left_on=['Latitude', 'Longitude'], right_on=['_latitude', '_longitude'])
	
	masterdf = pd.merge(PPLXdf, df, how='left', on=['latLong'])
	
	masterdf.drop(['Latitude','Longitude'],axis=1,inplace=True)
	masterdf.to_csv('Master.csv', index=False)


print("Enter the directory to recurse: ", end='', flush=True)
rootdir = input()

print("Enter name of the PDC: ", end='', flush=True)
pdc = rootdir + "\\" + input()


if __name__ == '__main__':
    main()
