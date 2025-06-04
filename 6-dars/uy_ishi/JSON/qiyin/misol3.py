import json
with open("odamlar_resume.json", "r") as file:
    odamlar = json.load(file)
    konikma = input("ko'nikma kiriting: ")
    print()
    for odam in odamlar:
        for skill in odam['skills']:
            if konikma in skill:
                print(f"| {odam['name'].center(30)} |")
