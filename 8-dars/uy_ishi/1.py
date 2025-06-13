
class Developer:
    def __init__(self, surname: str, position: str, salary: int):
        self.surname = surname
        self.position = position
        self.salary = salary

class SoftwareEngineer(Developer):
    def __init__(self, surname: str, position: str, salary: int, bonus: int, department: str):
        super().__init__(surname, position, salary)
        self.bonus = bonus
        self.department = department
    def total_payment(self):
        return self.salary + self.bonus
    
engineers = []

print("Ma'lumotlarni kiriting: ")
for i in range(5):
    data = input(f"{i+1}-dasturchi ma'lumotlari (familiya, lavozim, oylik, bonus, bo'lim): ").split()
    surname = data[0]
    position = data[1]
    salary = int(data[2])
    bonus = int(data[3])
    department = data[4]
    engineer = SoftwareEngineer(surname, position, salary, bonus, department)
    engineers.append(engineer)
# engineers = dict(engineers)
# for keys, value in engineers:
#     if 
dept_counts = {}
dept_sums = {}

for eng in engineers:
    dept = eng.department
    total = eng.total_payment()

    if dept not in dept_counts:
        dept_counts[dept] = 0
        dept_sums[dept] = 0

    dept_counts[dept] += 1
    dept_sums[dept] += total


print("\nNatija: ")
for dept in sorted(dept_counts.keys()):
    count = dept_counts[dept]
    summa = dept_sums[dept]
    print(f"{dept}: {count} ta dasturchi, jami to'lov: {summa}")
