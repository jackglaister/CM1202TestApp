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
                self.__password=pw
                self.__ID=users[item+2]
                self.__sessionToken=Token.Token(self.__ID)
                return True
        else:
            return False

class Student(user):
    def Menu():
        break

class Lecturer(user):
    def __setFormativeTest():
    def __setSummativeTest():
    def __setDeadline():
    def __init__(self):
    	#this is where the lecturer class will be instantiated for the given Lecturer information. 

class Token:
    def __init__(userID):
        
