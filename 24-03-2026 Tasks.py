'''
Mini Project 1: Employee Management System Concepts: Dictionary, List, Functions 
Build a system to manage employees. 
Requirements: Store multiple employees (list of dictionaries) 
Each employee: name, age, role, salary Add new employee Update employee details Delete employee Display all employees
'''
employees = []
def add_employee(name, age, role, salary):
    employees.append({
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    })

def update_employee(name, age=None, role=None, salary=None):
    for emp in employees:
        if emp["name"] == name:
            if age:
                emp["age"] = age
            if role:
                emp["role"] = role
            if salary:
                emp["salary"] = salary

def delete_employee(name):
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)

def display_employees():
    for emp in employees:
        print(emp)
#Example
add_employee("Alice", 30, "Developer", 70000)
add_employee("Bob", 25, "Designer", 60000)
add_employee("Tony",27,"HR",60000)
update_employee("Alice", salary=75000)
delete_employee("Bob")

display_employees()

'''
Mini Project 2: Student Report Card Concepts: Dictionary, Functions, Formatting 
Create a report system. Requirements: Store student name and marks (3 subjects)
Calculate total and average Print formatted report card Display grade based on average
'''
def create_report(name, m1, m2, m3):
    student = {
        "name": name,
        "marks": [m1, m2, m3]
    }

    total = sum(student["marks"])
    average = total / 3

    # Grade calculation
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Print report card
    print("Report Card")
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)


#usage
create_report("Ibrahim", 85, 78, 92)

'''
Mini Project 3: Shopping Cart 
System Concepts: List, Dictionary, Loop 
Simulate an online cart. 
Requirements: Add products (name, price, quantity) Calculate total bill 
Remove item from cart Display all items in formatted way
'''
cart = []

# Add product
def add_item(name, price, qty):
    cart.append({
        "name": name,
        "price": price,
        "qty": qty
    })

# Remove product
def remove_item(name):
    for item in cart:
        if item["name"] == name:
            cart.remove(item)

# Display cart
def show_cart():
    print("==> Cart Items ")
    for item in cart:
        print(item["name"], "-", item["price"], "x", item["qty"])

# Calculate total bill
def total_bill():
    total = 0
    for item in cart:
        total += item["price"] * item["qty"]
    print("Total Bill:", total)


#usage
add_item("Laptop", 50000, 1)
add_item("Mouse", 500, 2)
show_cart()
total_bill()
remove_item("Mouse")
show_cart()
total_bill()

'''
Mini Project 4: Login & User Validation 
Concepts: Dictionary, Condition 
Basic authentication system. 
Requirements: Store users (username & password) Take login input Validate credentials Print success or failure message
'''
# Store users (username: password)
users = {
    "admin": "1234",
    "ibrahim": "pass123",
    "guest": "guest"
}

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login Successful")
    else:
        print("Invalid Username or Password")

login()

'''
Mini Project 5: Unique Visitor Counter 
Concepts: Set 
Track unique visitors. 
Requirements: Store visitor names in a set Avoid duplicates Print total unique visitors

'''
visitors = set()

def add_visitor(name):
    visitors.add(name)

def show_visitors():
    print("Unique Visitors:", visitors)
    print("Total Unique Visitors:", len(visitors))


#usage
add_visitor("Ibrahim")
add_visitor("John")
add_visitor("Ibrahim")  # duplicate
show_visitors()

'''
Mini Project 6: String Formatter Tool 
Concepts: String Formatting 
Build a formatting utility. 
Requirements: Input name and product Display formatted sentence Show padded output (left, right, center)
'''
def formattool():
    name = input("Enter name: ")
    product = input("Enter product: ")
    print("{} bought {}".format(name, product))
    print("Left  :", name.ljust(12), product.ljust(12))
    print("Right :", name.rjust(12), product.rjust(12))
    print("Center:", name.center(12), product.center(12))



formattool()

'''
Mini Project 7: Bank Account System Concepts: Functions, Dictionary  
Simulate bank operations. 
Requirements: Create account (name, balance) Deposit money Withdraw money Check balance
'''
account = {}
def create_account(name, balance):
    account["name"] = name
    account["balance"] = balance

def deposit(amount):
    account["balance"] += amount


def withdraw(amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
    else:
        print("Insufficient balance")


def check_balance():
    print("Name:", account["name"])
    print("Balance:", account["balance"])


#usage
create_account("Ibrahim", 1000)
deposit(500)
withdraw(300)
check_balance()

'''
Mini Project 8: Voting System Concepts: Dictionary, Loop 
Count votes for candidates.
Requirements: Store candidates and votes Add vote Display winner
'''
votes = {
    "A": 0,
    "B": 0,
    "C": 0
}

def add_vote(candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        print("Invalid candidate")

def show_winner():
    winner = max(votes, key=votes.get)
    print("Votes:", votes)
    print("Winner:", winner)

#usage
add_vote("A")
add_vote("B")
add_vote("A")
add_vote("C")
add_vote("A")

show_winner()

'''
Mini Project 9: Course Enrollment System Concepts: List + Dictionary 
Manage student enrollments. 
Requirements: Add student with course list Update courses Display student details
'''
students = {}

def add():
    name = input("Name: ")
    course = input("Course: ")

    if name in students:
        students[name].append(course)
    else:
        students[name] = [course]

def show():
    for name, courses in students.items():
        print(name, courses)

def update():
    name = input("Name: ")
    if name in students:
        students[name] = [input("New course: ")]
    else:
        print("Not found")

add()
add()
show()
update()
show()

'''
Mini Project 10: Number Utility Tool Concepts: Functions, Formatting 
Work with numbers. 
Requirements: Convert number to binary, octal, hex Format large numbers with commas Print scientific notation
'''
def convert():
    n = int(input("Enter number: "))

    print("Binary:", n, "=", format(n, "b"))
    print("Octal :", n, "=", format(n, "o"))
    print("Hex   :", n, "=", format(n, "x"))

    print("Comma format:", f"{n:,}")
    print("Scientific  :", f"{n:.2e}")

convert()