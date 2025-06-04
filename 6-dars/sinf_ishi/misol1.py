
def toq_yig(list):
    yig = 0
    for i in range (len(list)):
        if list[i] % 2 == 1:
            yig += list[i]
    return yig
           

list = [1, 2, 3,4, 5, 6, 7, 89]
print(toq_yig(list))

