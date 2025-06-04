file = None
try:
    file = open("fayl1.txt", "w")
    royxat = ["Azizbek", "Elbek", "Rustam"]
    for i in royxat:
    
        file.write(i)
    
except FileNotFoundError:
    print("Fayl topilmadi")
finally:
    if file:
        file.close()
