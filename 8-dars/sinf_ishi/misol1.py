
class Mahsulot:
    def __init__(self, narxi, soni, nomi):
        self.narxi = narxi
        self.__soni = soni
        self.nomi = nomi

    def set_soni(self, son):
        self.__soni += son
    
    def get_soni(self):
        return self.__soni
    
    def umumiy_narxi(self):
        return self.narxi * self.__soni
    

    def __str__(self):
        return(f"Nomi: {self.nomi}\n"
               f"Narxi: {self.narxi}\n"
               f"Soni: {self.__soni}")
    
mahsulot = Mahsulot(15000, 20, "olma")
son =5
print(mahsulot)
print(umumiy_narxi(son)) efvevg ergrwgre ergeg ergrew