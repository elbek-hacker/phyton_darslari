from math import pi



class Aylana:

    def __init__(self, radius, rangi):
        self.__radius = radius
        self.__rangi = rangi

    # o'qish
    def get_radius(self):
        return self.__radius
    def get_rangi(self):
        return self.__rangi
    def set_rangi(self, rangi):
        assert isinstance(rangi, str), "Qiymat string bo'lishi kerak"
        self.__rangi = rangi
    def yuzini_top(self):
        return pi * self.__radius**2
    # yozish
    def set_radius(self, radius):
        # if isinstance(radius,(int,float)):
        #     self.__radius = radius
        # else:
        #     raise TypeError("Qiymat int yoki float bo'lishi kerak")
        assert isinstance(radius,(int,float)), "Qiymat int yoki float bo'lishi kerak"
        self.__radius = radius

    def __str__(self):
        return f"{self.__radius} {self.rangi}"
    
    

aylana1 = Aylana(10, "oq")

print(aylana1.rangi)
print(aylana1)
