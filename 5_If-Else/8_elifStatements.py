"""
Program to introduce the 'elif'  statements

Program to find whether price enetred by the user is High, Medium or Low.

        Price Range
High : >1000
Medium : >500
Low: <500 
"""

price = int(input("Your Price: "))

if price>1000:
    print("High Range")
elif price>500:
    print("Medium Range")
elif price<500 :
    print("Low Range")