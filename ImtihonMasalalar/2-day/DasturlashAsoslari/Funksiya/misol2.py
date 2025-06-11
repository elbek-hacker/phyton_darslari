def tartibla_toq_juft(lst):
    toqlar = []
    juftlar = []
    for i in lst:
        if i % 2 == 0:
            juftlar.append(i)
        else:
            toqlar.append(i)
    juftlar.sort(reverse = True)
    count = 0
    lst1 = []
    while (count < max(len(toqlar), len(juftlar))):
        lst1.extend((toqlar[count], juftlar[count]))
        # lst1.append(toqlar[count])
        # lst1.append(juftlar[count])
        count += 1
    return lst1



lst = [1,2,3,4,5,6,7,8,9,10]
natija = tartibla_toq_juft(lst)
print(natija)