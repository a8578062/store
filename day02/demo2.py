'''
import random
num = (random.random() * 100) // 1
i = 0

while True:
    a = int(input("请输入0-100的数字："))
    i = i+1
    if a > num:
        print("大了！")
    elif a < num:
        print("小了!")
    else:
        print("恭喜，本次数字为",num,"猜了",i,"次")
        break
'''
help("keywords")
