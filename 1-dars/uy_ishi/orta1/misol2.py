N = int(input("son kiriting: "))
M = int(input("son kiriting: "))
K = int(input("son kiriting: "))
juft_soni = 0
juft_yigindi = 0
for i in range (N, M, 1):
    if i % 2 == 0:
        juft_yigindi += i
        juft_soni += 1
    if juft_soni == K:
        break
    
print(juft_yigindi)
