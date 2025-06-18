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
    def login(username, password):
        users = load(User.file_name)
        for user in users:
            if user['username'] == username:
                if user['password'] == password:
                    return username, user['role']  
                else:
                    print("Parol/login xato")
                    return None, None
        print("Bunday foydalanuvchi bazada yo'q")
        return None, None
        

    # CRUD
    @staticmethod
    def create(username, password):
        users = load(User.file_name)
        for user in users:
            if user['username'] == username:
                print("Bunday foydalanuvchi bazada bor")
                return None
        users.append( {"username": username, "password": password, "role": "user"})
        save(User.file_name, users)
        return username
    
    @staticmethod
    def read():
        return load(User.file_name)
    
    @staticmethod
    def read_one(username):
        users = load(User.file_name)
        for user in users:
            if user['username'] == username:                
                return user

    @staticmethod
    def update(username, password):
        users = load(User.file_name)

        for user in users:
            if username == user['username']:
                user['password'] = password
                users = save(User.file_name, users)
                return
        print("Bunday user topilmadi")
    
    @staticmethod
    def delete(username):
        users = load(User.file_name)
        for i, user in enumerate(users):
            if username == user['username']:
                print(i)
                # users.remove(user)
                del users[i]
                users = save(User.file_name, users)
                return
        
        print("Bunday user topilmadi")

def user_crud():
    habar = """
    Foydalanuvchi, amallaridan birini tanlang
        1. Ko'rish
        2. Kiritish
        3. O'zgaritrish
        4. O'chirish
        5. Chiqish
    """

    while True:
        tanlov = int(input(habar))

        match tanlov:
            case 1:    
                for user in User.read():
                    print(f"{user['username']}")
            case 2:
                username = input("Login kiriting")
                password = input("Parolni kiriting: ")
                User.create(username, password)
            case 3:
                username = input("O'zgartirmoqchi bo'lgan Loginni kiriting")
                password = input("Parolni kiriting: ")
                User.update(username, password)
            case 4:
                username = input("Qaysi loginni o'chirmoqchisiz?")
                User.delete(username)
            case 5:
                return