import json


def load(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        with open(file_name, "w") as file:
            json.dump([], file)
        return []

def save(file_name, lst):
    with open(file_name, "w") as file:
        return json.dump(lst, file, indent=4)
        



class User:
    file_name = "users.json"

    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role

    
    # CRUD
    @staticmethod
    def create(username, password):
        users = load(User.file_name)
        users.append( {"username": username, "password": password, "role": "user"})
        save(User.file_name, users)
    
    @staticmethod
    def read():
        return load(User.file_name)

    @staticmethod
    def update(username, password):
        users = load(User.file_name)
        for user in users:
            if username == user['username']:
                user['password'] = password

                return
        print("Bunday user topilmadi")
    
    @staticmethod
    def delete(username):
        users = load(User.file_name)
        for user in users:
            if username == user['username']:
                users.remove(user)
                print("Foydalanuvchi o'chirildi")
                save(User.file_name, users)
                return
        
        print("Bunday user topilmadi")


# User.create("Anvar","123")
# User.create("Jasur","123")
# User.create("Otabek","123")

# User.update("Anvar", "1")
# User.delete("Anvar")
# print(User.read())
User.delete("Anvar")
# User.file_name
