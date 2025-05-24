N = int(input("son: "))
for i in range (1, N + 1):
    if N % i == 0:
        if i % 2 != 0:
            print(i, end = " ")