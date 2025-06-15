class Cinema:
    def __init__(self, id: int, name: str, income: int):
        self.id = id
        self.name = name
        self.income = income
        self.movies = []

    def get_name(self):
        return self.name

    def addMovie(self, movie, seats):
        self.movies.append({"title": movie, "seat": seats})

    def sellTicket(self, movie, quantity, price):
        found = False
        for film in self.movies:
            if film['title'].lower() == movie.lower():
                found = True
                if film['seat'] >= quantity:
                    film['seat'] -= quantity
                    self.income += (quantity * price)
                    print("✅ Chiptalar muvaffaqqiyatli sotildi!")
                else:
                    print(f"{quantity} ta mavjud emas, {film['seat']} ta mavjud.")
                break
        if not found:
            print(f"{movie} is not available.")

    def checkAvailability(self, movie):
        for film in self.movies:
            if film['title'].lower() == movie.lower():
                if film['seat'] == 0:
                    return "Chiptalar tugagan."
                else:
                    return f"Mavjud o'rindiqlar soni: {film['seat']}"
        return f"Siz qidirayotgan {movie} movie mavjud emas."

    def check_available_movies(self):
        for film in self.movies:
            print(f"{film['title']}  {film['seat']}")

    def check_income(self):
        return f"{self.income} ming dollor$"


cinema = Cinema(12345, "The best movie center in Uzbekistan! located in Tashkent.", 0)

cinema.addMovie("Avatar", 30)
cinema.addMovie("Inception", 20)
cinema.addMovie("Persuit of happiness", 45)

print("Welcome to our majical CINEMA!")

while True:
    print("\nOptions:")
    print("[1] - Cinema haqida")
    print("[2] - Kino qo'shish")
    print("[3] - Chipta sotib olish")
    print("[4] - Mavjud filmlar")
    print("[5] - Mavjud o'rindiqlar")
    print("[6] - Chiqish")
    
    choice = input("Tanlang: ")
    if not choice.isdigit():
        print("Faqat raqam kiriting.")
        continue

    choice = int(choice)

    if choice == 1:
        print(cinema.get_name())

    elif choice == 2:
        movie = input("Kinoni nomini kiriting: ").strip()
        seats_input = input("Nechta o'rindiq mavjud: ")
        if seats_input.isdigit():
            seats = int(seats_input)
            cinema.addMovie(movie, seats)
            print("Muvaffaqqiyatli qo'shildi✅")
        else:
            print("Iltimos, o'rindiqlar sonini to'g'ri kiriting.")

    elif choice == 3:
        cinema.check_available_movies()
        movie = input("Tanlang: ").strip()
        orindiq = input("Qaysi o'rindiqni tanlaysiz?\n[1]-qator - 50.000 so'm\n[2]-qator - 40.000 so'm\n[3]-qator - 30.000 so'm\n")

        if orindiq not in ['1', '2', '3']:
            print("Noto'g'ri qatorda.")
            continue

        if orindiq == '1':
            price = 50000
        elif orindiq == '2':
            price = 40000
        else:
            price = 30000

        quantity_input = input("Nechta chipta sotib olasiz?: ")
        if quantity_input.isdigit():
            quantity = int(quantity_input)
            cinema.sellTicket(movie, quantity, price)
        else:
            print("Iltimos, chipta sonini raqam bilan kiriting.")

    elif choice == 4:
        cinema.check_available_movies()

    elif choice == 5:
        cinema.check_available_movies()
        tanlang = input("Film tanlang: ").strip()
        print(cinema.checkAvailability(tanlang))

    elif choice == 6:
        print("Rahmat!")
        break

    else:
        print("Noto'g'ri tanlov :)")
