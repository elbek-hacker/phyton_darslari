#sonning raqamlar yigindisi
son = int(input("son kiriting: "))
yig = 0
while son != 0:
    yig += son % 10
    son = son // 10
print(yig)