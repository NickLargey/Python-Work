import os

def setCommOwner(directory, filename):

	file = open(directory, "r+")	
	if '_' in filename:
		polename = filename.split("_")[0]
	else:
		polename = filename.split(".")[0]
	
	lines = file.readlines()
	file.seek(0)
	flag = 0
	ownerSet = 0
	commOwner = ''
	
	try:
		for line in lines:
			if "<Insulator>" in line:
				flag = 1	
			elif "</Insulator>" in line:
				flag = 0
				ownerSet = 0	
			if flag and not ownerSet and "Owner" in line:
				ownerSet = 1
				commOwner = line.split('>')[1].split('<')[0]
				if commOwner == "TELCO" or commOwner =="CATV"  or commOwner == "FIBER":
					print(filename, commOwner)
			if flag and ownerSet and 'Owner' in line and "MCI" not in line and "PROPOSED" not in line:
				file.write('<VALUE NAME="Owner" TYPE="String">' + str(commOwner) + '</VALUE>' +'\n')
			else:
				file.write(line)
	except Exception as e:
		print(e)
	
	
	file.truncate()
	file.close()

print("Enter the directory to recurse:", end='', flush=True)
rootdir = input()


for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		if file.endswith('.pplx'):
			setCommOwner(os.path.join(subdir,file), file)	
