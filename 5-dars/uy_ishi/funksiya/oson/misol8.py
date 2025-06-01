def dict_yarat(list1, list2):
    dict = {}
    for k in range(len(list1)):
        i = list1[k]
        dict[i] = list2[k]
    return dict
list1 = ["Jon", "Jeyms", "Piter", "Tony"]
list2 = ["Vik", "Bond", "Parker", "Stark"]
print(dict_yarat(list1, list2))

