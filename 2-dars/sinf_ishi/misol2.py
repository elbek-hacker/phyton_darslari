import random

daraja = int(input('''darajani tanlang:
1. oson
2. orta
3. qiyin\n'''))
jami_togri = 0
count_t = 5
count_n = 0
while 1:
    count_t = 0
    if daraja == 1:
        boshi = 1
        oxiri = 5
    elif daraja == 2:
        boshi = 6
        oxiri = 10
    elif daraja == 3:
        boshi = 11
        oxiri = 15
    for i in range (5, 0, -1):
        son1, son2 = random.randint(boshi, oxiri), random.randint(boshi, oxiri)
        print(f"{i} - savol")
        amal = random.choice(["+", "-", "*", "//"])
        if amal == "+":
            togri = son1 + son2

        elif amal == "-":
            togri = son1 - son2
            
        elif amal == "*":
            togri = son1 * son2
        
        elif amal == "//":
            togri = son1 // son2

        javob = int(input(f"{son1} {amal} {son2} = "))
        if javob == togri:
            print("togri topdingiz")
            count_t += 1
        else:
            print(f"notogri javob, to'g'ri javob: {togri}")
            count_n += 1
    jami_togri += count_t
    if count_t == 5:
        daraja += 1
        if daraja == 4:
            print("Yutdingiz :)")
            break
        elif daraja == 2:
            print("\nsiz o'ta darajaga o'tdingiz :)")
        elif daraja == 3:
            print("\nSiz qiyin darajaga o'tdingiz :)")
    else:
        print("yutqazdingiz")
        break
#if count_t == 5:
#   count_t = jami_togri
print(f'''to'g'ri javoblar soni: {jami_togri}
noto'g'ri javoblar soni: {count_n}''')