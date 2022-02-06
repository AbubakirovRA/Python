# Составить список простых множителей натурального числа N
# https://www.pythonpool.com/prime-factorization-python/

import math

def prime_factors(num):
    for i in range(2, num + 1):
        if num % i == 0:
            count = 1
            h = (i//2 + 1)
            for j in range(2, h):
                if i % j == 0:
                    count = 0
                    break
            if count == 1:
                print(i)

num = int(input("Enter the number for calculating the prime factors :\n"))
prime_factors(num)
