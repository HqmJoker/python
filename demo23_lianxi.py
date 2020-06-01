def getValue(*arg):
    # maxNum = arg[0]
    # minNum = arg[0]
    # for tmp in arg:
    #     if(tmp>maxNum):
    #         maxNum = tmp
    #     if(tmp<minNum):
    #         minNum = tmp
    maxNum = max(arg)
    minNum = min(arg)
    print("最大值：%d"%(maxNum))
    print("最小值：%d"%(minNum))
    return maxNum, minNum

def test(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)

def calc(num):
    tatol = 1
    while num>0:
        tatol *= num
        num -= 1
    return tatol

print(getValue(100,300,200))
test(arg1=3,arg3=9,arg2=5)
print(calc(6))
