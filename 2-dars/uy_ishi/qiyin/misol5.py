N, M = int(input("son_1: ")), int(input("son_2: "))

yig = 0
for i in range (N, M + 1):
    count = 0
    for j in range (2, i // 2 + 1):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        yig += i
print(yig)
