# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

success = False
smallest_multiple = 2520
while success == False:    
    for i in range(10, 21):
        if smallest_multiple % i != 0:
            smallest_multiple += 20
            break
        else:
            if i == 20:
                success = True
                print(smallest_multiple)
