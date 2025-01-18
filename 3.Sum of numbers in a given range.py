a = int(input("Enter a first number: "))
b = int(input("Enter the second number: "))
# sum = 0
# for i in range(a,b+1):
#     sum +=i                          Complexity is O(N)
# print(sum)                

print(((b*(b+1)//2)-a*(a+1)//2)+a)

# sum = b * (b + 1) // 2 - a * (a + 1) // 2 + a  """complexity is O(1)"""
print(sum)