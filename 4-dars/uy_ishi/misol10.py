set1={100, 20, 45, 80, 70, 50}
set2={30, 55, 70, 60, 32, 100}

for i in set(set1):
    if i < 60:
        set1.discard(i)

for i in set(set2):
    if i < 60:
        set2.discard(i)

set3 = set1.intersection(set2)

yig = 0
for i in set3:
    yig += i
print(yig // len(set3))