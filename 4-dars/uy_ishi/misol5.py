set1={4,5,6,7,8,9}	
set2={5,6,7,10,11}
set3=set1.symmetric_difference(set2)
set4=set1.intersection(set2)
yig1 = 0
for i in set3:
    yig1 += i
yig2 = 0
for i in set4:
    yig2 += i

print(yig1 - yig2)