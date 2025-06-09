N = int(input("Nechta maxsulot kiritmoqchisiz?: "))
dict = {}
for i in range(N):
    keys = input(f"{i+1} - Mahsulot nomi?: ")
    dict[keys] = int(input("Mahsulot narxi?: "))
print(dict)