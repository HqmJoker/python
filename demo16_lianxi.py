import random
num = random.choice(range(1,100))
while True:
    inputNum = int(input("请输入数字："))
    if inputNum == num:
        print("猜对了！")
        break
    elif inputNum < num:
        print("太小了")
    else:
        print("太大了") 