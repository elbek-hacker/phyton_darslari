son = int(input("son kiriting: "))
max_num = son % 10
while son != 0:
    if max_num < son % 10:
        max_num = son % 10
    son = son // 10
print(max_num)