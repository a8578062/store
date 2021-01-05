list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(list)
for i in range(0, n//2):
    t = list[i]
    list[i] = list[(n-1-i)]
    list[(n-1-i)] = t
print(list)
