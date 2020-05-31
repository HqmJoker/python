def modifyCount(count):
    count -= 1
    print("in modifyCount, count is %d"%(count))
count = 10
modifyCount(count)
print(count)

def consume(myList):
    myList[0] = 10
    print(myList)
myList = [100,200,300]
consume(myList)
print(myList)