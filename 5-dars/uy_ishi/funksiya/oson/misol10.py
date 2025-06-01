def per_yuza(a, b):
    list = []
    per = 2 * (a + b)
    yuza = a * b
    list.append(per)
    list.append(yuza)
    list = tuple(list)
    return list
print(per_yuza(5, 6))