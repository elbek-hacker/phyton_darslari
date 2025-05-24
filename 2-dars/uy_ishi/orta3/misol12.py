# Optimal version :)
N = int(input("son: "))
if N % 5 == 0:
    M = N // 5
else:
    M = N // 5 + 1
son1, son2 = 1, 6
if N < 5:
    son2 = N % 5 + 1
for a in range (1, M + 1):
    for i in range(1, 11):
        for j in range(son1, son2):   
            print(f"{j} * {i} = {i * j}", end="\t")   
        print()
    print()
    son1 += 5
    if N % 5 != 0 and a == M - 1:
        son2 = son2 + N % 5
    else:
        son2 += 5