
n = int(input("Son kiriting: "))

yigindi = 0
for i in range(1, n + 1):
    yigindi += i
    for j in range (1, i + 1):
        print(j, end = "")
        if j != i:
            print('+', end = '')
    print("=", yigindi)