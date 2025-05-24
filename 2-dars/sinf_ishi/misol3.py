son = 5
hammasi = 11
ustun = 10
j = 0
for i in range(1,11):
    for j in range(1,hammasi//2+1):
        ustun += 1   
        print(f"{j} * {i} = {i * j}", end="\t")   
    print()
print()
for i in range(1,11):
    for j in range(hammasi//2+1, hammasi):
        ustun += 1   
        print(f"{j} * {i} = {i * j}", end="\t")
    print()
 