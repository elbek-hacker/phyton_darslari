class MyDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year
        self.Month = []
        self.day_in_month = []

    def isLeapYear(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    
    def isValidDate(self, day, month, year):
        pass

    def setDate(self, day, month, year):
        pass

    def findMaxMonth(self, month):
        if month > 12:
            return True
        else:
            return False
    def findMaxDayInMonth(self, month, year):
        if month == 1:
            return 31
        elif month == 2:
            if mydate.isLeapYear(self, year) is True:
                return 29
            else:
                return 28
        elif month == 3:
            return 31
        elif month == 4:
            return 30
        elif month == 5:
            return 31
        elif month == 6:
            return 30
        elif month == 7:
            return 31
        elif month == 8:
            return 31
        elif month == 9:
            return 30
        elif month == 10:
            return 31
        elif month == 11:
            return 30
        elif month == 12:
            return 31
    def nextDay(self):
        if self.__day + 1 > self.findMaxDayInMonth(self.__month, self.__year):
            if mydate.findMaxMonth() is True:
                print(f"{1}, {1}, {self.__year + 1}")
            else:
                print(f"{1}, {self.__month + 1}, {self.__year}")
        else:
            print(f"{self.__day + 1}, {self.__month}, {self.__year}") 
    def previousDay(self):
        if self.__day - 1 > 0:
            print(f"{self.__day - 1}, {self.__month}, {self.__year}")
    def nextMonth(self):
        pass
    def previousMonth(self):
        pass
    def nextYear(self):
        pass
    def previousYear(self):
        pass


mydate = MyDate(16, 6, 2025)
print(mydate)

not completed yet ! 