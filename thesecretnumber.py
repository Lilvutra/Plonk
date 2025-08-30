#codeforces: The secret number

"""
Vadim has thought of a number x
To ensure that no one can guess it, he appended a positive number of zeros to the right of it, thus obtaining a new number y
However, as a precaution, Vadim decided to spread the number n = x+y
Find all suitable x
that Vadim could have 
thought of for the given n

"""

import sys 
import math 


lines = sys.stdin.read().splitlines()
t = int(lines[0]) #number of test cases, n=55

for i in range(t):
    n = int(lines[i])
    suitable_x = []
    for x in range(1, n):
        y = n - x
        if y % 10 == 0:
            suitable_x.append(x)

print(" ".join(map(str, suitable_x)))
















