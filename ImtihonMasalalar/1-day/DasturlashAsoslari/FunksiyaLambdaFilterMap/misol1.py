def nol_oxiriga_sur(lst):
    nollar = list(filter(lambda x: x == 0, lst))
    nol_bolmagan = list(filter(lambda x: x != 0, lst))
    return nol_bolmagan + nollar


lst = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 , 7, 1]
natija = nol_oxiriga_sur(lst)
print(natija)

