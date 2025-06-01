lst1, lst2, lst3 = [1,2,3], [4, 5, 6], [7, 8, 9]

natija = map(lambda a, b, c: a*b*c, lst1, lst2, lst3)

print(list(natija))