son = int(input("son kiriting: "))
for i in range (1, son + 1, 1):
    for j in range (son - i + 1, 0, -1):
        print("*", end = "  ")
    print("\n")