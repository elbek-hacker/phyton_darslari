def joylashtir(list1, list2):
    list3 = []
    count = 0
    while count < max(len(list1), len(list2)):
        
        if len(list1) > count:
            list3.append(list1[count])
        if len(list2) > count:
            list3.append(list2[count])
        
        count += 1
    return list3

list1=[1, 2, 3, 4] 
list2=[11, 22, 33]
natija = joylashtir(list1, list2)
print(natija)