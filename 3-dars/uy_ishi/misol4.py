lst = [1, 2, 33, 5, 6, 7, 7]

son = int(input("son kiriting: "))

for i in range (len(lst)):
    for j in range (i, len(lst)):
        if lst[i] + lst[j] == son:
            print(f"{i}, {j}")