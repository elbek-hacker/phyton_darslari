
class Library:
    def __init__(self, id: int, name: str):
        self.id = id
        self.__name = name
        self.books = []
        self.members = []

    def get_name(self):
        return self.__name
    
    def addBook(self, title: str, quantity: int):
        for book in self.books:
            if book['title'] == title:
                book['quantity'] += quantity
                break
        else:
            self.books.append({"title": title, "quantity": quantity})

    def lendBook(self, ism, title, son):
        for member in self.members:
            if member['ism'] == ism:
                if member['quantity'] >= son:
                    member['quantity'] = son
                    for book in self.books:
                        if book['title'] == title:
                            if book['quantity'] - son >= 0:
                                book['quantity'] -=son
                                break
                else:
                    print(f"{son} ta mavjud emas, {member['quantity']} ta mavjud")
                    break
        else:
            self.members.append({"ism": ism, "title": title, "quantity": son})
            for book in self.books:
                if book['title'] == title:
                    book['quantity'] -= son
                    # break

    def returnBook(self, member, title, son):
        for book in self.books:
            if title == book['title']:
                book['quantity'] += son
                for name in self.members:
                    if name['ism'] == member:
                        name['quantity'] -= son

    def ekranga_chiqar_books(self):
        for book in self.books:
            print(f"{book['title']}  {book['quantity']}")

    def ekranga_chiqar_members(self):
        for member in self.members:
            print(f"{member['ism']}  kitob: {member['title']}  {member['quantity']}")
library = Library(1, "Central Library")
library.addBook("Python Basics", 5)
library.addBook("Muqaddima", 12)
library.addBook("Ulamolar Nazdida Vaqtning Qadri", 8)
library.addBook("Python Basics", 4)
library.addBook("Ochlik", 12)
library.lendBook("Ali", "Python Basics", 4)
library.lendBook("Elbek", "Ochlik", 3)
library.returnBook("Ali", "Python Basics", 3)
library.returnBook("Elbek", "Ochlik", 2)
# library.ekranga_chiqar_members()
# print()
# library.ekranga_chiqar_books()
# print()
# print(library.get_name())
# print(library.addBook("Ochlik", 12))


# MAIN FUNKSIYA
print("==== Welcome to our national Library! ====")
while 1:
    print("\n==== MENU ====")
    button = int(input("Options: \n[1] - Information of the Library\n[2] - Available books\n[3] - Available members\n[4] - Lend book\n[5] - Return book\n[6] - Quit\n"))
    if button == 1:
        print(library.get_name())
    elif button == 2:
        library.ekranga_chiqar_books()
    elif button == 3:
        library.ekranga_chiqar_members()
    elif button == 4:
        ism = input("Your name?: ")
        title = input("Which book u want to get?: ")
        son = int(input(f"How many {title} book, u wanna get?: "))
        library.lendBook(ism, title, son)
        print("You are added to our Dear members✅!")
        print("Thanks for choosing our Libray :)")
    elif button == 5:
        member = input("Your name?: ")
        title = input("Which book u want to return?: ")
        son = int(input(f"How many {title} book, u wanna return?: "))
        print("Finished ✅!")
        print("Thanks for choosing our Libray :)")
    elif button == 6:
        print("Thanks for being with us :)")
        break