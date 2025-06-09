def sarala(lst):
    return list(filter(lambda x: x[0] == 'a' or x[0] == 'A' or x[0] == 'f' or x[0] == 'F', lst))

# 2-usul
    # return list(filter(lambda x: x[0].lower() in ('a', 'f'), lst))
# 3-usul  filtersiz
    # return [x for x in lst if x[0].lower() in ('a', 'f')]


lst = ["Alisher","Kamoliddin", "abdulla", "Feruza", "Jamshid", "Dilnoza", "farhod", "Murod"]
natija = sarala(lst)
print(natija)