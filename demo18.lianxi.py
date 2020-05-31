# 计算平均值， >80返回优秀，否则返回一般
def calc(arr):
    totalScore = 0
    for score in arr:
        totalScore += score
    if (totalScore/len(arr)) > 80:
        return "优秀！" 
    else:
        return "一般！"

# 获取用户输入次数
def getList(count):
    myList = []
    while count>0:
        myList.append(int(input("请输入分数：")))
        count -= 1
    print(calc(myList))
    

getList(3)