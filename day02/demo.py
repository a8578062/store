name = input("请输入姓名：")
num = input("请输入身份证号：")
age = input("请输入年龄：")
sex = input("请输入性别：")
high = input("请输入身高：")
weight = input("请输入体重：")


info = '''
------------个人信息------------
        姓名：     {name}
        身份证号：  {num}
        年龄：     {age}岁
        性别：     {sex}
        身高：     {high}m
        体重：     {weight}kg
'''

print(info.format(name=name,age=age,sex=sex,high=high,weight=weight,num=num))

