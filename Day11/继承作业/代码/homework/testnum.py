from homework.numerator import Numerator
numerator = Numerator()
while True:
    num1 = float(input("请输入第一个数："))
    num2 = float(input("请输入第二个数："))
    print("1:加法  2：减法  3：乘法  4：除法  5:退出")
    choose = input("请输入选项：")
    if choose == '1':
        print("结果为：", numerator.jia(num1, num2))
    elif choose == '2':
        print("结果为：", numerator.jian(num1, num2))
    elif choose == '3':
        print("结果为：", numerator.cheng(num1, num2))
    elif choose == '4':
        print("结果为：", numerator.chu(num1, num2))
    else:
        break