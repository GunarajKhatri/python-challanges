#Find the largest palindrome made from product of two 3-digit numbers
def ispalindrome(n):
 	return str(n) == str(n)[::-1]
listofpalindrome=[]
for first_term in range(100,1000):
	for second_term in range(100,1000):
		num = first_term*second_term
		if ispalindrome(num)==1:
			listofpalindrome.append(num)
print(max(listofpalindrome))