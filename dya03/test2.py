h = 20
w = 3
b = 2
for i in range(1, 200):
    if w < h:
        h = h-(w-b)
        print("第", i, "天爬了", i*3-i*2, "米")
    else:
        print("第", i, "天爬出井")
        break
