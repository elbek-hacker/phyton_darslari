N = int(input("son: "))
yig = 0
for i in range (1, N):
    if N % i == 0:
        yig += i
print(yig)
if yig > 9 and yig < 20:
    print("O'n", end = " ")
elif yig > 19 and yig < 30:
    print("Yigirma", end = " ")
elif yig > 29 and yig < 40:
    print("O'ttiz", end = " ")
elif yig > 39 and yig < 50:
    print("Qirq", end = " ")
elif yig > 49 and yig < 60:
    print("Ellik", end = " ")
elif yig > 59 and yig < 70:
    print("Oltmish", end = " ")
elif yig > 69 and yig < 80:
    print("Yetmish", end = " ")
elif yig > 79 and yig < 90:
    print("Sakson", end = " ")
elif yig > 89 and yig < 100:
    print("To'qson", end = " ")
r = yig % 10
if r == 1:
    print("bir")
elif r == 2:
    print("ikki")
elif r == 3:
    print("uch")
elif r == 4:
    print("to'rt")
elif r == 5:
    print("besh")
elif r == 6:
    print("olti")
elif r == 7:
    print("yetti")
elif r == 8:
    print("sakkiz")
elif r == 9:
    print("to'qqiz")