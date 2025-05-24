import random

count_t = 0
count_n = 0
for i in range (5, 0, -1):
    son1, son2 = random.randint(1, 10), random.randint(1, 10)
    print(f"{i} - savol")
  
    togri = son1 * son2
    javob = int(input(f"{son1} * {son2} = "))
    if javob == togri:
        print("togri topdingiz")
        count_t += 1
    else:
        print("notogri javob")
        count_n += 1
print(f'''to'g'ri javoblar soni: {count_t}
noto'g'ri javoblar soni: {count_n}''')