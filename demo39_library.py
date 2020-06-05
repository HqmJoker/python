# py自带的标准库

# json
import json
myDict = {
    "age":10,
    "score":80,
    'name':'jack'
}
# json序列化,转换成json格式字符串
result = json.dumps(myDict)
print(result)
print(type(result))
# json反序列化,解析一个json格式字符串
result1 = json.loads('{"id":10}')
print(result1)
print(type(result1))

# random
import random
num = random.choice(range(1,100))
print("num is %d"%(num))
print(random.choice(['mike','michale', 'lucy']))
print(random.randint(1,100))