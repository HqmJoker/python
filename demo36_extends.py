# 继承
class Ticket:
    id = 0
    content = "默认的订单内容"
    def __init__(self, id, content):
        self.id = id
        self.content = content

class DeliveryTicket(Ticket):
    sender = "默认的骑手"
    def __init__(self, id, content, sender):
        self.sender = sender
        # 方案一
        # self.id = id
        # self.content = content
        # 方案二
        super().__init__(id, content)

dticket = DeliveryTicket(1, "商品1", "mike")

print(dticket.sender)
print(dticket.content)