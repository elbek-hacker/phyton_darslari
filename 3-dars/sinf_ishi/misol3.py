
nechta = int(input("Nechta son kiritasiz: "))

sonlar = []
for i in range(0, nechta):
    son = int(input(f"{i+1} sonni kiriting: "))
    sonlar.insert(0, son)
print(sonlar)
