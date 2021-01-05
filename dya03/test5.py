a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[j] <= a[i]:
            k = a[i]
            a[i] = a[j]
            a[j] = k
print(a)