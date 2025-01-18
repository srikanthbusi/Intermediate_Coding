
from math import sqrt

def isprime(n):
    # 0 and 1 are not prime numbers
    # negative numbers are not prime
    if n <= 1:
        return False
    # special case as 2 is the only even number that is prime
    elif n == 2:
        return True
    # Check if n is a multiple of 2, thus all these won't be prime
    elif n % 2 == 0:
        return False
    # If not, then just check the odds
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
n = list(map(int,input("Enter the range of numbers yto insert: ").split()))
n1 = n[0]
n2 = n[1]

for i in range(n1,n2+1):
    if isprime(i):
        print(i, end= " ")
