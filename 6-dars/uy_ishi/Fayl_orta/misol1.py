
from random import randint
with open("sonlar.txt", "w") as file:
    for i in range (10):
        son = randint(1, 11)
        file.write(f"{son} " )