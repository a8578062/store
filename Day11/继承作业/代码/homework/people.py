class People:
    __name = None
    __age = None
    __sex = None

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex = sex

    def getSex(self):
        return self.__sex

class WorkPeople(People):
    def work(self):
        print(super().getAge(),"岁的工人",super().getName(),"在干活。")

class Student(People):
    def study(self):
        print(super().getAge(), "岁的",super().getSex(),"学生", super().getName(), "在学习。")

    def sing(self):
        print(super().getAge(), "岁的", super().getSex(), "学生", super().getName(), "在唱歌。")
