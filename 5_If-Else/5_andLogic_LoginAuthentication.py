"""
Program to use Logic Operator 'and'

Create an Login Authentication Application, 

where if username and password entered by user 

matches with registered one, then user is allowed to Login

"""
regUserName = "Renuka"
regPassWord = "Creativity!"

username= input("Enter Username: ")
password= input("Enter Password: ")

if regUserName == username and regPassWord == password:
    print("You are allowed to Login!!")
    
else:
    print("Invalid Username or Password!!")
    