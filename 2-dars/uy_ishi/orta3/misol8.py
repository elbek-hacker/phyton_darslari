a, b = int(input("son 1: ")), int(input("son 2: "))
count = 0
for i in range (b, a, -1):
    if i % 2 != 0 and count != 3:
        print(i, end = " ")
        count += 1