import json

def get_people():
    with open("odamlar_resume.json", "r") as file:
        return json.load(file)

def save_people(people):
    with open("odamlar_resume.json", "w") as file:
        json.dump(people,file,indent=4)

# Read
def read():
    with open("odamlar_resume.json", "r") as file:
        odamlar = json.load(file)
        print("_" * 40)
        print()
        print(f"|{'Ism familiya'.center(30)} | {'Yosh'.center(5)}|")
        print("_" * 40)
        for odam in odamlar:        
            print(f"|{odam['name'].center(30)} | {str(odam['age']).center(5)}|")
# Update        
def update():
    name = input("Kimni yoshini o'zgartirmoqchisiz")
    people = get_people()
    for person in people:
        if person['name'] == name:
            yosh = int(input("Yoshini kiriting"))
            person['age'] = yosh
            break
    save_people(people)

# Delete
def delete():
    name = input("Kimni o'chirmoqchisiz?: ")
    people = get_people()
    for person in people:
        if person['name'] == name:
            people.remove(person)
            break
    save_people(people)

# CRUD
# update()
delete()
