"""
Use of While Loops.

Calculate the Area of Circle. 
Ask user whether he wish to continue calculating, 
calculate Area until user say No.

"""
choice ='y'

while(choice=='y'):
    radius = int(input("Enter the Radius of Circle: "))
    
    Area = 3.14 * (radius ** 2)
    
    print("Area of Circle with Radius "+str(radius)+" is "+str(Area))
    
    choice = input("Wish to continue calculating: (enter y/n)")

print("Thanks for using circle calculator")