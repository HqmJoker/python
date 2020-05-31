# python实现 for/white 不支持do-white
myList = [100,200,300]
for tmp in myList:
    print(tmp)
#补充知识点：range
print(list(range(3))) 
print(list(range(3,5))) 

for tmp in range(len(myList)):
    print(tmp,myList[tmp])
# while
count = 0
while count<5:
    print(count)
    count += 1
# break 停止循环/continue 直接进入下一次循环
while True:
    msg = input()
    # 输入next进入下一次
    if msg == 'next':
        continue
    print(msg)
    # 当msg是exit，结束循环
    if msg == 'exit':
        break
