import random 
import string

def idGen(id):
	a = ''.join(random.choice('0123456789abcdef') for _ in range(8))
	b = ''.join(random.choice('0123456789abcdef') for _ in range(4))
	c = ''.join(random.choice('0123456789abcdef') for _ in range(4))
	d = ''.join(random.choice('0123456789abcdef') for _ in range(4))
	e = ''.join(random.choice('0123456789abcdef') for _ in range(12))

	return a +'-'+ b +'-'+ c +'-'+ d +'-'+ e
	
	return id 



