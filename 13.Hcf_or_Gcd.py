# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the second number: "))
# hcf = 1
# small = num1 if num1>num2 else num2
# for i in range(1,small+1):
#     if num1%i==0 and num2%i == 0:
#         hcf = i
# print(f"The HCF for {num1} and {num2} is: ",hcf)



# Method 2:-
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the second number: "))
# hcf = 1
while num1!=num2:
    if num1>num2:
        num1-=num2
    else:
        num2-=num1
print(num1)

