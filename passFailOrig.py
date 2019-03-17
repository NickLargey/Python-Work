import os
import re


print("Enter the directory to recurse:", end='', flush=True)
rootdir = input()
failPoles = open(rootdir + '\\failPoles.txt', 'w')

def pass_fail(directory, fname):
	fname = open(directory, "r+")
	lines = fname.readlines()
	
	fname.seek(0)
	for line in lines:
		if "<VALUE NAME=\"PercentAtMCU\" TYPE=\"String\">" in line:
			line = [float(s) for s in re.findall(r'-?\d+\.?\d*', line)]
			try:
				line = float(line[0])
				if line < 100.00:
					fname = str(fname).split('\\')
					fname = fname[-1].split("'")
					print(fname[0], 'Pass')
				else:
					fname = str(fname).split('\\')
					fname = fname[-1].split("'")
					print(fname[0], 'Fail')
					failPoles.writelines(str(fname[0]) + ' ' + str(line) + ' failed' +'\n')

			except IndexError:
				pass
			except TypeError:
				pass


for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		if file.endswith('.pplx'):
			pass_fail(os.path.join(subdir,file), file)

failPoles.close()