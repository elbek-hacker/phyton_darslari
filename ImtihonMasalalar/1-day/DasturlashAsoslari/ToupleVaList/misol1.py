a, b = int(input("Son1: ")), int(input("Son2: "))

list = []
for i in range(a, b):
    if i % 2 == 0:
        list.append(i) 
print(list)