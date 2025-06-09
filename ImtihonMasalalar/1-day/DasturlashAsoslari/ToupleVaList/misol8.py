lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
lst1 = []
for i in lst:
    a = list(i)
    a[-1] = 100
    lst1.append(tuple(a))
print(lst1)