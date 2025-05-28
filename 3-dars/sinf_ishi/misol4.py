import random
yig = 0
sonlar = []
for i in range(20):
    son = random.randint(1,100)
    yig += son
    sonlar.append(son)
print(sonlar)
print(f"ortacha qiymat: {yig//20}")
