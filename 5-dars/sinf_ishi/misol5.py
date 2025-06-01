from random import randint

def n_tasodifiy_son(N):
    N = randint(10 ** (N-1), 10 ** N)
    return N

print(n_tasodifiy_son(N = int(input("son kiriting: "))))

