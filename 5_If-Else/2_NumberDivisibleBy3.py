"""
Program to check whether the number entered by the user 
is divisible by 3 or not
"""

num = int(input("Enter your Number: "))

remainder = num % 3

if remainder == 0:
    print("Number is Divisible by 3")
else:
    print("Number is not Divisible by 3")