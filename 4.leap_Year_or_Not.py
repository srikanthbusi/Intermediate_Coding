num = int(input("Enter an leap year: "))
# if num%400==0:
#     print("It is an Leap year!!!!")
# elif num%4==0 and num%100!=0:
#     print("It is an leap year!")
# else:
#     print("Not an leap year")


print("Leap year " if num%400 ==0 or (num%4==0 and num%100!=0) else "Not an leap Year")

year = 2000

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
