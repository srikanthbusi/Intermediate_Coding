# def armstrong(f, s):
#     for i in range(f, s + 1):  # Loop through the given range
#         power = len(str(i))
#         temp = i
#         arm_sum = 0  # Reset sum for each number
        
#         while temp > 0:
#             rem = temp % 10
#             arm_sum += rem ** power
#             temp //= 10
        
#         if i == arm_sum:  # Check if it's an Armstrong number
#             print(i, end=" ")

# # Taking input
# numbers = list(map(int, input("Enter the required numbers: ").split()))
# f = numbers[0]
# s = numbers[1]

# print(f"Armstrong numbers between {f} and {s}:")
# armstrong(f, s)  # Call function to print Armstrong numbers



# Function to calculate the number of digits in a number
def order(num):
    len = 0
    while num:
        len += 1
        num = num // 10
    return len

# Function to find and print Armstrong numbers in a given range
def armstrong(low, high):
    count = 0
    for num in range(low, high + 1):
        sum = 0
        temp, digit, len = num, 0, 0
        len = order(num)
        
        temp = num
        while temp != 0:
            digit = temp % 10
            sum += digit ** len
            temp //= 10
        
        if sum == num:
            print(num, end=' ')
            count += 1
    
    if count == 0:
        print("Given Range does not have any Armstrong numbers.")

# Main function
if __name__ == "__main__":
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the high bound: "))
    
    print(f"Armstrong numbers between {low} and {high} are: ", end='')
    armstrong(low, high)