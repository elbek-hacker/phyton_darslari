matn = input("son kiriting: ")
soz = input("soz kiriting: ")

matn1 = matn.split()
matn2 = []
for i in range (len(matn1)):
   a = soz + matn1[i]
   matn2.append(a)

print(matn2)
