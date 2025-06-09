def kvadratga_oshir(lst):
# 1-usul
    return list(map(lambda x: x*x, lst))

# 2-usul
    # def kvadratga_oshir(lst):
    #     return [x * x for x in lst]


lst = [1,2,3,4,5,6,7,8,9,10]
natija = kvadratga_oshir(lst)
print(natija)

