#Find the differences between the sum of squares of  first one hundred natural numbers and the square of sum.
def difference(n):
	sum_of_squares=(n*(n+1)*(2*n+1))/6
	square_of_sum=(n*(n+1)/2)*(n*(n+1)/2)
	return int(square_of_sum-sum_of_squares)

print(difference(100))