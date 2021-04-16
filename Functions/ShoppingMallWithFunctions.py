
"""
Shopping Mall App

Item List & Their discounts:
    1.Soaps & Sanitizer(30/-) : 5% 
    2.Grains(100/-): 10%
    3.Biscuits & Cookies(25/-) : 15%
    4.Sauces(80/-) : 8%
    5.Snacks(60/-): 12%
    6.T-Shirts(500/-): 20%
    7.Tops(700/-):25%
    8.Kitchenware(350/-) : 30%
"""
#Display Menu to user
print("1.Soaps & Sanitizer(30/-) : 5% ")
print("2.Grains(100/-): 10% ")
print("3.Biscuits & Cookies(25/-) : 15% ")
print("4.Sauces(80/-) : 8%")
print("5.Snacks(60/-): 12%")
print("6.T-Shirts(500/-): 20% ")
print("7.Tops(700/-):25%")
print("8.Kitchenware(350/-) : 30% ")

#Ask user to purchase item
Item=int(input("Select the item to be purchased: "))

#Ask the user the Qty
Qty=int(input("Enter the Qty for the item"))


def CalculateDiscount(Qty,UnitPrice,DiscountPercent):
    Amount= Qty * UnitPrice 
    Discount= (Amount * DiscountPercent)/100
    Total=Amount-Discount
    
    print("Your Bill with " +str(DiscountPercent)+"% discount is: "+str(Total))
    

#Compare Items & Calculate the discount

if Item==1: 
    CalculateDiscount(Qty,30,5)
   
if Item==2: 
    CalculateDiscount(Qty,100,10)  
if Item==3:
   CalculateDiscount(Qty,25,15)
     
if Item==4: 
    CalculateDiscount(Qty,80,8)
   
  


