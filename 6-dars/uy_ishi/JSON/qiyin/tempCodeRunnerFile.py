import json

# with open("odamlar_resume.json", "r", encoding="utf-8") as file:
#     odamlar = json.load(file)

# # Shahar nomlari bo‘yicha guruhlash uchun lug'at yaratamiz
# shahar_guruh = {}

# for odam in odamlar:
#     shahar = odam.get('city', "Noma'lum")  # Agar 'city' bo'lmasa, 'Noma'lum' deb olamiz
#     if shahar not in shahar_guruh:
#         shahar_guruh[shahar] = []
#     shahar_guruh[shahar].append(odam['name'])  # Shahar ostiga odamning ismini qo'shamiz

# # Natijani chiqamiz
# for shahar, ism_list in shahar_guruh.items():
#     print(f"Shahar: {shahar}")
#     print("Odamlar:")
#     for ism in ism_list:
#         print(f" - {ism}")
#     print()

