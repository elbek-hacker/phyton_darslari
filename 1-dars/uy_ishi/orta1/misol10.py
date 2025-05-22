A =int(input("son kiritng: "))
B =int(input("son kiritng: "))
j = -1
farq = 0
if A % B != 0:
    for i in range(1, A, B):
        j += 1
    farq = A - B * j
    print(f'''A kesmada {j} ta B bor
    Bo'sh qismi {farq}''')
else:
    j = A // B
    print(f'''A kesmada {j} ta B bor
    Bo'sh qismi {farq}''')