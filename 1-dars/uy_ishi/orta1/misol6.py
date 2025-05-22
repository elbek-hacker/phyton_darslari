#Foydalanuvchi natural son kiritadi. Shu sonning natural bo'luvchilari
son = int (input("son kiriting: "))
for i in range(1, son+1, 1):
    if son % i == 0:
        print(i, end = " ")