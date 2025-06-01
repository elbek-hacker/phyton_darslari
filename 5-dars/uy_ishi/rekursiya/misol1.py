
def yigindi(t):
    if not t:
        return 0
    
    if t[0] % 2 == 0:
        return t[0] + yigindi(t[1:])
    else:
        return yigindi(t[1:])
t = (2, 3, 5, 6, 3, 7, 8, 4)
print(yigindi(t))