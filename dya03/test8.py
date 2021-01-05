# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["何登勇", "56", "男", "106", "IBM", 500, "50"],
    ["曹东雪", "19", "女", "230", "微软", 501, "60"],
    ["刘营营", "19", "女", "210", "Oracle", 600, "60"],
    ["李汉聪", "45", "男", "230", "Tencent", 700, "10"],
    ["张佳伟", "45", "男", "220", "alibaba", 500, "30"]
]
#平均薪资
sum = 0
for i in range(len(names)):
    sum = sum + names[i][5]
print("平均薪资为：", sum/len(names))

#平均年龄
age = 0
for i in range(len(names)):
    age = age + int(names[i][1])
print("平均年龄为：", age/len(names))

#男女人数
men = 0
women = 0
for i in range(0, len(names)):
    if names[i][2] == "男":
        men = men + 1
    else:
        women = women + 1
print("男性人数为：", men, "\t女性人数为：", women)

#部门人数
sum60 = 0
sum50 = 0
sum30 = 0
sum10 = 0
for i in range(0, len(names)):
    if names[i][6] == "50":
        sum50 = sum50 + 1
    elif names[i][6] == "60":
        sum60 = sum60 + 1
    elif names[i][6] == "30":
        sum30 = sum30 + 1
    elif names[i][6] == "10":
        sum10 = sum10 + 1
print("60部门人数为：", sum60)
print("50部门人数为：", sum50)
print("30部门人数为：", sum30)
print("10部门人数为：", sum10)

