"""
Program to check 
whether the number entered by the user is greater than 100 
"""

price = int(input("Enter the Price of a Product: "))

#Compare the Price 
#check whether Price > 100

if price > 100:
    print("Your product is costly")
    print(price)
    diff = price -100
    print("The Difference in price is : " + str(diff))
    
else:
    print("I am buying the product!!")
    print("Price is in my budget")