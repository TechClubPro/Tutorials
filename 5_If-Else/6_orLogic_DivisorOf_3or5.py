"""
Program to use Logic Operator 'or'

Create an application which checks whether

the number entered is divisible by 3 or 5
"""


num = int(input("Enter the Number: "))

if num % 3==0 or num % 5==0:
    print("The number is divisible by 3 or 5")
else:
    print("The number is not divisible by 3 or 5")
    
