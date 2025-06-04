import json

with open("odamlar_resume.json", "r") as file:
    odamlar = json.load(file)
    print("_" * 70)
    print()
    print(f"| { 'Ism Familiya'.center(30)} | {'Darajasi'.center(30)} |")
    print("_" * 70)
    for odam in odamlar:
        if odam['education']['graduation_year'] > 2020:
            print(f"| {odam['name'].center(30)} | {odam['education']['degree'].center(30) } |")
    print("_" * 70)