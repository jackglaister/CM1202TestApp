from Test import *
from user import *

def userLogin():
    return User()

if __name__ == '__main__':
    user = False
    while not user:
        user = userLogin()
    