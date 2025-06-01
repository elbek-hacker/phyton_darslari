lst = [121, 34, 565, 78]

natija = filter(lambda a: a == int(str(a)[::-1]), lst)

print(list(natija))