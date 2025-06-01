def toq_son(n):
    if n > 0:
        n = n - 1
        toq_son(n)
    if n % 2 != 0:
        print(n, end = " ")

n = int(input("son kiriting: "))
toq_son(n+1)
    