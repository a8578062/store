from homework.AgeException import AgeException
class Person:
    __age = None

    def setAge(self, age):
        if age <= 0:
            raise AgeException("输入非法！")
        else:
            self.__age = age

    def getAge(self):
        return self.__age

