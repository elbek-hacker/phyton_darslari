son = int(input("son: "))
count = 0
while 1:
    if son % 2 == 0:
        count += 1
    elif son % 2 != 0:
        break
    son = son // 2
print(count)