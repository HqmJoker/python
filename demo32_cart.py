'''
import demo31_user


def addToCart():
    print(demo31_user.isLogin)
    if (not demo31_user.isLogin):
        print(demo31_user.login('dingding','111111'))
'''

'''
import demo31_user as user

def addToCart():
    print(user.isLogin)
'''

from demo31_user import *
def addToCart():
    print(isLogin)
addToCart()