num1 = int(input("Enter the number: "))
num2 = int(input("Enter the second number: "))
small = num1 if num1>num2 else num2
for i in range(1,small+1):
    if num1%i==0 and num2%i == 0:
        print(i)
        break
