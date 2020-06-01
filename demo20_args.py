# 可变长参数
def test():
    pass
    # print(arguments)
# test(100,200,300)
test()

# 可变长参数
def myFunc(*myArgs):
    print(myArgs)
    print(list(myArgs))

myFunc()
myFunc(1,2,3)

def myTest(**myArgs):
    print(myArgs)

myTest()
myTest(a=1,b=2)