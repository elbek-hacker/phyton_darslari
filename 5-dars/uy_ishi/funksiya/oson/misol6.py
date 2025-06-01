def musbat_sonlar(list):
    list1 = []
    for i in list:
        if i > 0:
            list1.append(i)
    return list1

list = [1, -1, 2, 9, -3, -11, 20, 5, -8, 4]
print(musbat_sonlar(list))