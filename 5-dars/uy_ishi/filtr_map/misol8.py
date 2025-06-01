lst = [3,7,9,14,7]
natija = set(filter(lambda a: a % 7 == 0, lst))

print(list(natija))