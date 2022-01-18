num=4
for i in range(1, num+1):
    for j in range(i, num+1):
        print("", end=" ")
    for k in range(0, i):
        print('*', end=" ")
    print()   