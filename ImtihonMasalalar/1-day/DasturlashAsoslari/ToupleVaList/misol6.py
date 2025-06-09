son = int(input("Son: "))

for i in range(1, son+1):
    yig = 0
    for j in range(1, i+1):
        yig += j
        print(j, end = "")
        if j < i:
            print(" + ", end = "")
        if j == i:
            print(f" = { yig }")
    
