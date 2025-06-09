dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
# 1-usul
dic1.update(dic2)
dic1.update(dic3)

print(dic1)
# 2-usul
natija = {**dic1, **dic2, **dic3}

print(natija)