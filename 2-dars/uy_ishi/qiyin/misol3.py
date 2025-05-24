a, b = int(input("son 1: ")), int(input("son 2: "))
a, b = 2 * a, 2 * b
for i in range (a, b + 1):
    yig = 0
    if i % 2 == 0:
        j = i
        while j != 0:
            yig = yig*10 + j % 10
            j = j // 10
        print(yig, "(", i, ")", end = ' ')