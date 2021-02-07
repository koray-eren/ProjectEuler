import math

for c in range(335,997):
    lowerLimit = (1000-c)/2
    for b in range(math.floor(lowerLimit) + 1, 499 ):
        a = 1000 - b - c
        if a > 0:
            if (a**2) + (b**2) == (c**2):
                print("success!")
                print("a: " + str(a))
                print("b: " + str(b))
                print("c: " + str(c))

print("a x b x c = " + str(a*b*c))
