class HisobRaqami:

    def __init__(self, ism, balans):
        self.ism = ism
        self.balans = balans

    def pul_tushir(self, pul):
        if pul < 0:
            return print("Xatolik")
        self.balans += pul


    def pul_yechish(self, pul):
        if pul < 0:
            return print("Xatolik")
        elif pul > self.balans:
            return print("kop kiritildi")
        self.balans -= pul

    def ekranga(self):
        print(f"{self.ism} {self.balans}")
        

anvar = HisobRaqami("Anvar", 1_000_000)
anvar.pul_tushir(1000)
anvar.pul_yechish(12300)
anvar.ekranga()
# print(anvar.ekranga())