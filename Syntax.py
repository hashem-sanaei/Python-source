# Python Syntax
import array as arr
print("Hello, World!")

# Python Comments
# This is a single-line comment

"""
This is a
multi-line comment
"""

# Python Variables
x = 5
y = "Hello"

# Python Data Types
# Numbers
a = 10
b = 3.14

# Casting
c = int(5.5)
d = float(3)

# Strings
name = "John Doe"
message = 'Python is awesome'

# Booleans
flag = True
is_false = False

# Python Operators
sum = 2 + 2
difference = 5 - 3
product = 4 * 6
quotient = 10 / 2

# Python Lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

# Python Tuples
person = ("John", 25, "New York")

# Python Sets
my_set = {1, 2, 3, 4, 5}

# Python Dictionaries
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
# Create an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary
my_dict["name"] = "John"
my_dict["age"] = 30
my_dict["city"] = "New York"

# Access values using keys
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30

# Modify values for existing keys
my_dict["age"] = 35
print(my_dict["age"])   # Output: 35

# Check if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary")

# Remove key-value pairs
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 35}

# Iterate over key-value pairs
for key, value in my_dict.items():
    print(key, ":", value)

# Output:
# name : John
# age : 35

# Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squared_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Python If...Else
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# Python While Loops
count = 0
while count < 5:
    print(count)
    count += 1

# Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits: # for(int i =0 ; i < 5 ; i++ ){}
    print(x)
for x in range(5):
    print(x)
    
# Python Functions


def greet(name):
    print("Hello, " + name + "!")

greet("Meli")  # Output: Hello, Meli!

def sum(a, b):
    print(a + b)

sum(2,3)  # Output: 5
# Python Arrays
numbers = arr.array('i', [1, 2, 3, 4, 5])

# Prompt the user for their name
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Prompt the user for their age
age = input("Enter your age: ")
age = int(age)  # Convert the input from string to integer
next_year_age = age + 1
print("Next year, you will be", next_year_age, "years old.")
