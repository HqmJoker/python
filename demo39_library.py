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


# math
import math 
print(math.ceil(0.8))
print(math.floor(0.8))

# time
import time
print(time.localtime())
# %y/%m/%d %H %M %S
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 路径相关/文件相关
import os.path
print(os.path.exists("demo39_library.py1"))
print(os.path.exists("./user"))
print(os.path.isfile("./user"))
print(os.path.isfile("./user/user_center.py"))
print(os.path.abspath("./"))