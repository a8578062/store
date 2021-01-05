'''
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,"=",i*j,"\t",end="")
    print()
'''
a = [10,1,3,2,6,9,7,5,4,10]
'''
求和
sum = 0
for i in range(0,len(a)):
    sum = sum + a[i]

print(sum)

偶数和
sum = 0
for i in range(0,len(a)):
    if a[i] % 2 == 0:
        sum = sum + a[i]

print(sum)

最大值
k=0
for i in range(0,len(a)):
    if a[i] >= k:
        k = a[i]
print(k)
'''
#选择排序
k=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j] >= a[i]:
            k = a[i]
            a[i] = a[j]
            a[j] = k
print(a)

