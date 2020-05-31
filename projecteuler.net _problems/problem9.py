#There exist only one pythagorean triplet for which a+b+c=1000.Find the product abc.
#a^2+b^2=c^2------(1)
#a+b+c=1000--------(2)
#1000*(500-b) % (1000-b)------(from (1) & (2))

array=[]
a=0
for b in range(1,500):
	if 1000*(500-b) % (1000-b) == 0:
		array.append(b)
for i in array:
	a=a+i
c=1000-a
array.append(c)
product=1
for i in array:
	product=product * i
print(product)
		