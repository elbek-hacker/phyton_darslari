from users import User, user_crud
from products import Product

def admin_menu():
    while True:
        habar = """
    Admin panel
        1. Foydalanuvchi sozlamalari  
        2. Mahsulot qo'shish  
        3. Buyurtma    
        0. Chiqish
        """
        tanlov = 0
        while True:
            try:
                tanlov = int(input(habar))
                assert tanlov in range(1,6)
                break
            except:
                print("Xato. Qayta kiriting")
        if tanlov == 1:
            user_crud()
        elif tanlov == 2:
            name = input("Nomini kiriting: ")
            stock = int(input("Miqdorini kiriting: "))
            price = int(input("Narxini kiriting: "))
            category = input("Kategoriyasini kiriting: ")
            Product.mahsulot_qosh(name, stock, price, category)
        elif tanlov == 0:
            return

    

def menu():
    habar = """
    Bittasini tanlang:
        1. Kirish
        2. Ro'yxatdan o'tish
        3. Chiqish
    """
    while True:
        try:
            tanlov = int(input(habar))
            assert tanlov in [1,2,3]
            return tanlov
        except:
            print("Xato. Qayta kiriting")



while True:
    tanlov = menu()

    if tanlov == 1:
        username = input("Login kiriting:")
        password = input("Parolni kiriting:")
        username, role = User.login(username, password)
        if username:
            if role == "user":
                Product.user_menu()
            elif role == "admin":
                admin_menu()

    elif tanlov == 2:
        username = input("Login kiriting")
        password = input("Parolni kiriting: ")
        if User.create(username,password):
            print("Ro'yxatdan o'tdingiz")
    else:
        break
