"""
COMPREHENSIVE PYTHON BASICS REFERENCE
This file covers all fundamental Python syntax, features, and common patterns.
"""

# ============================================================================
# 1. VARIABLES AND DATA TYPES
# ============================================================================

# Variables (no declaration needed, dynamically typed)
x = 10                      # Integer
y = 3.14                    # Float
name = "Python"             # String
is_active = True            # Boolean
nothing = None              # NoneType

# Type checking and conversion
print(type(x))              # <class 'int'>
age = int("25")             # String to integer
price = float("9.99")       # String to float
text = str(123)             # Integer to string

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0               # Same value to multiple variables

# ============================================================================
# 2. NUMERIC OPERATIONS
# ============================================================================

# Basic arithmetic
addition = 5 + 3            # 8
subtraction = 5 - 3         # 2
multiplication = 5 * 3      # 15
division = 5 / 2            # 2.5 (float division)
floor_division = 5 // 2     # 2 (integer division)
modulo = 5 % 2              # 1 (remainder)
exponent = 2 ** 3           # 8 (2^3)

# Augmented assignment
x = 10
x += 5                      # x = x + 5 (works with -, *, /, //, %, **)
x -= 3
x *= 2
x /= 4

# Built-in math functions
abs_val = abs(-5)           # 5
rounded = round(3.7)        # 4
max_val = max(1, 5, 3)      # 5
min_val = min(1, 5, 3)      # 1
power = pow(2, 3)           # 8

# ============================================================================
# 3. STRINGS
# ============================================================================

# String creation
single = 'Hello'
double = "World"
multi_line = """This is
a multi-line
string"""
raw_string = r"C:\new\folder"  # Raw string (ignores escape sequences)

# String concatenation and repetition
full = single + " " + double    # "Hello World"
repeated = "Ha" * 3             # "HaHaHa"

# String indexing and slicing
text = "Python"
first = text[0]                 # 'P' (0-indexed)
last = text[-1]                 # 'n' (negative indexing from end)
substring = text[1:4]           # 'yth' (start:end, end exclusive)
start_slice = text[:3]          # 'Pyt' (from beginning)
end_slice = text[3:]            # 'hon' (to end)
step = text[::2]                # 'Pto' (every 2nd character)
reverse = text[::-1]            # 'nohtyP' (reverse string)

# String methods
upper = text.upper()            # 'PYTHON'
lower = text.lower()            # 'python'
capitalized = text.capitalize() # 'Python'
title = "hello world".title()   # 'Hello World'

# String formatting
name = "Alice"
age = 25
# Old style
formatted1 = "Name: %s, Age: %d" % (name, age)
# str.format()
formatted2 = "Name: {}, Age: {}".format(name, age)
formatted3 = "Name: {n}, Age: {a}".format(n=name, a=age)
# f-strings (Python 3.6+, preferred)
formatted4 = f"Name: {name}, Age: {age}"
formatted5 = f"Calculation: {10 + 5}"

# String methods (continued)
stripped = "  hello  ".strip()     # 'hello' (remove whitespace)
split_list = "a,b,c".split(",")    # ['a', 'b', 'c']
joined = "-".join(['a', 'b', 'c']) # 'a-b-c'
replaced = "hello".replace("l", "L") # 'heLLo'
found = "hello".find("ll")         # 2 (index of substring, -1 if not found)
contains = "ll" in "hello"         # True
starts = "hello".startswith("he")  # True
ends = "hello".endswith("lo")      # True
count = "hello".count("l")         # 2

# ============================================================================
# 4. LISTS (Mutable, ordered collections)
# ============================================================================

# List creation
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]

# List operations
numbers.append(6)               # Add to end: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)            # Insert at index: [0, 1, 2, 3, 4, 5, 6]
numbers.extend([7, 8])          # Add multiple: [0, 1, 2, 3, 4, 5, 6, 7, 8]
removed = numbers.pop()         # Remove and return last: 8
numbers.remove(0)               # Remove first occurrence of value
del numbers[0]                  # Delete by index

# List methods
numbers = [3, 1, 4, 1, 5]
numbers.sort()                  # Sort in place: [1, 1, 3, 4, 5]
numbers.reverse()               # Reverse in place: [5, 4, 3, 1, 1]
sorted_new = sorted(numbers)    # Return new sorted list (original unchanged)
reversed_new = list(reversed(numbers))  # Return new reversed list

# List operations (continued)
length = len(numbers)           # Get length
index = numbers.index(4)        # Get index of first occurrence
count = numbers.count(1)        # Count occurrences
numbers.clear()                 # Remove all elements

