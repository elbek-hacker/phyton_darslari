def takrorni_qaytar(lst1):
    return [x for x in lst1 if lst1.count(x) > 1]

# yuqorida short versiyasi
# result = []
# for x in lst:
#     if lst.count(x) > 1:
#         result.append(x)
# return result


lst1 = [1,2,6,4,3,2,4,6]
natija = takrorni_qaytar(lst1)
print(natija)