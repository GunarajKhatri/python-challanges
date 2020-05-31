#what is the largest prime factor of 600851475143
import math
array=[]

for i in range(1,600851475143):
	if i > 1:
		for num in range(2,i):
			if i%num==0:
				break
		else:
			if(600851475143%i==0):
				array.append(i)
print(max(array))