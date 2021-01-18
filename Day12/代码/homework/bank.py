from homework.MoneyException import MoneyException
money = int(input("请输入金额："))
try:
    if money > 3000:
        raise MoneyException("余额不足！")
    else:
        print("取钱成功！")
except MoneyException:
    print("金额不足")