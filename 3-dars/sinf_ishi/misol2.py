sonlar = [1, 2, 3, 4, 5]
min = sonlar[0]
yig = 0
toq_soni = 0

for i in range (0, len(sonlar)):
    if sonlar[i] < min:
        min = sonlar[i]
    yig += sonlar[i]
    if sonlar[i] % 2 != 0:
        toq_soni += 1
print(f"Minimum son: {min}\nYigindi: {yig}\nToqlar soni: {toq_soni}")