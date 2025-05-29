sinfdagilar = {"Eldor", "Elnur", "Elbek", "Xurshid", "Samariddin"}
face_iddan_otganlar = {"Sardor", "Abdurazzoq", "Javohir", "Muhammadamin", "Muhammadayyub", "Xurshid", "Samariddin"}

# hammasini ro'yxati
# sinfdagilar = sinfdagilar.union(face_iddan_otganlar)
# print(sinfdagilar)

# sinfda lekin face id dan o'tmagan
# print(sinfdagilar.difference(face_iddan_otganlar))

# face id dan o'tgan va darsda emas
# print(face_iddan_otganlar.difference(sinfdagilar))

# sinfda lekin face id dan o'tmagan yoki face id dan o'tgan va darsda emas
# print(face_iddan_otganlar.symmetric_difference(sinfdagilar))

# ham face iddan o'tgan ham darsda
# print(sinfdagilar.intersection(face_iddan_otganlar))


# print({3,4,5} - {5,6,7})
# print({3,4,5,6}.difference({5,6,7}))
# print({5,6,7}.difference({3,4,5,6}))
# # print({5,6,7}.intersection({3,4,5,6}))

# # print({5,6,7}.union({3,4,5,6}))

# print({5,6,7}.symmetric_difference({3,4,5,6}))

sonlar = {3,4,5,6,7,8}

sonlar1 = set()
for son in sonlar:
    if son % 2 == 0:
        sonlar1.add(son)
print(sonlar1)
