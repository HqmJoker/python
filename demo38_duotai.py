# 多态： 在py中 所谓的多态就是通过方法的复写来实现的
class Test:
    def myFunc(self):
        print("it is a test")

class MyClass(Test):
    def myFunc(self):
        print("it is a new test")
obj = MyClass()
obj.myFunc()
