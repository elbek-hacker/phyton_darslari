set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
set3 = set1.intersection(set2)
set4 = set1.difference(set2)
yig = 0
for j in set4:
    yig += j
yig1 = 0
for i in set3:
    yig1 += i
print(yig1 - yig)