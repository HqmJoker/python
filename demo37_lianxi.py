class Student:
    id = ""
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def study(self):
        print("学号为%s的学生%s正在上课!"%(self.id, self.name))

class Doctor(Student):
    def __init__(self, id, name):
        super().__init__(id, name)
    def publish(self):
        print("%s发布了一篇论文"%(self.name))

doctor = Doctor('10086',"dingding")
doctor.study()
doctor.publish()
