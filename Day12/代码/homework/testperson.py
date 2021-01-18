from homework.Person import Person
from homework.AgeException import AgeException
p1 = Person()
try:
    p1.setAge(-3)
except AgeException:
    print("输入非法！")