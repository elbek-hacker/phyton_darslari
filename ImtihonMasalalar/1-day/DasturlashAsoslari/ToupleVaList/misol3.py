list1=['salom',123,True,'Hayr','world',3.14,'7214']
Text = []
other = []
for i in list1:
    if isinstance(i, str):
        Text.append(i)
    else:
        other.append(i)

Text.sort()
other.sort(reverse = True)
print(Text)
print(other)