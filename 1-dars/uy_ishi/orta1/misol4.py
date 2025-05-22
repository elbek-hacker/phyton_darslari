#N ni qabul qilib, N ta fibonachi sonini chop etish
N = int(input("son kiriting: "))
if N < 1:
    print("Xato")
elif N == 1:
    print(0)
elif N == 2:
    print(0, 1)
elif N > 2:
    son1 = 0
    son2 = 1
    print(0, 1, end = " ")
    for i in range(2, N, 1):
        son1, son2 = son2, son1
        son2 = son1 + son2
        print(son2, end = " ")