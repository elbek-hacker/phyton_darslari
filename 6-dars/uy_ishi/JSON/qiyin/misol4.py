import json
with open("odamlar_resume.json", "r") as file:
    odamlar = json.load(file)
    for odam in odamlar:
        for tugagan_yil in odam['work_experience']:
            if not tugagan_yil['end_year']:
                print(f"| {odam['name'].center(30)} |")
                break
