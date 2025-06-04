lst = list(map(int, input("Sonlar:").split()))
index = int(input("Index kiriting: "))

try:
    index < len(lst)
    print(lst[index])
except IndexError:
    print("Bunday index mavjud emas")