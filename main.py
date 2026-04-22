# 1
class EmployeeSalary:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase(self, percent):
        print(f"{self.salary + percent}")

    def show_salary(self):
        print(f"Salary: {self.salary}")


a = EmployeeSalary("bunyod", 100000000000000000000)
a.increase(.5)
a.show_salary()

# 2
class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, demage):
        self.health -= demage
        print(f"{self.name} zarar oldi: {demage} HP qoldi.")

    def heal(self, amount):
        self.health += amount
        print(f"Tiklandi: {amount} ")

a = GameCharacter("Bunyod", 100)
a.attack(90)
a.heal(100)

# 3
class Course:
    def __init__(self, title, students_count, capacity):
        self.title = title
        self.students_count = students_count
        self.capacity = capacity


    def enroll(self):
        if self.students_count == self.capacity:
            print("Joy yo‘q")
        else:
            print("Ro‘yxatdan o‘tdi")


a = Course("dlkxlk", 9, 10)
a.enroll()

# 4
class FileManager:
    def __init__(self, filename, is_open=False):
        self.filename = filename
        self.is_open = is_open

    def open_file(self):
        if self.is_open:
            print("Allaqachon ochiq")
        else:
            self.is_open = True
            print(f"{self.filename} ochildi")

    def close_file(self):
        if not self.is_open:
            print("Allaqachon yopiq")
        else:
            self.is_open = False
            print(f"{self.filename} yopildi")

a = FileManager("test.txt")
a.open_file()


# 5
class TaxiRide:
    def __init__(self, distance, price_per_km):
        self.distance = distance
        self.price_per_km = price_per_km

    def calculate_fare(self):
        self.total = self.distance * self.price_per_km
        print(f"Yo‘l narxi: {self.total} so'm")

    def apply_discount(self, percent):
        discount_price = self.total * (1 - percent / 100)
        print(f"Chegirmadan keyin: {int(discount_price)} so'm")


a = TaxiRide(10, 2500)
a.calculate_fare()
a.apply_discount(20)
