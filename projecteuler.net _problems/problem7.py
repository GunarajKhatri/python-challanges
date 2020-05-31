#What is the 10001st prime number ?
count = 1
i = 2
array=[]
while count!= 10002:
	for k in range(2,i):
		if i%k==0:
			break
	else:
		array.append(i)
		count+=1
	i+=1
print(array[10000])