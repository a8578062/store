a = [15, 20, 12, 63, 3, 8, 94, 61, 27, 5, 10]
sum = 0
for i in range(0, len(a)):
    if a[i] % 5 == 0:
        sum = sum + a[i]
print("5的倍数的和为：", sum)