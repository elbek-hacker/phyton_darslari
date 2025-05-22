#sonning necha xonali son ekanligi
son = int (input("son kiriting: "))
counter = 0
while son != 0:
    counter += 1
    son = son // 10
print(counter, "xonali")