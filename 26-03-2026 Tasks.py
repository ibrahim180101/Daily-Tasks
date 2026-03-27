'''
Task 1: User Info Manager (Functions + Dictionary) 
Create a function: def create_user(name, age, role): 
Return user as a dictionary 
Store multiple users in a list Print all users 
Add: 
Format names using .title()
'''
def c_user(name, age, role):
    user = {
        "name": name,  
        "age": age,
        "role": role
    }
    return user


users = []

users.append(c_user("ibrahim", 22, "developer"))
users.append(c_user("micheal", 30, "manager"))
users.append(c_user("trevor", 28, "tester"))

print("User List:")
for user in users:
    print(user)

'''
Task 2: Dynamic Calculator (*args) 
Create: def calculate_total(*numbers): 
Return sum of all numbers Accept unlimited inputs 
Bonus: Also return average
'''
def c_total(*numbers):
    total = sum(numbers)
    
    if len(numbers) == 0:
        average = 0
    else:
        average = total / len(numbers)
    
    return total, average

user_input = input("Enter numbers but leave space ")

numbers = list(map(int, user_input.split()))

total, avg = c_total(*numbers)

print("Total:", total)
print("Average:", avg)

'''
Task 3: Keyword Config System (**kwargs) 
Create: def system_config(**settings): 
Print all key-value pairs 
Example: mode: debug 
version: 1.0
'''
def syscon(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

# Example usage
syscon(mode="debug", version="1.0", user="admin")

'''
Task 4: Factorial Service (Recursion) 
Create: def factorial(n): 
Handle: n = 0 negative numbers (show error)
'''
def factorial(n):
    if n < 0:
        return "Error"
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Input
n = int(input("Enter number: "))
print("Result:", factorial(n))

'''
Task 5: Memory Optimization (Generator) Create: def square_generator(n): 
Yield squares instead of storing in list 
Compare: Normal list vs generator (print type)
'''
def sqgen(n):
    for i in range(n):
        yield i*i

lst = [i*i for i in range(5)]

gen = sqgen(5)

print("List:", lst)
print("Generator:", list(gen))

print(type(lst))
print(type(sqgen(5)))

'''
Task 6: Exception Handling Module 
Take input: numerator denominator Handle: divide by zero invalid input 
Always print: Program Completed
'''

try:
    N = int(input("Enter numerator: "))
    D = int(input("Enter denominator: "))
    
    result = N / D
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program Completed")

'''
Task 7: File Handling Create file: team_data.txt
Write user details into file Read and display content 
Bonus: Check if file is closed
'''

with open("team_data.txt", "w") as f:
    f.write("Name: Ibrahim\nAge: 22\nRole: Developer")

with open("team_data.txt", "r") as f:
    print(f.read())
    print("Closed:", f.closed)
    