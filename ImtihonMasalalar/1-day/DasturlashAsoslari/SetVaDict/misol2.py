N = int(input("Son: "))

# 1-usul
dic = {}
for i in range (1, N):
    dic[i] = i*i
print(dic)

# 2-usul
dicc = {i: i*i for i in range(1, N)}
print(dicc)