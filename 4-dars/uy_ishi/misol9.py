set1={2,3,4,5,6}
set2={4,5,6,7,8,9}

set3 = set1.symmetric_difference(set2)
yig = 0
for i in set3:
    yig += i

print(yig)