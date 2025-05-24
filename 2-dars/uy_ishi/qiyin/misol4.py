N, M, K = int(input("son_N: ")), int(input("son_M: ")), int(input("son_K: "))
N, M = N + K, M +K
yig = 0
for i in range (N, M + 1):
    if i % K != 0:
        yig += i
print(yig)