def dictga_aylantir(lst):
    dic = {}
    for i in lst:
        key = i[0]
        value = i[1:]
        dic[key] = value
    return dic
lst = [
    [1, "Jean Castro", "V"],
    [2, "Lula Powell", "V"],
    [3, "Brian Howell", "VI"],
    [4, "Lynne Foster", "VI"],
    [5, "Zachary Simon", "VII"],
]
natija = dictga_aylantir(lst)
for key, value in natija.items():
        print(f"{key}: {value}")