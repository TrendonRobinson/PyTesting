from Manager import SignUpForm
from emailValidation import check
import os

####################################

username    = ""
email       = ""
password    = ""

####################################


def usernameFucntion():
    username = str(input("Type in a valid username:"))
    for char in username:
        if char == " ":
            print("Spaces can not be included.")
            usernameFucntion()

def emailFunction():
    email = str(input("Type in your email:"))
    if check(email) == False:
        print("Enter a valid email.")
        emailFunction()

def passwordFunction():
    print("Password Requirements: \n - Longer than 6 characters \n")
    password = str(input("Type in a valid password:"))


    def failed():
        print("Password Does not meet requirements, try again.")
        passwordFunction()

    if len(password) < 6:
        failed()


    for char in password:
        if char == " ":
            failed()
            
            



usernameFucntion()
emailFunction()
passwordFunction()



FormInfo = SignUpForm(username, email, password)

#clear()

print(FormInfo)
print(username)
print(email)
print(password)
