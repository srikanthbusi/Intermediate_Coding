# n = int(input("Enter the number: "))
# rev = 0
# temp = n
# while n >0:
#     rem = n%10
#     rev = rev*10 + rem
#     n = n//10
# if temp == rev:
#     print(f"{temp} is an Palindrome number!!")
# else:
#     print("Nahi")



num = 1234
len = 0 
while num >0:
    print(num)
    num //=10
    len+=1
print(len)
