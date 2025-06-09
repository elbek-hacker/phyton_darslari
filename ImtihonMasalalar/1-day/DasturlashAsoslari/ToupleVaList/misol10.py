lst = [('item1', '12:20'), ('item2', '15:10'), ('item3', '24:05')]
lst1 = []
for item, time in lst:
    new_time = time.replace(':', '.')

    lst1.append((item, new_time))

natija = sorted(lst1, key = lambda x: float(x[1]), reverse = True)

print(natija)
