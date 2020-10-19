import re
content = 'Xiaoming has 100 bananas'
res = re.match('^Xi.*(\d+)\s.*s$',content) #  匹配一个数字
print(res.group(1))
res2 = re.match('^Xi.*?(\d+)\s.*s$',content) #  匹配多个数字
print(res2.group(1))