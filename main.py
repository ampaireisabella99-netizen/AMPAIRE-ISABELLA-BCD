print("hello world")
age = 20
print("age")
price = 12.7
print("price")

print(5+7)



# HELLO WORLD  (the print function)
print("Hello World")
print("Hello,", "Python", "learner!")

# COMMENTS
# A single-line comment starts with the # symbol
print("Comments are ignored by Python")  # A comment can also follow code

# VARIABLES  (names that store values)
name = "Anthony"
age = 22
print("Name:", name)
print("Age:", age)

# DATA TYPES  (int, float, str, bool)

price = 19.99
is_student = True
print("Types:", type(age), type(price), type(name), type(is_student))
print("Values:", age, price, name, is_student)

# TYPE CONVERSION
number_text = "50"
print("String to int:", int(number_text) + 10)
print("Int to string:", str(100) + " marks")
# OPERATORS  (arithmetic, comparison, logical)
a, b = 10, 3
print("Arithmetic:", a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
print("Comparison and logic:", a > b, a == b, (a > b) and (b > 5))

# STRINGS  (working with text
text = "data science"
print("Upper and title:", text.upper(), "|", text.title())
print("Slice and f-string:", text[0:4], "|", f"I love {text}")

# LISTS  (ordered, changeable collection
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("After append:", fruits)
fruits.remove("banana")
print("After remove:", fruits, "| first item:", fruits[0]
# TUPLES  (ordered, NOT changeable)
#
point = (4, 7)
print("Tuple:", point)
x, y = point
print("Unpacked: x =", x, ", y =", y)


# SETS  (unique items only)
numbers = {1, 2, 2, 3, 3, 3}
print("Set without duplicates:", numbers)
print("Set intersection:", {1, 2, 3} & {2, 3, 4})

# DICTIONARIES  (key : value paid)
student = {"name": "Anthony", "course": "Data Science"}
print("Read a value:", student["name"])
student["grade"] = "A"
print("After adding a pair:", student)


# CONDITIONAL STATEMENTS  (if / elif / else)

score = 72
if score >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"
print("Grade:", grade)


# FOR LOOP

for fruit in ["apple", "banana"]:
    print("Fruit:", fruit)

for i in range(1, 4):
    print("Number:", i)


# WHILE LOOPS

count = 1
while count <= 3:
    print("Count:", count)
    count += 1

total = 0
while total < 10:
    total += 4
print("Total:", total)


# BREAK AND CONTINUE

for n in range(1, 10):
    if n == 4:
        break
    print("Before break:", n)

for n in range(1, 6):
    if n == 3:
        continue
    print("Skipping 3:", n)


# FUNCTIONS  (reusable blocks of code)

def greet(person):
    return "Hello, " + person + "!"

def add(x, y=0):
    return x + y

print(greet("Anthony"))
print("Add:", add(5, 7), add(5))


# RECURSION  (a function that calls itself)

def factorial(n):
    if n == 0:  # base case stops the recursion
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Factorial of 5:", factorial(5))
print("Fibonacci of 7:", fibonacci(7))


# LAMBDA FUNCTIONS  (short one-line functions)

square = lambda n: n * n
print("Square of 6:", square(6))
print("Sorted by length:", sorted(["pear", "fig", "banana"], key=lambda w: len(w)))


# LIST COMPREHENSIONS  (build lists in one line)

print("Doubled:", [n * 2 for n in range(5)])
print("Even numbers:", [n for n in range(10) if n % 2 == 0])


# EXCEPTION HANDLING  (try / except)
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    int("abc")
except ValueError:
    print("That is not a valid number")
finally:
    print("Finally always runs")


# FILE HANDLING  (write and read files)

with open("sample.txt", "w") as file:
    file.write("Line one\nLine two\n")

with open("sample.txt", "r") as file:
    print("File content:", file.read().strip().replace("\n", " | "))


# MODULES AND IMPORTS

import math
print("Square root of 16:", math.sqrt(16))

import random
print("Random number:", random.randint(1, 10))


# CLASSES AND OBJECTS  (object-oriented programming)

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return self.name + " says Woof!"

class Puppy(Dog):
    def bark(self):
        return self.name + " says Yip!"

print(Dog("Rex").bark())
print(Puppy("Bobo").bark())

# USER INPUT  (input function)

user_name = input("Enter your name: ")
print("Welcome,", user_name)

user_age = int(input("Enter your age: "))
print("Next year you will be", user_age + 1)

