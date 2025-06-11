def sonini_qaytar(lst):
    count = 0
    for i in range (0, len(lst)-1):
        for j in range (i+1, len(lst)):
            if lst[i] == lst[j]:
                lst.remove(lst[i])
                count += 1

    return len(lst) - count

lst = [4,1,2,1,2]
natija = sonini_qaytar(lst)
print(natija)ong jjngrwo ongoewrjng jnrweon jrigeienfn nfvjenfneov enjvoejnfv eneojnjenr ejnoerneojrnfoejnv veornejonejo nfjeonej ejfnenfejnfejfoen