

class Time:
    def __init__(self, soat: int, minut: int, sekund: int):
        self.__soat = soat
        self.__minut = minut
        self.__sekund = sekund

    def get_soat(self):
        return self.__soat
    def get_minut(self):
        return self.__minut
    def get_sekund(self):
        return self.__sekund
    
    def time_left(self):
        self.__soat = 24 - self.__soat
        self.__minut = 60 - self.__minut
        self.__sekund = 60 - self.__sekund
        return self.__soat, self.__minut, self.__sekund
    
    def add_minutes(self):
        self.__minut += 100
        if self.__minut > 60:
            self.__soat += 1
            self.__minut -= 60
        if self.__minut > 60:
            self.__soat += 1
            self.__minut -= 60

        return self.__soat, self.__sekund
    def __str__(self):
        self.time_left()
        print(f"24:00:00 gacha qolgan vaqt: \n{self.__soat}:{self.__minut}:{self.__sekund} qoldi.")
        self.add_minutes()
        return f"100 daqiqa qo'shgandan keyin: \n{self.__soat}:{self.__minut}:{self.__sekund} qoldi."
    
soat, minut, sekund = int(input("Soat: ")),  int(input("Minut: ")),  int(input("Sekund: "))
time = Time(soat, minut, sekund)
print(time)