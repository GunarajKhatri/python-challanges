#By considering terms in Fibonacci sequence whose value do not exceed four million,find the sum of even-valued terms

first_term=0
second_term=1
total_sum=0
for i in range(1,11):
	third_term=first_term+second_term
	first_term=second_term
	second_term=third_term
	if(third_term<4000000 and third_term%2==0):
		total_sum+=third_term

print(total_sum)