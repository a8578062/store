import random
shop = [
    ["Iphone", 1000],
    ["Mac loptop", 12000],
    ["Iwatch", 500],
    ["Lenovo PC", 4000],
    ["辣条", 10],
    ["洗衣粉", 23.5]
]
#我的购物车
mycart = []

integral = 0    #当前积分

#让用户输入自己的薪资
while True:
    salary = input("请初始化您的薪资：")
    if salary.isdigit():
        salary = int(salary)
        break
    else:
        print("请输入合适的薪资！")

while True:
    discount = round((random.random() + 8) / 10, 2)  # 本次折扣
    preferential = int(random.random() * 100)
    pay = 0
    # 展示商品
    print("---------------欢迎光临，开业大酬宾，本次消费享受\033[41:20:1m","%.1f" % (discount * 10),"折优惠\033[0m-------------------")
    for item, value in enumerate(shop):
        print(item, value)
#输入要买的商品编号
    chose = input("请输入你要买的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        if chose >= len(shop):
            print("您输入的商品不存在！")
        else:
            if salary < shop[chose][1]:
                print("\033[41:20:1m余额不足！\033[0m")
            else:
                mycart.append(shop[chose])
                pay = shop[chose][1] * discount - preferential
                if pay <= 0:
                    pay = 0
                salary = salary - pay
                #积分
                integral = integral + (shop[chose][1] // 5000) * 200
                print("\033[32:20:1m购买成功！您的余额为：", "%.2f" % salary, "积分为：", integral, "\033[0m")
                print("\033[32:20:1m本次优惠卷金额为：",preferential, "\033[0m")
    elif chose == "Q" or chose == "q":
        break
    else:
        print("您输入不合法请重新输入！")

print("欢迎下次光临！您的购物车信息为：")

for item in mycart:
    print(item)
print("您的余额为：", "%.2f" % salary, "积分为：", integral)