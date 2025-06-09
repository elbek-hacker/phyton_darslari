# Calculator, for fun XDXD
son1 = int(input("son: "))
mark = input("amal: ")
son2 = int(input("son: "))
if mark == '+':
    print(f"{son1} {mark} {son2} = {son1 + son2}")
elif mark == '-':
    print(f"{son1} {mark} {son2} = {son1 - son2}")
elif mark == '*':
    print(f"{son1} {mark} {son2} = {son1 * son2}")
elif mark == '/':
    if son2 == 0:
        print("Xato: sonni nolga bo'lib bo'lmaydi.")
    else:
        print(f"{son1} {mark} {son2} = {son1 / son2}")
else:
    print("Noto'g'ri amal kiritildi!")