
lst = list(map(int, input("Ikkita son: ").split()))

try:
    if len(lst) == 2:
        print(lst[0] // lst[-1])
    else:
        print("Ikkita son yozish kerak!")
except ZeroDivisionError:
    print("Sonni nolga bo'lib bo'lmaydi!")
except ValueError:
    print("Raqam kiriting!")
except:
    print("Xato!!!")