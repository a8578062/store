username = 'jason'
password = 'admin'
i = 2
while i >= 0:
    username1 = input("请输入用户名：")
    password1 = input("请输入密码：")
    if username1 == username and password == password1:
        print("登录成功")
        break
    else:
        print("用户名密码错误！还有",i,"次机会")
    i = i - 1
