def yigindi_list(lst):
    lst1 = list(map(lambda x: sum(x), lst))
    return lst1

lst = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
natija = yigindi_list(lst)
print(natija)