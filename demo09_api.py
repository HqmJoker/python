# 元组：不可修改的数组
myTuple = (100,200)
print(len(myTuple))

# 字典
myDict = {
    "age":20,
    "name":"dingding"
}
# 添加
myDict["score"] = 80
print(myDict)
# 删除
myDict.pop("age")
print(myDict)
# 修改
myDict["name"] = "mike"
print(myDict)
# 查找
# print(myDict["score1"])
print(myDict.get("score1"))
# 强制类型转换
myValues = list(myDict.values())
print(myValues[0])
myKeys = list(myDict.keys())
print(myKeys)
