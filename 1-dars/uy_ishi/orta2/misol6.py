son = int(input("son kiriting: "))
for i in range (1, son + 1, 1):
    for j in range ((2*son)//2 - i, 0, -1):
        print("   ", end = "")
    for a in range (0, 2*i-1, 1):
        print(" * ", end = "")
    print("\n")