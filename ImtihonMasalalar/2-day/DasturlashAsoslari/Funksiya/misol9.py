def yigindi(son):
    lst = []
    count = 0
    yig = 0
    while son != 0:
        count += 1
        yig += son%10
        son //= 10
        if count == 2:
            lst.append(str(yig))
            count = 0
            yig = 0
    if count == 1:
        lst.append(str(yig))
        
    lst.reverse()
    return ' '.join(lst)

son = 1234
natija = yigindi(son)
print(natija)