class Monester:
    hp = 100
    def __init__(self, hp):
        self.hp = hp
    def WhoAmI(self):
        print("我是Monester")
class Boss(Monester):
    name = ""
    def __init__(self, hp, name):
        self.name = name
        super().__init__(hp)
    def WhoAmI(self):
        print("我是%s"%(self.name))

boss = Boss(5000, "蜘蛛王")
boss.WhoAmI()
print(boss.hp)