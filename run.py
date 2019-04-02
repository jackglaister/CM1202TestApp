import csv
from Test import *
from user import *

def userLogin():
    return User()

def importTestsList():
    file = open("Tests.csv")
    csvf = csv.reader(file)
    a = []
    for line in csvf:
        a.append(line)
    return a

if __name__ == '__main__':
    user = False
    while not user:
        user = userLogin()
    