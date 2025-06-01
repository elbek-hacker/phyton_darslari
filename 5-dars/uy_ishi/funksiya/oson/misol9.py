def katta_qiy(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
list = [3, 6, 8, 1, 0]
print(katta_qiy(list))