
dictga  = lambda s: {"yil": int(s.split("-")[0]), "oy": int(s.split("-")[1]), "kun": int(s.split("-")[2])}

sana = "2020-02-15"
print(dictga (sana))