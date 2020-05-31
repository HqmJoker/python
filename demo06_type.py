#数组
myList = [100,200,300,'2']
print(myList,type(myList))
#元组：就是一个带来枷锁的数组(数组数据只能读，不可写)
myTuple = (200,300) #定义元组
print(myTuple[0])
#myTuple[0] = 110 不可以修改元组的值
print(myTuple,type(myTuple))
myTuple1 = (40,) #元组只有一个项写法，(40)表示整数
#字典
#所有key都必须有引号（单双引号都可以）
myDict = {
    "age":20,
    "name":"dingding"
}
print(myDict,type(myDict))