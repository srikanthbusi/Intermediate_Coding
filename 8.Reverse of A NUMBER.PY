# num = 72365
# reverse = 0

# while num != 0:
#     rem = num % 10
#     reverse = reverse * 10 + rem
#     num //= 10

# print(reverse)

# while num!=0:
#     rem = num %10
#     rev = rev*10+rem
    
def reverse(n):
    if n<0:
        n = str(abs(n)) + "-"

    return int(str(n)[::-1])
n = int(input("Enter the number: "))
print(reverse(n))