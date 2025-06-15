class Karta:
    def __init__(self, __nomi, __raqami, __muddati, balansi):
        self.nomi = __nomi
        self.raqami = __raqami
        self.muddati = __muddati
        self.balansi = balansi

    @property
    def nomi(self):
        return self.__nomi
    @nomi.setter
    def nomi(self, qiymat):
        self.__nomi = qiymat

    @property
    def raqami(self):
        return self.__raqami
    @raqami.setter
    def raqami(self, qiymat):
        if len(qiymat) == 16:
            self.__raqami =qiymat
        else:
            print(f"{qiymat} karta raqam Xato!")

    @property
    def muddati(self):
        return self.__muddati
    @muddati.setter
    def muddati(self, qiymat):
        if qiymat > 2025:
            self.__muddati = qiymat
        else:
            print(f"{qiymat} sana xato")

    @property
    def balansi(self):
        return self.balansi
    @balansi.setter
    def balansi(self, qiymat):
        if qiymat > 0:
            self.balansi += qiymat
        else:
            print(f"{qiymat}. 0 dan katta qiymat kiriting!")

    def ekranga_chiqar(self):
        print(f"Nomi: {self.__nomi}\n"
              f"Raqami: {self.__raqami}\n"
              f"Muddati: {self.__muddati}\n"
              f"Balansi: {self.balansi}\n")

karta = Karta("Elbek", 9860_0101_8600_9860, 2028, 86_000_000)
# karta.ekranga_chiqar()
karta.muddati = 2024
print(karta.muddati)
