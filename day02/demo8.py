a = float(input("请输入三角形边1(正整数)："))
b = float(input("请输入三角形边2(正整数)："))
c = float(input("请输入三角形边3(正整数)："))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a == b  and a == c and b == c:
            print("构成等边三角形")
        elif a == b and b != c and a != c:
            print("构成等腰三角形")
        elif a == c and a != b and b !=c:
            print("构成等腰三角形")
        elif b == c and a != b and a !=c:
            print("构成等腰三角形")
        else:
            print("构成普通三角形")
    else:
        print("不能构成三角形")

else:
    print("请输入正整数！")