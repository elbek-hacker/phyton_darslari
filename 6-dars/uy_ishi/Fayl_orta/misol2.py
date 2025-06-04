import math 
sonlar = []
with open ("sonlar.txt", "r") as file:

    sonlar = file.read().split()

with open("ildiz.txt", "w") as file:
    for son in sonlar:
        ildiz = math.sqrt(float(son))

        file.write(f"{ildiz} ")