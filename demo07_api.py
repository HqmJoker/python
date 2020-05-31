#数组、元组、字典常见api
scoreList = [100,200]
# 向数组中插入数据 append/insert
scoreList.append(300) #尾部追加
print(scoreList)
scoreList.insert(0,50) #
print(scoreList)
# 从数组中删除数据 clear/pop
# scoreList.clear() #删除数组所有元素
scoreList.pop(1)
print(scoreList)
# 从数组中查看数据
myList = ['diingding', 'lucy', 'mike', 'apple', 'banana']
print(myList[1])
print(myList[-2])
# 修改数组数据
myList[0] = 'linchong'
print(myList)
# reverse
myList.reverse()
print(myList)
# sort 排序
myList.sort(reverse=True) #默认为升序，reverse=False为降序
print(myList)
# 获取数组长度
print(len(myList))