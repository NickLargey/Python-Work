import random

height = input()
sd = float(input())

def frange():
	y = [float(x) / 10000.0 for x in range(970, 1030, 1)]
	return y


def heightsList():
	htLst = []
	lst = frange()
	for j in lst:
		htLst.append(float(j)*float(height) + 2.0)
	
	return htLst



def main():
	x = frange()
	hiLst = heightsList()
	global height
	global sd
	add = random.choice(x)
	data = [round(elem, 2) for elem in hiLst]
	print(data)
	if sd in data:
		print('Correct height')
	else:
		sd = (float(height)*float(add)) + 2
		print('correct height is ' + str(sd))

if __name__ == '__main__':
		main()

 
