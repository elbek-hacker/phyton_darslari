

class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    
    
    def get_quarter(self):
        if self.__x > 0 and self.__y > 0:
            return 1
        elif self.__x < 0 and self.__y > 0:
            return 2
        elif self.__x < 0 and self.__y < 0:
            return 3
        elif self.__x > 0 and self.__y < 0:
            return 4
    
    def __str__(self):
        return f"{self.get_quarter()} - chorak"


x, y = int(input("x-son: ")), int(input("y-son: "))

point = Point(x, y)
print(point)