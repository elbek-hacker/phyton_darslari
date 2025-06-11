

class Car:
    def __init__(self, speed: int, time: int):
        self.__speed = speed
        self.__time = time

    def get_speed(self):
        return self.__speed
    def get_time(self):
        return self.__time
    

    def __str__(self):
        return f"{self.__speed * self.__time} km masofa bosib o'tgan."
    
car = Car(60, 2)
print(car)