import pandas as pd
from pandas import ExcelWriter
import xml.etree.ElementTree as ET
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

def parser(directory, filename):

	poleSheets = []
	poleCols = []
	poleText = []

	guid = []

	file = open(directory, 'r+')
	file.seek(0)
	file.close()

	tree = ET.parse(rootdir + '\\' + filename)
	root = tree.getroot()

	name = "Description"
	value = root.find('.//ATTRIBUTES/VALUE[@NAME="{}"]'.format(name)).text
	
	insAttrib = []
	insText = []
	

	for Insulator in root.findall('.//Insulator//'):
		insAttrib.append(Insulator.attrib)
		insText.append(Insulator.text)
		print(Insulator.text)
	print(insText)
	
	


	df = pd.DataFrame(insAttrib)
	se = pd.Series(insText)
	df['Text'] = se.values
	writer = ExcelWriter(path=workbooks	+ '\\' + filename.split('.')[0] + '.xlsx')
	df.to_excel(writer, index=False)
	writer.save()

	# for i in root.iter():

		# if 'NAME' in i.attrib.keys():
		# 	poleCols.append(i.attrib['NAME'])
		# 	poleText.append(i.text)
		# 	if i.attrib['NAME'] == 'Guid':
		# 		guid.append(i.text)

	# df = pd.DataFrame([poleText], columns = poleCols)
	# df1 = pd.DataFrame(guid, columns=['Guid'])

	# writer = ExcelWriter(path=workbooks	+ '\\' + filename.split('.')[0] + '.xlsx')
	# df.to_excel(writer,'main')
	# df1.to_excel(writer, 'guid')
	# writer.save()

print("Enter the directory to recurse:", end='', flush=True)
rootdir = input()
workbooks = rootdir + '\\Workbooks'
if not os.path.exists(workbooks):
	os.makedirs(workbooks)




for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		if file.endswith('.pplx'):
			parser(os.path.join(subdir,file), file)

