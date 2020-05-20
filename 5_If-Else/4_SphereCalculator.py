
"""
Program to create a Sphere Calculator

Ask user to choose the operation, whther he want to calculate:
    1. Area of Circle
    2. Circumference of Circle
    3. Surface area of Sphere
    4. Volume of Sphere
"""

print("Please choose the Operation:")
print("1. Calculate Area of Circle.")
print("2. Calculate Circumference of Circle ")
print("3. Calculate surface Area of Sphere.")
print("4. Calculate volume of Sphere ")

choice = int(input("Enter you choice:"))

radius = float(input("Enter the value of Radius: "))

if choice==1:
    Area= 3.14 * (radius ** 2)
    print("Area of circle with radius "+ str(radius)+" is: " + str(Area))
    
if choice==2:
    circum= 2* 3.14 * radius 
    print("Cicumference of circle with radius "+ str(radius)+" is: " + str(circum))    
    
if choice==3:
    SurfaceArea= 4* 3.14 * (radius ** 2)
    print("Area of Sphere with radius "+ str(radius)+" is: " + str(SurfaceArea))
    
if choice==4:
    Volume = (4/3)* 3.14 * (radius ** 3)
    print("Volume of a Shpere with radius "+ str(radius)+" is: " + str(Volume))