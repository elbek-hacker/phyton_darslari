

class Mahsulot:
    def __init__(self, nomi, narxi, soni):
        self.nomi = nomi
        self.narxi = narxi
        self.soni = soni
    
    def ekranga_chiqar(self):
        print(f"Nomi: {self.nomi}\n"
              f"Narxi: {self.narxi}\n"
              f"Soni: {self.soni}")

mahsulot = Mahsulot("olma", 15000, 25)
mahsulot.ekranga_chiqar()