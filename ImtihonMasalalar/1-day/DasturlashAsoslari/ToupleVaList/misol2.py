a, b = int(input("son1: ")), int(input("son2: "))
list = []
for i in range (a, b):
    if i % 2 == 1:
        list.append(i)

print(list)