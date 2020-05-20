"""
Program to take input as multiple values, the personal info and Marks

Name

Roll Number

Subject 1 Marks
Subject 2 Marks
Subject 3 Marks

And Give us the percentage of the Student
"""

name = input("Enter the name")
RollNo = int( input ("Enter your Roll Number"))
Marks1 = float( input("Enter Marks for Subject 1"))
Marks2 = float( input("Enter Marks for Subject 2"))
Marks3 = float( input("Enter Marks for Subject 3"))

Percentage = ((Marks1+Marks2+Marks3) / 300)*100

print("Name of Student: "+ name)
print("Roll Number: " + str(RollNo))
print("Percentage: "+ str(Percentage) )