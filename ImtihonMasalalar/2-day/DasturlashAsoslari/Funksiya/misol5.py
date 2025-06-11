def kirit_va_sarala(lst):
# 1-usul
    lst1 = [x for x in lst if int(str(x)[0]) % 2 == 0]
    return lst1

# 2-usul
    # lst1 = []
    # for i in lst:
    #     a = int(str(i)[0])
    #     if a % 2 == 0:
    #         lst1.append(i)
    # return lst1
    
N = int(input("nechta son kiritasiz?: "))
lst = []
for i in range(N):
    lst.append(int(input(f"{i+1} - sonni kiriting: ")))
natija = kirit_va_sarala(lst)
print(natija)