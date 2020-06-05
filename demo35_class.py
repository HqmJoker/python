# 完成一个类的封装
class Order:
    id = 0
    price = 0
    content = ""
    # 构造函数
    def __init__(self, id, price, content):
        self.id = id
        self.price = price
        self.content = content
    # f方法
    def printOrder(self):
        print("打印了一张小票")
        print("订单编号为%d的订单价格是%d,订单内容是：%s"%(self.id, self.price, self.content))
# 调用(实例化)
orderObj = Order(10086, 15.5, "这是订单内容")
print(orderObj.price)
orderObj.printOrder()