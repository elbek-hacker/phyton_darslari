'''Butun sonni o'qib olib, unda yonma-yon 2ta bir xil
son bor yoki yo'qligini aniqlovchi dastur yozing'''

son = int(input("son kiriting:"))
raqam = son % 10
counter = 0
while son != 0:
    copy_raqam = raqam
    son = son // 10
    raqam = son % 10
    if copy_raqam == raqam:
        counter += 1
        break
if counter == 1:
    print("BOR")
else:
    print("YO'Q")