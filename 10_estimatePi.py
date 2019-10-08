# This problem was asked by Google.

# The area of a circle is defined as (pi)r^2. Estimate (pi) to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x^2 + y^2 = r^2.
import random
import math

def estimatePi(tries):
    inCircle = 0
    for i in range(tries):
        x = random.random()
        y = random.random()
        if(math.sqrt(x**2 + y**2) <= 1):
            inCircle += 1
    return float(inCircle/tries) * 4

print(estimatePi(10000))
