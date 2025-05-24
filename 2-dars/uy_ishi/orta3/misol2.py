N = int(input("son: "))
yig, son = 0, N
while N != 0:
    yig += N % 10
    N = N // 10
qoldiq = son % yig
print("qoldiq: ", qoldiq)