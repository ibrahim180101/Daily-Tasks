'''# Section 1 Loops Basics
#1
for a in range(1,51):
    print(a)

#2
for b in range(2,101,2):
    print(b)

#3 
for c in range(1,101,2):
    print(c)

#4
for d in range(1,11):
    print(7 * d)

#5
num = 0
for e in range(1,101):
    num = num + e
print(num)

#6
for f in range(50,0,-1):
    print(f)

#7
count = 0
for g in range(3,101,3):
    count +=1
print(count)

#8
for h in range(1,11):
    print(h * h)

#9
for i in range(1,11):
    print(i ** 3)

#10
number = int(input("Enter the numbee"))
for j in range(1,number + 1):
    print(j)

#section 2 While loop
#11
k = 1
while k <= 20:
    print(k)
    k +=1

#12
L = int(input("Enter the number"))
fact = 1
while L > 0:
    fact *= L
    L -= 1
print(fact)

#13
M = int(input("Enter the number"))
reverse = 0
while M > 0:
    digit = M % 10
    reverse = reverse *10 + digit
    M //= 10
print(reverse)

#14
N = int(input("Enter the number"))
count = 0
while N > 0:
    N //= 10
    count += 1
print(count)

#15
while input() != "stop":
    print("continue")


# section 3 Nested loops
# 16
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

# 17
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 18
for i in range(1, 6):
    for j in range(1, 11):
        print(i*j, end=" ")
    print()

# 19
for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()

# 20
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()
'''
'''

# section 4 string basics
# 21
#builtin function
s = input()
print(len(s))

#using loop
S = input()
count = 0
for i in S:
    count += 1
print(count)


# 22
P = input().lower()
vowels = "aeiou"
vcount = 0
for i in P:
    if i in vowels:
        vcount += 1
print(vcount)

# 23
Q = input()
c_count = 0
for i in Q:
    if i.isalpha() and i not in vowels:
        c_count += 1
print(c_count)

# 24
R = input()
rev = ""
for i in R:
    rev = i + rev
print(rev)

# 25
if R == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
'''

# section 5 String Slicing 
s = "Happiness"
#26
print(s[:5])
#27
print(s[-3:])
#28
print(s[::-1])
#29
print(s[::2])
#30
print(s[1:-1])    


# section 6 List basics

#31
lst = [10,30,50,20,40]
print(sum(lst))
#32
print(max(lst))
#33
print(min(lst))
#34
print(len(lst))
#35
mylist = [10,30,50,20,40]
x = int(input("Enter :"))
if x in list:
    print("Found")
else:
    print("not found")

#section 7 list operations
#36
numbers =[10,50]
numbers.append(40)
numbers.append(30)
numbers.append(20)
print(numbers)

#37
numbers.insert(4,40)
print(numbers)

#38
numbers.remove(40)
print(numbers)

#39
reverssed = []
for i in numbers:
    reverssed =[i] + reverssed
print(reverssed)

#40
slist = numbers[:]
for i in range(len(slist)):
    for j in range(i + 1, len(slist)):
        if slist[i] > slist[j]:
            slist[i], slist[j] = slist[j], slist[i]
print(slist)