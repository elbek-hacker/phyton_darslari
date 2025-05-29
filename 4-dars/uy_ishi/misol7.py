n = int(input("Nechta mahsulot kiritasiz: "))
dict = {}
for i in range (n):
    keys = input(f"{i+1} - mahsulotni kiriting: " )
    value = int(input("Narxi: "))
    dict[keys] = value

print(dict)