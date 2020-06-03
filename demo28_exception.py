# js支持try/catch/finally
# python 支持try/except/finally
try:
    myAge = 10
    print(myAge)
except NameError:
    print("调用了未定义变量")
finally:
    print("exit")



# 如何捕获多个错误
try:
    age = int(input("请输入年龄：")) 
    print(age)
    print(count)

# 方案二
except ValueError:
    print("输入的数值不符合要求")
except NameError:
    print("调用了不存在变量")
# 方案一 
'''
except Exception as msg:
    print(msg)
    print("程序出错了")
'''