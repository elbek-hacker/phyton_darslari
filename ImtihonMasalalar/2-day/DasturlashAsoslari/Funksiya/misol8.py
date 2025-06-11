def isAnagram(soz1, soz2):
    for i in range(len(soz1)):
        if soz1[i] not in soz2:
            return False
    return True

soz1 = 'anagram'
soz2 = 'nagaram'
natija = isAnagram(soz1, soz2)
print(natija)