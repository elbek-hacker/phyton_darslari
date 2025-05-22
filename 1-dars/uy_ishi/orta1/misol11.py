'''Barcha uch xonali sonlar orasidagi raqamlaridan
kamida bittasida 3 raqami bo'lgan sonlani
chiqaruvchi dastur tuzing'''
for i in range (100, 1000, 1):
    son = i
    while i != 0:
        raqam = i % 10
        if raqam == 3:
            print(son, end = " ")
        i = i // 10