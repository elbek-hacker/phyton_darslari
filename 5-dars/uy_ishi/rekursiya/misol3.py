def just_son(n):
    if n % 2 == 0 and n >  0:
        print(n, end = " ")
    if n > 0:
        n = n - 1
        just_son(n)
    

n = int(input("son kiriting: "))
just_son(n)
    