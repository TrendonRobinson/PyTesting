import time, math


class SignUpForm():

    def __init__(self, username, email, password):
        print(username, email, password)
        self.username   = username
        self.email      = email
        self.password   = password

    def printDetails(self):
        print(self.username, self.email, self.password)