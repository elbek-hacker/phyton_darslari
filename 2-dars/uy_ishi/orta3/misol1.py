son = int(input("son kiriting: "))
for i in range (1, son):
    print(i, end = " ")
    if i == son - 1:
        for j in range (son, 0, -1):
            print(j, end = " ")