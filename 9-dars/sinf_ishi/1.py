class Dorixona:
    
    def __init__(self, nomi: str, manzili: str) -> None:
        self.nomi = nomi
        self.manzil = manzili
        self.__dorilar = []
        self.__balans = 0 

    def dori_kirit(self, nomi, narxi, soni):
        assert isinstance(nomi, str), "Nomi satr bo'lishi kerak"
        assert isinstance(soni, (int, float)), "Soni int yoki float bo'lishi kerak"
        
        self.__dorilar.append({"nomi": nomi, "narxi": narxi, "soni": soni})
        print(f"{soni} dona {nomi} dori qo'shildi.")
    
    def olib_tashla(self, nomi):
        for dori in self.__dorilar:
            if nomi == dori['nomi']:
                self.__dorilar.remove(dori)

    def dorilar_malumoti(self):
        print("Dorilar ma'lumoti: ")
        for dori in self.__dorilar:
            print(f"{dori['nomi']} - {dori['narxi']} - {dori['soni']}")

    def dori_sot(self, nomi: str, soni: int):
        for dori in self.__dorilar:
            if dori['nomi'] == nomi:
                if dori['soni'] >= soni:
                    dori['soni'] -= soni
                    jami = soni * dori['narxi']
                    self.__balans += jami
                    print(f"{soni} dona {nomi} dori sotildi.")
                    print(f"Hisobga {jami} so'm qo'shildi. Jami: {self.__balans}")

                    if dori['soni'] == 0:
                        self.__dorilar.remove(dori)
                    return
                else:
                    print(f"{nomi} yetarli emas. {dori['soni']} qolgan.")
        print("Bazada yo'q")

    def narxini_ozgartir(self, nomi: str, narxi: int):
        for dori in self.__dorilar:
            if dori['nomi'] == nomi:
                dori['narxi'] = narxi
                return
        print(f"{nomi} dori zaxirada yo'q")
    
    def check_medicine_stock(self, nomi: str) -> int:
        for dori in self.__dorilar:
            if dori['nomi'] == nomi:
                return dori['soni']
        return 0
    # def total_medicines_value(self) -> float     to'liq bo'madi
dorixona = Dorixona(nomi="Shifokor Dorixonasi", manzili="Toshkent, O'zbekiston")
dorixona.dori_kirit(nomi="Paracetamol", narxi=2000, soni=50)
dorixona.dori_kirit(nomi="Ibuprofen", narxi=3000, soni=30)
# Output: 30 dona Ibuprofen dori qo'shildi.
# dorixona.dorilar_malumoti()
# dorixona.olib_tashla("Paracetamol")
# dorixona.dorilar_malumoti()
dorixona.narxini_ozgartir('Paracetamol', 5000)
dorixona.dorilar_malumoti()
print(dorixona.check_medicine_stock('Paracetamol'))