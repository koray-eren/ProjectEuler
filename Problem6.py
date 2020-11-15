# sum of squares of first 10 natural numbers is 385: 1**2 + 2**2 + 3**2 ... 10**2 = 385
# square of the sum of first 10 natural numbers is 3025 sum of 1-10 = 55; 55**2 = 3025
# difference between the two is 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = 385
sum_101 = 55
for i in range(11,101):
    sum_101 += i
    sum_of_squares += (i**2)
square_of_sum = sum_101**2

difference = square_of_sum - sum_of_squares
print(difference)
    
