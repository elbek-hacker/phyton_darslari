def qabul (list):
    list1 = []
    for i in list:
        if i > 0:
            list1.append(i)
    return list1

print(qabul(list = [1, -1, 2, 9, -3, -11, 20, 5, -8, 4]))
