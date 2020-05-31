# 不支持++语法
# 位运算
num1 = int("00111010", 2)
num2 = int("00100011", 2)
print(num1, num2)
print(num1&num2)
print(num1|num2)
print(58&35)

# 身份运算 is
name1 = "jack"
name2 = "lim"
print(name1 is name2) #判断变量内存地址是否一致
class1 = "123"
class2 = "123"
print(class1)
print(class1 is class2)
print(id(class1))
print(id(class2))

myList1 = [1,2,3]
myList2 = [1,2,3]
print(id(myList1))
print(id(myList2))