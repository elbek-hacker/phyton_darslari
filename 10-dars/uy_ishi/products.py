import json
from users import User
def load(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        with open(file_name, 'w') as file:
            json.dump([], file)
            return []
def save(file_name, lst):
    with open(file_name, 'w') as file:
        json.dump(lst, file, indent = 4)
    
class Product:
    file_name = "products.json"
    def __init__(self, name, stock: int, price: int, category):
        self.name = name
        self.stock = stock
        self.price = price
        self.category = category
        self.savat = []

    @staticmethod
    def mahsulot_qosh(name, stock, price, category):
        products = load(Product.file_name)
        for product in products:
            if product['name'] == name:
                product['stock'] = int(product['stock']) + stock
                product['price'] =  price
                print("Mahsulot Mavjud, soni oshirildi, narxi yangilandi.")
                save(Product.file_name, products)
                return
        products.append({"name": name, "stock": stock, "price": price, "category": category})
        print("Muvaffaqqiyatli qo'shildi:)")
        save(Product.file_name, products)
        return

    @staticmethod
    def mahsulotlarni_korish():
        return load(Product.file_name)
    
    @staticmethod
    def mahsulot_qidirish(name):
        products = load(Product.file_name)
        for product in products:
            if product['name'].lower() == name.lower():
                print(f"{product['name']} | {product['price']} so'm | {product['stock']} dona | {product['category']}")
                return
        print("Bunday mahsulot mavjud emas")

    @staticmethod
    def mahsulotlarni_filtirlash(category):
        products = load(Product.file_name)
        found = False
        for product in products:
            print(f"{category} kategoriyasidagi maxsulotlar:")
            if product['category'].lower() == category.lower():
                print(f"{product['name']} | {product['price']} so'm | {product['stock']} dona")
                found = True
        if not found:
            print("Bunday kategoriya mavjud emas!")


    def user_menu():
        habar = """
        Amallardan birini tanlang:
            1. Mahsulotni ko'rish 
            2. Mahsulot qidirish
            3. Mahsulotni filtrlash
            4. Savatchaga qo'shish
            5. Savatchani ko'rish (Har biri va Jami mahsulot summasi)
            6. Savatchadan o'chirish
            7. Profil
            0. Chiqish
        """
        savat = []
        while True:
            print(habar)
            tanlov = input("Tanlovingizni kiriting: ").strip()
            
            if tanlov == '1':
                products = Product.mahsulotlarni_korish()
                for i in products:
                    print(f"Nomi: {i['name']}, Miqdori: {i['stock']}, Narxi: {i['price']}, Kategproyasi: {i['category']}")
            
            elif tanlov == '2':
                name = input("Qaysi mahsulotni qidiryapsiz: ")
                Product.mahsulot_qidirish(name)

            
            elif tanlov == '3':
                category = input("Qaysi kategoriyadagi mahsulotni qidiryapsiz: ")
                Product.mahsulotlarni_filtirlash(category)
            
            elif tanlov == '4':
                name = input("Qaysi mahsulotni savatga qo'shmoqchisiz? ")
                for product in products:
                    if product['name'].lower() == name.lower():
                        savat.append(product)
                        print(f"{product['name']} savatga qo'shildi.")
                        break
                else:
                    print("Bunday mahsulot topilmadi.")
            
            elif tanlov == '5':
                if not savat:
                    print("🛒Savat hozircha bo'sh:)")
                else:
                    print("Savatdagi mahsulotlar:")
                    jami_summa = 0
                    for product in savat:
                        print(f"Nomi: {product['name']}, Miqdori: {product['stock']}, Narxi: {product['price']}, Kategoriyasi: {product['category']}")
                        jami_summa += product['price']
                    print(f"💰Jami summa: {jami_summa} ming so'm")
            elif tanlov == '6':
                name = input("Qaysi mahsulotni savatchadan o'chirmoqchisiz? ")
                for product in savat:
                    if product['name'].lower() == name.lower():
                        savat.remove(product)
                        print(f"{name} savatchadan o'chirildi.")
                        break
                else:
                    print("Bunday mahsulot savatchada yo'q.")

            elif tanlov == '7':
                # User.read_one()
                print("Profil funksiyasi ishlamayapti (keyin yoziladi).")
            
            elif tanlov == '0':
                print("Dasturdan chiqilmoqda...\nBizni tanlaganingiz uchun Rahmat:)")
                return
            
            else:
                print("Xato! Iltimos, 0 dan 7 gacha bo'lgan raqamni tanlang.")
