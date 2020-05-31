# 获取输入的语文、数学、英语成绩，保存到数组中，计算平均值
'''
myList = []
totalScore = 0
chinese = int(input("your chinese grade："))
myList.append(chinese)
totalScore += chinese
math = int(input("your math grade："))
myList.append(math)
totalScore += math
english = int(input("your english grade："))
myList.append(english)
totalScore += english
print(myList)
print(totalScore)
print(totalScore/len(myList))
'''
myList = []
myList.append(int(input("your chinese is：")))
myList.append(int(input("your math is：")))
myList.append(int(input("your english is：")))
print(myList)
print((myList[0]+myList[1]+myList[2])/len(myList))
