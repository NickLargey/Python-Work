import os
import csv
import re
from math import pi


def tag(directory, filename):
	file = open(directory, "r+")

	if '_' in filename:
		polename = filename.split("_")[0]
	else:
		polename = filename.split(".")[0]

	poletag = ''
	polelon = polelat = '0.0'
	polerad = '0'
	poleglc = '0'
	
	for row in reader:
		if polename in row[pnindex]:
			print(row[pnindex])
			poletag = row[ptindex]
			print(poletag)
			polelat = repr(round(float(row[latindex]), 6))
			print(polelat)
			polelon = repr(round(float(row[lonindex]), 6)) 
			print(polelon)
			if row[pnindex] == polename and polerad == '0':
				print(row)
				poleglc = row[glcindex]
				if poleglc == '':
					print("glc field empty")
					break
			print("circ:" + poleglc)
			polerad = repr(round(float(poleglc) / (2 * pi), 14))
			print("radi:" + polerad)
	csvfile.seek(0)

	pole = polename.split("-")[2]
	print(pole)

	glmline = "          <VALUE NAME=\"GLCircumMethod\" TYPE=\"String\">Measured</VALUE>" + "\n"
	radline = "          <VALUE NAME=\"MeasuredRadiusGL\" TYPE=\"Double\">" + polerad + "</VALUE>" + "\n"
	
	if re.match(r"^\w+$",poletag) is None:
		poletag = "NT"
	print(poletag)

	ptline = "          <VALUE NAME=\"Pole Number\" TYPE=\"String\">" + pole + ' - EID ' + poletag.upper() + "</VALUE>" + "\n"
	latline = "      <VALUE NAME=\"Latitude\" TYPE=\"Double\">" + polelat + "</VALUE>" + "\n"
	lonline = "      <VALUE NAME=\"Longitude\" TYPE=\"Double\">" + polelon + "</VALUE>" + "\n"

	lines = file.readlines()
	
	file.seek(0)
	
	for line in lines:
		if "<VALUE NAME=\"Pole Number\" TYPE=\"String\">" in line:
			file.write(ptline)
			print(line)
			print("writing poletag")
		elif "<VALUE NAME=\"Latitude\" TYPE=\"Double\">" in line:
			file.write(latline)
			print(line)
			print("writing latitude")
		elif "<VALUE NAME=\"Longitude\" TYPE=\"Double\">" in line:
			file.write(lonline)
			print(line)
			print("writing longitude")
		elif "<VALUE NAME=\"GLCircumMethod\" TYPE=\"String\">" in line and polerad != '0':
			file.write(glmline)
			print(line)
			print("writing measured")
		elif "<VALUE NAME=\"MeasuredRadiusGL\" TYPE=\"Double\">" in line and polerad != '0':
			file.write(radline)
			print(line)
			print("writing radius")
		elif "<VALUE NAME=\"Owner\" TYPE=\"String\">DWP</VALUE>" in line:
			file.write("<VALUE NAME=\"Owner\" TYPE=\"String\">PGE</VALUE>")
		else:
			file.write(line)
	
	file.truncate()
	file.close()

print("Enter the directory to recurse:", end='', flush=True)
rootdir = input()
print('Enter the name of the mre csv:')
pdcsv = rootdir + '\\' + input()

csvfile = open(pdcsv, "r", newline='')
reader = csv.reader(csvfile)
header = next(reader)

try:
	pnindex = header.index("_title")
except ValueError:
	pass
try:
	pnindex = header.index("id")
except ValueError:
	print("ValueError: _title/id index not found in csv")
ptindex = header.index("pole_tag_1")
latindex = header.index("_latitude")
lonindex = header.index("_longitude")
glcindex = header.index("circumference_in_inches")


for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		if file.endswith('.pplx'):
			tag(os.path.join(subdir,file), file)