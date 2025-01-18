from math import sqrt
# """Method 1"""
# # n = int(input())
# # count = 0

# # for i in range(1,n+1):
# #     if n%1==0:
# #         count+=1
# # # if (n <2 or count >2):
# # #     print("NOT PRIME")
# # # else:
# # #     print("Prime")                 Complexity is O(N)
                                                                     
# # print("NOT PRIME " if n<2 or count>2 else "PRIME")


# """Method 2"""
# n = int(input())
# if n<2:
#     print("NOT Prime")
# for i in range(2,n):
#     if n%i==0:
#         print("Not Prime")
#         break
#     else:
#         print("Prime")
#         break

# """Method 3"""
# isprime = True
# n = 5

# if n < 2:
#     isprime = False
# else:
#     x = n // 2
#     for i in range(2, x + 1):
#         if n % i == 0:
#             isprime = False
#             break

# if isprime:
#     print("Number is a Prime Number")
# else:
#     print("Number is not a Prime Number")


# """Method 4"""
# n = int(input("Enter the number: "))
# isprime = True
# if n<2:
#     isprime= False
# elif n==2:
#     isprime = True
# else:
#     for i in range(3,int(sqrt(n))+1,2):
#         if n%i==0:
#             isprime = False
# res = "Prime" if isprime else "Not an prime"
# print(f"The given number i.e, {n} is Officailly "+res)

"""Method 5"""
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
n = int(input())
print(isprime(n))