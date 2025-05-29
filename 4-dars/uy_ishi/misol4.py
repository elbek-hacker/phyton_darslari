
set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

set4 = (set1.intersection(set2)).difference(set3)
for i in set4:
    print(f'"{i}"', end = " ")