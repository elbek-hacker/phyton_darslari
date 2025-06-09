def toqlarni_qaytar(lst):
    return list(filter(lambda x: x % 2 == 1, lst))

# 2-usul.  filtersiz
#   return [x for x in lst if x % 2 == 1]

lst = [2,3,4,5]
natija = toqlarni_qaytar(lst)
print(natija)