

class Vaqt:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def get_day(self):
        return self.__day
    def get_month(self):
        return self.__month
    def get_year(self):
        return self.__year
    
    def __str__(self):
        return f"{self.__day}  {self.__month}  {self.__year}"
    
vaqt = Vaqt(10, 3, 2025)
print(vaqt)