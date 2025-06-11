def sarala(lst1):
    lst = []
    for odam in lst1:
        if odam['age'] > 18 and odam['cars'] > 1:
            lst.append(odam)
    return lst


lst1 = [
    {"Name": "Asil", "age": 9, "cars": 3},
    {"Name": "Laziz", "age": 19, "cars": 2},
    {"Name": "Sardor", "age": 25, "cars": 7},
    {"Name": "Og`abek", "age": 5, "cars": 5},
]
natija = sarala(lst1)
print(natija)