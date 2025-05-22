qator = int(input("Qatorni kiriting: "))
ustun = int(input("Ustunni kiriting: "))
for i in range (0, qator , 1):
    
    for j in range (0, ustun, 1):
        if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                print("  1  ", end = "")
        else:
            print("  0  ", end = "")
    print("\n")