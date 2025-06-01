def teskari(k):
    print(k % 10, end = " ")
    k = k // 10
    if k != 0:
        teskari(k)
teskari(1234)