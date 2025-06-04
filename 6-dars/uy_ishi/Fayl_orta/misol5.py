while True:
    son = int(input('''         ==== MENU ====
        1,2 yoki 3 ni tanlang

        1. Yangi fayl yarating
        2. Faylni ko'rsatish
        3. Faylga yangi element qo'shish
        4. Chiqish:  '''))
    if son == 1:
        fan = input("Maktab fanini kiriting: ")
        with open("fan.txt", "w") as file:
            file.write(f"{fan} ")
    elif son == 2:

        with open("fan.txt", "r") as file:
            fayl_ichi = file.read().strip()
        print(fayl_ichi)
    elif son == 3:
        new_fan = input("Yangi fan kiriting: ")
        with open("fan.txt", "a") as file:
            file.write(f"{new_fan} ")

        with open("fan.txt", "r") as file:
            new_fayl_ichi = file.read().strip()
        print(new_fayl_ichi)
    elif son == 4:
        print("Rahmat")
        break
    else: 
        print("Xato son kiritildi!")