# 1-usul
def borini_qaytar(a, b):
    a, b = set(a), set(b)
    # lst = a.intersection(b)
    lst = a & b
    return lst

# 2-usul
# def borini_qaytar(a, b):
#       return [i for i in a if i in b]

# 3-usul
# def borini_qaytar(a, b):
#       return list(filter(lambda x: x in b, a))

# 4-usul. The most fastest :)
# def borini_qaytar(a, b):
#     return list(set(a) & set(b))

# 5-usul
# def borini_qaytar(a, b):
#     result = []
#     for i in a:
#         if i in b and i not in result:
#             result.append(i)
#     return result


a = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

natija = borini_qaytar(a, b)
print(natija)