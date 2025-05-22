#1dan Ngachan sonlarni juftlarini yigindisi
son = int ( input ( "son kiriting: " ) )
yig  = 0
for i in range (1, son, 1):
    if (i % 2 == 0):
        yig += i

print("yigindisi", yig)