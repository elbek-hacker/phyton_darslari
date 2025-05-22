son = int(input("son kiriting: "))
for i in range (0, son , 1):
    
    for j in range (0, son, 1):
        if i == 0  or i == son - 1 or j == 0 or j == son - 1:
                print("  1  ", end = "")
        else:
            print("  0  ", end = "")
    print("\n")