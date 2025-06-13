
class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    
    def set_address(self, yangi_manzil):
        self.__address = yangi_manzil

    def __str__(self):
        return (f"Ism: {self.__name}\nManzil: {self.__address}\nYangi manzili: {self.__address}")
    
class Student(Person):
    def __init__(self, name, address, courses=[], grades=[]):
        super().__init__(name, address)
        self.courses = courses
        self.grades = grades
    def add_course_grade(self, courses: str, grades: int):
        self.courses.append(courses)
        self.grades.append(grades)
        return self.courses, self.grades
    def print_grades(self):
        return f"Kurslar: {self.courses}\nBaholar: {self.grades}"
    def get_average_grade(self):
        return sum(self.grades) // len(self.courses)
    def __str__(self):
        return f"O'rtacha bahosi: {self.get_average_grade()}"

person = Student("otabek", "yangihayot", ["math", "english"], [4, 5])
print(person)
person.set_address("Chilonzor")
person.add_course_grade(["math", "english"], [4, 5])
print(person)