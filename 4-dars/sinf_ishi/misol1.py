lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst1 = []
for i in range (len(lst)):
    if lst[i] % 2 == 0:
        lst1.append(lst[i])

print(lst1)
