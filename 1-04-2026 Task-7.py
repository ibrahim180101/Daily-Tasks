'''
Task 1: Use super() properly 
Modify constructors so child classes reuse parent initialization. 
👉 Requirement: User should have name and id Student adds dept and fees Faculty adds salary TempFaculty adds duration 
👉 Expected: 
class Student(User): 
    def __init__(self, name, id, dept, fees): 
        super().__init__(name, id) 
        self.dept = dept 
        self.fees = fees
'''
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration


# Testing Task 1
s = Student("Arthur", "S101", "Artificial Intelligence", 75000)
f = Faculty("Dutch", "F201", 55000)
tf = TempFaculty("Sadie", "T301", 22000, 6)

print("Task 1 - super() Output:")
print(s.name, s.id, s.dept, s.fees)
print(f.name, f.id, f.salary)
print(tf.name, tf.id, tf.salary, tf.duration)


'''
✅ Task 2: Apply Abstraction Create an abstract base class. 
👉 Requirement: Create AbstractUser using ABC Add abstract method get_details() All child classes must implement it 
👉 Example expectation: 
from abc import ABC, abstractmethod 
class AbstractUser(ABC): 
    @abstractmethod 
    def get_details(self): 
        pass
'''
from abc import ABC, abstractmethod

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"User | Name: {self.name}, ID: {self.id}"

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student | Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty | Name: {self.name}, ID: {self.id}, Salary: {self.salary}"

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty | Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration} months"

# Sample Data

students = [
    Student("Arthur", "S101", "Artificial Intelligence", 75000),
    Student("John", "S102", "Data Science", 45000),
    Student("Charles", "S103", "Cyber Security", 60000),
    Student("Lenny", "S104", "Cloud Computing", 30000),
    Student("Micah", "S105", "Software Engineering", 90000),
]

faculty = [
    Faculty("Dutch", "F201", 55000),
    Faculty("Hosea", "F202", 28000),
    Faculty("Susan", "F203", 40000),
]


'''
✅ Task 3: Sorting using key Create a list of students and sort them. 
👉 Requirement: Sort students by fees Sort faculty by salary
👉 Example: students.sort(key=lambda x: x.fees)
'''

students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)


'''
✅ Task 4: Use map() Transform data. 
👉 Requirement: Extract only student names using map 
👉 Example: names = list(map(lambda s: s.name, students))
'''

names = list(map(lambda s: s.name, students))


'''
✅ Task 5: Use filter() Filter data. 
👉 Requirement: Get students with fees > 50000 Get faculty with salary > 30000 
👉 Example: high_fee_students = list(filter(lambda s: int(s.fees) > 50000, students))
'''

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))


'''
✅ Task 6: Use reduce() Aggregate data. 
👉 Requirement: Calculate total salary of all faculty Calculate total fees collected 
👉 Example: 
from functools import reduce 
total_fees = reduce(lambda acc, s: acc + int(s.fees), students, 0)
'''
from functools import reduce

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)



'''
✅ Task 7: Higher Order Function Create a function that accepts another function. 
👉 Requirement: Create function process_users(users, func) Apply any operation (map/filter) 
👉 Example: 
def process_users(users, func): 
    return list(map(func, users))
'''


def process_users(users, func):
    return list(map(func, users))


'''
🧪 Final Challenge (Important 🔥) 
👉 Build a mini system: 
Store multiple students & faculty in lists Print: 
All details (get_details()) 
Sorted data Filtered data Total fees & salary 
Use at least 3 functional programming concepts together

'''
all_users = students + faculty
print("                      FINAL CHALLENGE - MINI SYSTEM")
print("\n===== ALL DETAILS =====")
for user in all_users:
    print(user.get_details())


print("\nSorted Students by Fees:")
for s in sorted(students, key=lambda x: x.fees):
    print(f"{s.name} -> {s.fees}")


print("\nFiltered - High Fee Students (> 50000):")
for s in filter(lambda s: s.fees > 50000, students):
    print(f"{s.name} -> {s.fees}")


from functools import reduce

print("\nTotal Fees   :", reduce(lambda acc, s: acc + s.fees, students, 0))
print("Total Salary :", reduce(lambda acc, f: acc + f.salary, faculty, 0))