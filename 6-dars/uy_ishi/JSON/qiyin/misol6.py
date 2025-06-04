import json

with open("odamlar_resume.json", "r") as file:
    print("_" * 75)
    print()
    print(f"|{'Ism Familiya'. center(31)} | {'Shahri'. center(20)} | {'Lavozimi'. center(30)} |")
    print("_" * 75)
    odamlar = json.load(file)
    for odam in odamlar:
        if odam['age'] >= 40:
            for experience in odam['work_experience']:
                if not experience['end_year']:
                    lavozimi = experience['position']
                    break
                else:
                    lavozimi = 'ishsiz'
            print(f"| {odam['name'].center(30)} | {str(odam['city']).center(20)} | {str(lavozimi).center(30)} |")
    print("_" * 75)