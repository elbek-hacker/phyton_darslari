def raqamgacha_yigindi(son):
    yig  = 0
    for i in range (1, son + 1):
        yig += i
    
    return yig

print(raqamgacha_yigindi(son = int(input("son kiriting: "))))
