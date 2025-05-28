list1=['salom',123,True,'Hayr','world',3.14,'7214']
TEXT = []
OTHER = []
for i in range (len(list1)):
    if type(list1[i]) == str:
        TEXT.append(list1[i])
    else:
        OTHER.append(list1[i])
TEXT.sort()
OTHER.sort()
OTHER.reverse()
print(TEXT)
print(OTHER)