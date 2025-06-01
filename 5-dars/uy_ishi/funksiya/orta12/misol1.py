
def raqamli_ildizi(n):
    yig = 0
    while n != 0:
        yig += n % 10
        n //= 10
    if yig > 9: 
        return raqamli_ildizi(yig)
    else:
        print(yig)
        return yig

raqamli_ildizi(45893)
