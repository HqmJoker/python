def getList():
    userList = []
    def login(uname=""):
        userList.insert(0,uname)
        return userList
    return login

loginObj = getList()
print(loginObj(uname="dingding"))
print(loginObj(uname="milk"))
print(loginObj(uname="cordova"))
