import json
with open("odamlar_resume.json", "r") as file:
    odamlar = json.load(file)
    for odam in odamlar:
        for experience in odam['work_experience']:
            if not experience['end_year']:
                experience['end_year'] = 2025
            davomiylik = experience['end_year'] - experience['start_year']
            print(f"| {odam['name'].center(30)} | {experience['company'].center(30)} | {str(davomiylik).center(4)} |")
            
