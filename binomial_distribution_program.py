#CSE 3300 Homework 1 Binomial Distribution program

import math

def bin_distr(n, i, p):
    #p is the porbability
    #P is the probability of i successes

    P = (math.factorial(n) / (math.factorial(n-i)* math.factorial(i))) * (p**i) * (1-p)**(n-i)

    print(P)

# def fact(n):
#     if (n <= 1):
#         return n
#     else:
#         n = n * fact(n-1)

bin_distr(50, 10, 0.2)
