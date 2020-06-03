# 定位是指定匿名函数的
func = lambda x:x+1
print(func(3))
test = lambda x,y:x>y
print(test(4,3))
# python支持一个方法filter
myList = [1,2,3,4,5,6,7,8,9]
result = filter(lambda x:x%2==0, myList)
print(list(result))