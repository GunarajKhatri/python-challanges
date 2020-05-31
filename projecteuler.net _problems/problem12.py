#What is the value of the first triangle number to have over five hundred divisors
#If u are unknown about triangle no. the ,Go here:- projecteuler.net/problem=12
def numdivisors(triangle):
	factors=0
	for i in range(1,int((triangle ** 0.5))+1):
		if triangle%i==0:
			factors+=1
	return factors * 2

def maxtraingledivisors(max):
	i=1
	triangle=0
	while i>0:
		triangle+=i
		print(triangle)
		if numdivisors(triangle)>= max:
			print(triangle)
			return triangle
		i+=1

maxtraingledivisors(5)