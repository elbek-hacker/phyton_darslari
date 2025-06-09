def kubga_oshir(lst):
    return list(map(lambda x: x**3, lst))

# 2-usul
    # return [x ** 3 for x in lst]

lst = [1, 2, 3]
natija = kubga_oshir(lst)
print(natija)