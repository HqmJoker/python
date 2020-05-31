myDict = {}
myList = [100,200,300]
myTuple = (101,201,301)
myDict1 = {
    "age": 20,
    "name":"dingding"
}
myDict["myList"] = myList
myDict["myTuple"] = myTuple
myDict["myDict1"] = myDict1
print(myDict)
# 删除字典
myDict.pop("myDict1")
print(myDict)
# 修改list数组中值，添加值
myDict.get("myList").append(400)
print(myDict)