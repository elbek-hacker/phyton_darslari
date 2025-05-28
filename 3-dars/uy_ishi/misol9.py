touple = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]

new_lst = []
for t in touple:
    if t != ():
        new_lst.append(t)

print(new_lst)