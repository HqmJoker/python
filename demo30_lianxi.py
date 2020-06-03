myList = [1,2,3]
try:
    myList[10]
except IndexError as msg:
    print(msg)
    print("数组越界了")
finally:
    print("程序执行结束")

try:
    data = {
        "msg":"这是一个自定错误",
        "code":300
    }
    raise(IndexError(data))
except IndexError as msg:
    print(msg)
    print(type(msg))
    # print(msg["msg"])
    # print(msg["code"])
finally:
    print("程序执行结束")