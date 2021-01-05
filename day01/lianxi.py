'''
i=1
j=1
while j < 10:
    print(i,"x",j,"=",i*j,"\t",end="")
    if i == j :
        i = 0
        j =j + 1
        print("")
    i = i + 1
    print("*"*i)

j=6
for i in range(1,8):
    print(" " * j,"*" * i)
    j=j-1

for i in range(1,8):
    if i ==1:
        print("      *")
    elif i == 2:
        print("     * *")
    elif i == 3:
        print("    * * *")
    elif i == 4:
        print("   * * * *")
    elif i == 5:
        print("  * * * * *")
    elif i == 6:
        print(" * * * * * *")
    else:
        print("* * * * * * *")

for f in range(6):
    for l in range(5-f):
        print(" ",end="")
    for g in range(f+1):
        print("*",end=" ")
    print("")

for i in range(1,8):
    if i % 2 != 0:
        for j in range(1,7+i):
            if j % 2 != 0:
                print("*",end="")
            else:
                print(" ", end="")
    else:
        for j in range(1,7+i):
            if j % 2 != 0:
                print(" ", end="")
            else:
                print("*", end="")
    print() ###暂时不会


j=6
for i in range(1,8):
    print(" " * j,"* " * i)
    j = j - 1


def sum(x, y):
    r = x + y
    return r

a = sum(7,9)
print(a)
'''

#discount = round((random.random() + 8) / 10, 2)
import random
discount = random.random() + 8 / 10
print ("%.2f" % discount)


