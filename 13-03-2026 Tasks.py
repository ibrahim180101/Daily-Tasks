#Bitwise operator Tasks

#1
a= 10 
b =6
print(a & b)

#2
x = 12
y = 5
print(x | y)

#3
num = 8 
print(~num)

#4
A = 15 
B = 9
print(A ^ B)

#5
Num=7
print(Num << 2)

#6
numm = 20 
print(numm >> 1)
 
#7
R = int(input("Enter the Number"))
T = int(input("Enter the Number"))
print(R & T)

#8 
J = int(input("Enter the Number"))
K = int(input("Enter the Number"))
print(J ^ K)


#String Tasks

#9
print(" Hi " * 4)

#10
print(" Python " * 3)

#11
print("Super" + "Man")

#12
print("Hello"+" "+"World")

#13
Word = str(input("Enter the String"))
print(Word * 5)

#14
Word1 = str(input("Enter the String"))
Word2 = str(input("Enter the String"))
print(Word1 + Word2)



#Input and type casting Tasks

#15
name =input()
print("The Data Type is " ,type(name))

#16
age = int(input("Enter your Age"))
print(type(age))

#17
sum1 = int(input("Enter your Num"))
sum2 = int(input("Enter your Num"))
print("Total ",sum1 + sum2)

#18
Eng = int(input("Enter your marks"))
Sci = int(input("Enter your Marks"))
Avg = (Eng + Sci )/ 2
print("The Average is",Avg)

#19
inputnum1 = int(input("Enter your Num"))
inputnum2 = int(input("Enter your Num"))
sol = 3 * inputnum1 * 2 + inputnum2 -2
print(sol)

#20
Tcast = int(input("Enter your Num"))
print("Before Typecast",type(Tcast))
Tcast = str(Tcast)
print("After Typecast",type(Tcast))



#unit Digit tasks

#21
Ldigit ="12345"
print(Ldigit[-1])

#22
Udigit = 5007
print(Udigit % 10)

#23
Rdigit = 5678
print(Rdigit // 10)

#24
Sdigit = 7696
print((Sdigit // 10 ) % 10)

#25 
Last = 45678
print( Last % 10)


#if statement tasks

#26
if 10 >= 5:
    print(" 10 Greater than 5")

#27
gnum = int(input("Enter your Num"))
if gnum > 50:
    print(gnum," is greater than 50")

#28
Age = int(input("Enter your Age"))
if Age >= 18:
    print("Eligible")

#29
Gnum = int(input("Enter your Num"))
if Gnum > 100:
    print(Gnum," is greater than 100")

#30
pos = int(input("Enter your Num"))
if pos >= 0:
    print(pos," is a positive number")


#if else tasks

#31
Number = int(input("Enter your Num"))
Eonum = Number % 2
if  Eonum == 0:
    print(Number,"is a Even")
else:
    print(Number,"is a odd")

#32
Marks = int(input("Enter your score"))
if  Marks >= 35:
    print(" Passed")
else:
    print(" Failed")
#33
N = int(input("Enter your Num"))
if N >= 0:
    print(N," is a positive number")
else:
    print("its an Negative Number")

#34
I = int(input("Enter your Num"))
if I > 10:
    print("Bigger than  10")
else:
    print("Lesser than 10")


#Nested if tasks

#35 
Age = int(input("Enter your Age"))
Height = int(input("Enter your height"))
weight = int(input("Enter your Weight"))

if Age >= 18:
    if Height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejeected low Weight")
    else:
        print("Rejected low Height")        
else:
    print("Rejected below age")

#36
Marks = int(input("Enter your Marks"))
age = int(input("Enter your Age"))
if Marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Admission canceled because of age")
else:
    print("Admission canceled because of marks")

#37
Agee = int(input("Enter your Age"))
height = int(input("Enter your height"))
weight = int(input("Enter your Weight"))

if Agee >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejeected low Weight")
    else:
        print("Rejected low Height")        
else:
    print("Rejected below age")


#Match Statement Tasks
#38
days = int(input("Enter the number 1 - 7:"))
match days:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
#39 
color = int(input("Enter number between 1 - 3: "))
match color:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")

#40
Fruit = int(input("Enter number between 1 - 4: "))
match Fruit:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")