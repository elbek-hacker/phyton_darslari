import json

with open("odamlar_resume.json", "r") as file:
    print("_" * 75)
    print()
    print(f"|{'Ism Familiya'. center(31)} | {'Yosh'. center(4)} | {'Universitet'. center(30)} |")
    print("_" * 75)
    odamlar = json.load(file)
    for odam in odamlar:
        if odam['is_student']:
            print(f"| {odam['name'].center(30)} | {str(odam['age']).center(4)} | {odam['education']['university'].center(30)} |")
    print("_" * 75)