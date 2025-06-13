
class Karta:
    def __init__(self, nomi, raqami, muddati, balansi):
        self.nomi = nomi
        self.raqami = raqami
        self.muddati = muddati
        self.balansi = balansi

    def ekranga_chiqar(self):
        print(f"Nomi: {self.nomi}\n"
              f"Raqami: {self.raqami}\n"
              f"Muddati: {self.muddati}\n"
              f"Balansi: {self.balansi}\n")
        
karta = Karta("Milliy bank", 8600_9860_8600_9860, 12.27, 139_000_000)
karta.ekranga_chiqar()