# List slicing (same as strings)
nums = [0, 1, 2, 3, 4, 5]
sub = nums[1:4]                 # [1, 2, 3]
every_other = nums[::2]         # [0, 2, 4]
reversed_list = nums[::-1]      # [5, 4, 3, 2, 1, 0]

# List unpacking
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5

# ============================================================================
# 5. TUPLES (Immutable, ordered collections)
# ============================================================================

# Tuple creation
empty_tuple = ()
single = (1,)                   # Note the comma for single element
coordinates = (10, 20)
mixed_tuple = (1, "hello", 3.14)

# Tuple operations (limited because immutable)
x, y = coordinates              # Unpacking
length = len(coordinates)
first = coordinates[0]
# coordinates[0] = 15           # ERROR: tuples are immutable

# Tuple benefits: faster than lists, can be used as dict keys
point = (3, 4)
# my_dict = {point: "location"}  # Valid

# ============================================================================
# 6. SETS (Unordered, unique elements)
# ============================================================================

# Set creation
empty_set = set()               # Note: {} creates empty dict, not set
numbers_set = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3])   # {1, 2, 3} - duplicates removed

# Set operations
numbers_set.add(6)              # Add element
numbers_set.remove(1)           # Remove (raises error if not found)
numbers_set.discard(10)         # Remove (no error if not found)
popped = numbers_set.pop()      # Remove and return arbitrary element
numbers_set.clear()             # Remove all elements

# Set operations (mathematical)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union = a | b                   # {1, 2, 3, 4, 5, 6}
intersection = a & b            # {3, 4}
difference = a - b              # {1, 2} (in a but not in b)
symmetric_diff = a ^ b          # {1, 2, 5, 6} (in either but not both)

# Set comparisons
is_subset = {1, 2} <= {1, 2, 3} # True
is_superset = {1, 2, 3} >= {1, 2} # True

# ============================================================================
# 7. DICTIONARIES (Key-value pairs)
# ============================================================================

# Dictionary creation
empty_dict = {}
person = {"name": "Alice", "age": 25, "city": "NYC"}
from_keys = dict.fromkeys(["a", "b", "c"], 0)  # {'a': 0, 'b': 0, 'c': 0}

# Dictionary access
name = person["name"]           # 'Alice' (raises error if key doesn't exist)
age = person.get("age")         # 25
default = person.get("salary", 0)  # 0 (default value if key doesn't exist)

# Dictionary modification
person["email"] = "alice@email.com"  # Add new key-value
person["age"] = 26              # Update existing value
person.update({"city": "LA", "country": "USA"})  # Update multiple

# Dictionary removal
del person["email"]             # Delete key-value pair
popped = person.pop("country")  # Remove and return value
last = person.popitem()         # Remove and return last (key, value) pair

# Dictionary methods
keys = person.keys()            # dict_keys(['name', 'age', 'city'])
values = person.values()        # dict_values(['Alice', 26, 'LA'])
items = person.items()          # dict_items([('name', 'Alice'), ...])

# Dictionary operations
has_key = "name" in person      # True
length = len(person)            # Number of key-value pairs

# Dictionary comprehension (covered later)
squared = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ============================================================================
# 8. CONDITIONAL STATEMENTS
# ============================================================================

# Basic if-elif-else
age = 18
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# Comparison operators: ==, !=, <, >, <=, >=
# Logical operators: and, or, not
x = 10
if x > 5 and x < 15:
    print("x is between 5 and 15")

if not (x < 0 or x > 100):
    print("x is in valid range")

# Ternary operator (conditional expression)
status = "Even" if x % 2 == 0 else "Odd"

# Truthy and Falsy values
# Falsy: False, None, 0, 0.0, "", [], {}, ()
# Everything else is Truthy
if []:
    print("This won't print")
if [1, 2]:
    print("This will print")

# ============================================================================
# 9. LOOPS
# ============================================================================

# For loop
for i in range(5):              # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):       # 2, 4, 6, 8 (start, stop, step)
    print(i)

# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Enumerate (get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Iterate over dictionary
person = {"name": "Alice", "age": 25}
for key in person:              # Iterate over keys
    print(key)

for value in person.values():   # Iterate over values
    print(value)

for key, value in person.items():  # Iterate over key-value pairs
    print(f"{key}: {value}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue                # Skip this iteration
    if i == 7:
        break                   # Exit loop
    print(i)
else:
    print("Loop completed normally")  # Executes if no break

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# ============================================================================
# 10. FUNCTIONS
# ============================================================================

# Basic function
def greet(name):
    """This is a docstring describing the function."""
    return f"Hello, {name}!"

result = greet("Alice")

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))                 # 9 (uses default exponent=2)
print(power(3, 3))              # 27

