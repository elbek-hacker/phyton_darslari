def katta_harf(dict):
    for k in dict:
        dict[k] = dict[k].upper()
    return dict
print(katta_harf(dict = {"Ism": "Ali", "Familya": "Kamolov", "Manzil": "Angren shahri"}))