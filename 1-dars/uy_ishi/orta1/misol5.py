N = int(input("son kiriting: "))
M = int(input("son kiriting: "))
K = int(input("son kiriting: "))
counter = 0

for s in range (1, 2, 1):
    f_son = 0
    if N <= f_son and f_son <= M:
        print(0, end = " ")
        counter += 1
        if counter == K:
            break
    son1 = 0
    f_son = 1
    if N <= f_son and  f_son <= M:
        print(1, end = " ")
        counter += 1
        if counter == K:
            break
    while 1:
        son1, f_son = f_son, son1
        f_son = son1 + f_son
        if f_son > N and f_son < M:
            print(f_son, end = " ")
            counter += 1
            if counter == K:
                break