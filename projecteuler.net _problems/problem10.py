#Find the sum of all the primes below two million.
sum=0
for i in range(1,2000000):
	if i>1:
		for j in range(2,i):
			if i%j==0: 
				break
		else:
			sum=sum+i
print(sum)