# num = int(input("Enter an number: "))
# len = 0 
# arm = 0
# temp = num
# new_temp = temp
# while temp > 0:
#     temp //=10
#     len+=1
# while num > 0:
#     # print(num)
#     rem = num %10
#     arm += rem**len
#     num//=10
# if new_temp == arm:
#     print(f"{new_temp} is an armstrong number")
# else:
#     print("It is not an Armstrong number")
# print(arm)


numbers = list(map(int,input("Enter the two numbers")).split())
n = int(input("Enter the number: "))
temp = n
arm = 0
power = len(str(n))
print(power)
while n > 0:
    rem = n%10
    arm += pow(rem,power) 
    n//=10
if temp == arm:
     print(f"{temp} is an armstrong number")
else:
    print("It is not an Armstrong number")
print(arm)


# def armstrong(num,len):
#     temp = num
#     sum = 0
#     while temp>0:
#         rem = temp%10
#         sum += rem**len
#         temp //= 10
#     return num  == sum
# def order(num):
#     return len(str(num))

# num = int(input("enter a number: "))
# len = order(num)
# if armstrong(num,len):
#     print(f"Given {num} is an armstrong number!")
# else:
#     print(f"Given {num} is not an armstrong number!")



