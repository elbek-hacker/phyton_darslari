import json

with open("odamlar_resume.json", "r") as file:
    odamlar = json.load(file)
    for odam in odamlar:
        if odam['education']['graduation_year'] > 2020:
            print(f"{odam['name']}   {odam['education']['degree']}")
