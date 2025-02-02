from math import sqrt
# num = int(input("Enter a number: "))
# for i in range(2,int(sqrt(num))+1):     
#     while num%i==0:                    
#         print(i,end=" ")               
#         num//=i
# if num>2:
#     print(num)
    
# 12 = 2: 12%2==0: 12//2==6; 6%2==0:6//2==3"""
#  """ 3  = 3: 3%3 ==0: 3//3==1; num =1   """
#  """     21 = 3 : 21%3==0: 21//3 ==7"""
def primefact(num):
    while num%2==0:
        print(2,end=" ")
        num//=2
    for i in range(3,int(sqrt(num))+1,2):
        while num%i==0:
            print(i,end=" ")
            num//=i
        if num>2:
            print(num)
num = int(input("Enter a  number: "))
primefact(num)