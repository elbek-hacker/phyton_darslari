son = int(input("son kiriting: "))
for i in range(son, 0, -1):
    for j in range(0, i, 1):
        print(j + 1, end = "")
    print("")