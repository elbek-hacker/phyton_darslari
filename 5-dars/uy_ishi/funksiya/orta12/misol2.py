def satrlar_farqi(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return i
    if len(list1) == len(list2):
        return -1
    else:
        return 0
list1 = 'olma'
list2 = 'olma'
print(satrlar_farqi(list1, list2))