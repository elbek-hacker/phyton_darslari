#To'liq emas, lekin ishlaydi :)
import random

uy_hayvonlar = ["tovuq", "echki", "it", "mushuk", "quyon", "sigir", "ot", ]

hayvon = random.choice(uy_hayvonlar)

#print(hayvon)
yashirish = []
for a in range (len(hayvon)):
    yashirish.append('□')
print(' '.join(yashirish))
qaytarilgan_harf = []

togri_top_soni = 0
count_while = 5
while 1:
    
    count = 0
    print(count_while, "- ta urinish qoldi")
    
    harf = input("Harf kiriting: ")

    for j in range (len(hayvon)):
        harf = harf.lower()
        count_qaytarilgan = 0
        if harf == hayvon[j]:
            count += 1
            for k in range (len(qaytarilgan_harf)):
                if harf == qaytarilgan_harf[k]:
                    count_qaytarilgan += 1
            if count_qaytarilgan > 0:
                print("Bu harf oldin kiritilgan :)")
                count_while -= 1
                continue
            qaytarilgan_harf.append(harf)

            topilgan_index = j
            togri_top_soni += 1
            yashirish.pop(topilgan_index)
            yashirish.insert(topilgan_index, harf)
    if count > 0:
        print("Bu harf so'zda bor :)")   
    else :
        print("Bu harf so'zda yo'q :(")
        count_while -= 1
    print(' '.join(yashirish))

    if togri_top_soni == len(hayvon):
        print("Tabriklayman. Siz yutdingiz :)")
        break
    elif count_while == 0:
        print("Siz yutqazdingiz :(")
        break
