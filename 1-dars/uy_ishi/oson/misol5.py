#Kiritilgan natural sonni mukammal ekanligini aniqlovchi dastur
son = int(input("son kiriting: "))
yig = 0
for i in range(1, son // 2 + 1, 1):
    if son % i == 0:
        yig += i

if yig == son:
    print("Mukammal son")
else:
    print("Mukammal emas")