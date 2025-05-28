a, b = int(input("son kiriting: ")),  int(input("son kiriting: "))
sonlar = []

for i in range (a, b):
    sonlar.insert(-1, i)

for i in range (len(sonlar)):
    if sonlar[i] % 2 != 0:
        print(sonlar[i], end = " ")