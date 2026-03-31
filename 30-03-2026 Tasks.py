#Task 1: Encapsulation(user class)
#create class user with propetr encapsulatipon
class User1:
    def set_user(self, user_name, pwd):
        self.__user_name = user_name # private attribute
        self.__pwd = pwd # private attribute

    def get_user(self):
        return self.__user_name  # returns username, hides password

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


u1 = User1()
u1.set_user("ibrahim", "pass123")
print(u1.get_user()) 
u1.register() # Registering user
u1.login() # Logging in


#Task 2: Inheritance(user -> student,Faculty)

class User2:
    def __init__(self, name):
        self.name = name

    def register(self):
        print(f"Registering user: {self.name}")

    def login(self):
        print(f"Logging in: {self.name}")


class Student(User2):
    def student_greet(self):
        print("Hello Student")


class Faculty(User2):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty): # Multilevel inheritance
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


student = Student("Brock")
faculty = Faculty("Vince")
temp = TempFaculty("Paul")

# Child can access parent methods
student.register()
student.login()
student.student_greet()

faculty.register()
faculty.login()
faculty.faculty_greet()

temp.register() # inherited from User (via Faculty)
temp.login() # inherited from User (via Faculty)
temp.faculty_greet() # inherited from Faculty
temp.tempFaculty_greet() # own method


#Task 3: Method Overriding
class User3:
    def greet(self):
        print("Welcome User")


class Student3(User3):
    def greet(self): # overrides parent greet
        print("Welcome Student")


class Faculty3(User3):
    def greet(self): # overrides parent greet
        print("Welcome Faculty")


base_user = User3()
student3 = Student3()
faculty3 = Faculty3()

base_user.greet() # Welcome User
student3.greet() # Welcome Student
faculty3.greet() # Welcome Faculty

#Task 4: Method Chaining
class User4:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


user4 = User4()
user4.login().greet().register()


#Task 5: Combined Mini User System
class UserFull:
    users_count = 0 

    def __init__(self):
        UserFull.users_count += 1 

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"registered: {self.__user_name}")
        return self

    def login(self):
        print(f"logined: {self.__user_name}")
        return self

    def greet(self):
        print("Welcome User")
        return self


class StudentFull(UserFull):
    def greet(self): # method overriding
        print("Welcome Student")
        return self

    def student_greet(self):
        print("Hello Student")


class FacultyFull(UserFull):
    def greet(self): # method overriding
        print("Welcome Faculty")
        return self

    def faculty_greet(self):
        print("Hello Faculty")


# Create objects (users_count increments automatically)
s1 = StudentFull()
s1.set_user("Peter", "pass1")
s2 = StudentFull()
s2.set_user("bruce", "pass2")

f = FacultyFull()
f.set_user("Tony Stark", "pass2")

# Method chaining
s1.login().greet().register()
s2.login().greet().register()


f.login().greet().register()



print(f"Total users created: {UserFull.users_count}") 