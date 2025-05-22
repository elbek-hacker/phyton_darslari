yig = 0
for i in range(1, 500, 1):
    if i % 2 != 0:
        yig += i

print(yig)
yig1 = 0
a = yig
while yig != 0:
    yog1 = yig1 * 10 + yig % 10
    yig //= 10
if yig1 == a:
    print("Palindrom son")
else:
    print("Palindrom son emas")
