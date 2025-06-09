lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]
lst1 = []
for i in lst:
    if i != ():
        lst1.append(i)

print(lst1)