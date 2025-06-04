file  = open("fayl1.txt", "r")
max = -4
for i in range (len(file.readlines())):
    if max < len((file.readlines())[i]):
        max = len(file.readlines[i])
print(max)

file.close()