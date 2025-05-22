son = int(input("son kiriting: "))
tes = 0
a = son
while son != 0:
    tes = tes * 10 + son % 10
    son = son // 10
print(a - tes)