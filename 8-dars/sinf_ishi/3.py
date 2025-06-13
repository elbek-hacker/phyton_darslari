class Shape:
    def __init__(self, symbol, length):
        self.__symbol = symbol
        self.__length = length
    
    def get_symbol(self):
        return self.__symbol
    
    def set_symbol(self, symbol):        
        self.__symbol = symbol
    
    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        self.__length = length
    
    def show():
        pass

class Line(Shape):

    def show(self):
        print(self.get_symbol() * self.get_length())

class Triangle(Shape):

    def show(self):
        for i in range(1, self.get_length()+1):
            print(self.get_symbol() * i)

class tortburchak(Shape):

    def show(self):
        for i in range(1, self.get_length() + 1):
            print(self.get_symbol()*self.get_length())

line1 = Line("* ", 8)

t = Triangle("+", 10)

tortbur = tortburchak(" * ", 5)
tortbur.show()
shakllar = [line1,t]

for shakl in shakllar:
    shakl.show()
