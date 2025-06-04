

with open("countries.txt", "w") as file:
    file.write("Italya Xitoy Fransiya Kanada Turkiya")

country = []
with open("countries.txt", "r") as file:
    country = file.read().split()


with open("capitals.txt", "w") as file:
    file.write("Rim Pekin Parij Ottava Anqara")

poytaxt = []
with open("capitals.txt", "r") as file:
    poytaxt = file.read().split()

with open("royxati.txt", "w") as file:
    for i in range(len(country)):
        file.write(f"{country[i]} - {poytaxt[i]}\n")