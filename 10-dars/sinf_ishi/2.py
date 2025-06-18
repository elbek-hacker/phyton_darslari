class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            raise ValueError("Currency mismatch")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            raise ValueError("Currency mismatch")

    def __mul__(self, other):
        return self.amount * other.amount
    
    def __truediv__(self, other):
        return self.amount / other.amount
    
    def __floordiv__(self, other):  #bo'lib, butun qism oladi
        return self.amount // other.amount
    
    def __mod__(self, other): #qoldiq
        return self.amount % other.amount
    
    def __str__(self):
        return f"{self.amount} {self.currency}"

m1 = Money(100, "USD")
m2 = Money(200, "USD")
print(m1 % m2)