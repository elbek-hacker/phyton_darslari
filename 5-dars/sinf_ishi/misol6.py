def faktorlar (n: int) -> list:

    list = []
    for i in range (2, n):
        if n % i == 0:
            list.append(i)
    return list
print(faktorlar(n = int(input("son kiriting: "))))
