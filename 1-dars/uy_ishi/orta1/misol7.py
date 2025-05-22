A =int(input("son kiritng: "))
B =int(input("son kiritng: "))
for i in range (A, B + 1, 1):
    if i % 2 == 0:
        print(i * (-1), end = " ")
    else:
        print(i, end  = " ")