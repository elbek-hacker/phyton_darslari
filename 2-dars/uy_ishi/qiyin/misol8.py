n = int(input("son: "))

for i in range (0, n):
    for j in range (0, n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or (i == j or i == n - j - 1) and i < n // 2 :
            print("* ", end = "")
        else:
            print("  ", end = "")
    print()