# Keyword arguments
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

describe_pet(animal="dog", name="Rex")  # Order doesn't matter
describe_pet(name="Whiskers", animal="cat")

# Variable number of arguments
def sum_all(*args):             # *args = tuple of arguments
    return sum(args)

print(sum_all(1, 2, 3, 4))      # 10

def print_info(**kwargs):       # **kwargs = dict of keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Return multiple values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(square(5))                # 25

add = lambda x, y: x + y
print(add(3, 4))                # 7

# Lambda with map, filter, reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))        # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers)) # [2, 4]

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)       # 120

# ============================================================================
# 11. LIST COMPREHENSIONS
# ============================================================================

# Basic list comprehension
squares = [x**2 for x in range(10)]         # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# With if-else
parity = ["even" if x % 2 == 0 else "odd" for x in range(5)]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_squares = {x**2 for x in [1, -1, 2, -2]}  # {1, 4}

# Generator expression (memory efficient)
gen = (x**2 for x in range(10))             # Generator object
print(next(gen))                            # 0
print(next(gen))                            # 1

# ============================================================================
# 12. USEFUL BUILT-IN FUNCTIONS
# ============================================================================

# Type conversion
int("10")                       # String to int
float("3.14")                   # String to float
str(123)                        # Int to string
list("hello")                   # ['h', 'e', 'l', 'l', 'o']
tuple([1, 2, 3])                # (1, 2, 3)
set([1, 2, 2, 3])               # {1, 2, 3}
dict([("a", 1), ("b", 2)])      # {'a': 1, 'b': 2}

# Numeric functions
abs(-5)                         # 5
round(3.7)                      # 4
pow(2, 3)                       # 8
min(1, 2, 3)                    # 1
max(1, 2, 3)                    # 3
sum([1, 2, 3])                  # 6

# Sequence functions
len([1, 2, 3])                  # 3
sorted([3, 1, 2])               # [1, 2, 3]
reversed([1, 2, 3])             # Iterator
all([True, True, False])        # False (all elements truthy?)
any([False, False, True])       # True (any element truthy?)

# zip (combine iterables)
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# enumerate (index and value)
for i, name in enumerate(names):
    print(f"{i}: {name}")

# range
list(range(5))                  # [0, 1, 2, 3, 4]
list(range(2, 10, 2))           # [2, 4, 6, 8]

# input (get user input)
# name = input("Enter your name: ")  # Returns string

# isinstance (check type)
isinstance(5, int)              # True
isinstance("hello", str)        # True
isinstance([1, 2], list)        # True

# ============================================================================
# 13. ADVANCED FEATURES (Brief Introduction)
# ============================================================================

# Decorators
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator_func
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Alice")

# Generators (functions that yield values)
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)                  # 5, 4, 3, 2, 1

# Context managers
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# with FileManager("test.txt") as f:
#     f.write("Hello")

# ============================================================================
# 14. COMMON IDIOMS AND TRICKS
# ============================================================================

# Swap variables
a, b = 10, 20
a, b = b, a                     # a=20, b=10

# Multiple comparisons
x = 15
if 10 < x < 20:                 # Chained comparison
    print("x is between 10 and 20")

# Default dictionary value
counts = {}
for letter in "hello":
    counts[letter] = counts.get(letter, 0) + 1

# Or use defaultdict
from collections import defaultdict
counts = defaultdict(int)
for letter in "hello":
    counts[letter] += 1

# Counter
from collections import Counter
word = "hello"
letter_counts = Counter(word)   # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Unpacking
first, *rest = [1, 2, 3, 4, 5]  # first=1, rest=[2,3,4,5]

# Check if all/any elements satisfy condition
numbers = [2, 4, 6, 8]
all_even = all(x % 2 == 0 for x in numbers)  # True

# Flatten list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]  # [1,2,3,4,5,6]

# Dictionary merge (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2          # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Walrus operator (Python 3.8+)
# if (n := len([1, 2, 3])) > 2:
#     print(f"Length {n} is greater than 2")

# ============================================================================
# 15. IMPORT STATEMENTS
# ============================================================================

# Import entire module
import math
print(math.pi)                  # 3.141592653589793
print(math.sqrt(16))            # 4.0

# Import specific functions
from math import pi, sqrt
print(pi)                       # No need for math. prefix

# Import with alias
# import numpy as np            # Common convention (requires installation)
from datetime import datetime as dt

# Import all (not recommended)
# from math import *

# ============================================================================
# END OF BASIC PYTHON REFERENCE
# ============================================================================
