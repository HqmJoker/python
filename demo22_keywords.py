# 关键字参数
def connect(host, port):
    print(host,port)

connect("localhost", 3306)
# 关键字参数 指的是在调用方法时，不用关心先后顺序：可通过形参匹配等号来指定实际要传递的参数
connect(port = 80, host = "localhost")

# 默认值参数
def myFunc(arg1, arg2=1):
    print(arg1, arg2)

myFunc(10)
myFunc(20)
myFunc(100)
myFunc(50)
myFunc(10,2)