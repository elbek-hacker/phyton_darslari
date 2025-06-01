def faktor_top(N):
    list = []
    for i in range(2, N):
        if N % i == 0:
            list.append(i)
    return list

print(faktor_top(N = int(input("son kiriting: "))))