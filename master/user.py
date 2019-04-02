import csv
import hashlib
class User:
    def verifyLogin(self):
        #This is a routine which returns a bool value of true or false for the user's login
        #If true is returned, this means taht user will be able to login and will be greeted with an appropriate welcome screen. 
        #Otherwise the user will be told their login information is wrong and will be sent back to the login screen to try again. 
        file = open("usernames.txt","r")
        fr = csv.Reader(file)
        users = []
        for row in fr:
            for item in row:
                users.append(item)
        un = input("please enter your username")
        pw = input("please enter your password")
        for item in range(len(users[::3])):
            if users[item] == un and users[item+1] == hashlib.sha256(b(pw)).hexdigest():
                self.__name=un
                self.__ID=users[item+2]
                self.sessionToken=Token.Token(self.__ID)
                return True
        else:
            return False
    def __init__(self):
        self.verifyLogin()

class Student(User):
    def Menu():
        pass

class Lecturer(User):
    def __setFormativeTest():
        pass
    def __setSummativeTest():
        pass
    def __setDeadline():
        pass
    def menu():
        pass

class Token:
    def __init__(self, userID):
        self.__ExpiryDate
        self.__TokenID = userID
        self.__AdminPermissions = userID[0]
        
