
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

for key, value in d1.items():
    if key in d2:
        d2[key] += value
    else:
        d2[key] = value
print(d2)