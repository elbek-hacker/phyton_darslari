# from abc import ABC, abstractmethod  # ABC modulidan foydalanamiz

# class Hayvon(ABC):  # Hayvon sinfi, abstrakt
#     @abstractmethod
#     def ovoz(self):  # Abstrakt metod
#         pass  # Bu yerda hech qanday kod yo'q, aniq sinflar tomonidan amalga oshiriladi

# class It(Hayvon):  # It sinfi, Hayvon sinfidagi aniq realizatsiya
#     def ovoz(self):
#         return "Barking"

# class Mushuk(Hayvon):  # Mushuk sinfi, Hayvon sinfidagi aniq realizatsiya
#     def ovoz(self):
#         return "Meowing"

# # Obyektlar yaratish
# it = It()
# mushuk = Mushuk()

# print(f"It ovozi: {it.ovoz()}")  # It ovozi: Barking
# print(f"Mushuk ovozi: {mushuk.ovoz()}")  # Mushuk ovozi: Meowing
from abc import ABC, abstractmethod

class ovoz(ABC):
    @abstractmethod
    def ovozi(self):
        pass
class It(ovoz):
    def ovozi(self):
        return "barking"
    
class Mushuk(ovoz):
    def ovozi(self):
        return "myawing"
    
class Cow(ovoz):
    def ovozi(self):
        return "cow ovozi"
    
it = It()
mushuk = Mushuk()
cow = Cow()

print(f"It ovozi: {it.ovozi()}")
print(f"Mushuk ovozi: {mushuk.ovozi()}")
print(f"Cow ovozi: {cow.ovozi()}")