a, b = int(input("son 1: ")), int(input("son 2: "))
for i in range (a + 1, b):
    if i < 2: continue
    count = 0
    for j in range (2, int(i ** 0.5) + 1): 
        if i % j == 0:
            count += 1; break
    if count == 0:
        print(i, end = " ")