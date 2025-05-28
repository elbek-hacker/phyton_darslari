lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

new_lst = []
for d in lst:
    
    new_lst.append(d[:-1] + (100,))

print(new_lst)