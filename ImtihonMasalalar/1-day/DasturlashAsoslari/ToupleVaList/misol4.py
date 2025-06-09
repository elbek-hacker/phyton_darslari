lst = [1, 2, 33, 5, 6, 7, 7]
lst1 = []
son = int(input("son: "))
for i in range (len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == son:
            lst1.append((i, j))

print(lst1)