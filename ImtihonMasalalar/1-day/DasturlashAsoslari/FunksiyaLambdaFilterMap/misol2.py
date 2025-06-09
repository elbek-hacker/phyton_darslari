def olib_tashla(lst):
    lst1 = []
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    return lst1

lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
natija = olib_tashla(lst)
print(natija)
