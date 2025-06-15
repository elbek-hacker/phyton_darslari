class Mahsulot:
    def __init__(self, nomi, narxi, soni):
        self.nomi = nomi
        self.narxi= narxi
        self.soni = soni

    def ekranga_chiqar(self):
        print(f"Nomi: {self.nomi}\nNarxi: {self.narxi}\nSoni: {self.soni}\n")


olma = Mahsulot("Olma", 15000, 3)
olma.ekranga_chiqar()
anor = Mahsulot("anor", 12_000, 8)
anor.ekranga_chiqar()