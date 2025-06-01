from random import randint

def n_tasodifiy_son(n):
    a = randint(10 ** (n-1), 10 ** n - 1)
    return a
print(n_tasodifiy_son(n = int(input("necha xonali son kerak?: "))))