# # Write a class that performs some math operations on x and y

# class Math:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def update_values(self, x, y):
#         self.x = x
#         self.y = y
#     def add(self):
#         return self.x + self.y
#     def subtract(self):
#         return self.x - self.y
#     def multiply(self):
#         return self.x * self.y
#     def divide(self):
#         # error when y = 0
#         return self.x/self.y

# m = Math(3, 4)
# print(m.add()) # 7
# print(m.subtract()) # -1
# print(m.multiply()) # 12
# print(m.divide()) # 0.75

# File I/O -> read .csv file into Python dictionary

pet_dict = {}
line_list = []
with open('pet_info.csv', 'r') as pet_file:
    for line in pet_file:
        data = line.split(',')
        #print(data)
        line_list.append(data)
        #pet_dict[data[0]] = {'age': int(data[1]), 'last_seen': data[1]}
        # print(line)
        # Dictionary
        # {
        # 'Kitty':{'age': 9,
        #           'last_seen': '08/2019'},
        #  'Sasha': {'age': 4,
        #            'last_seen': '07/2021'},
        #   ...
        # }
for line in line_list[1:]:
    pet_dict[line[0]] = {'age': int(data[1]), 'last_seen': data[2]}
print(pet_dict)

# Exceptions and Unit Testing
import unittest

class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def __str__(self):
        return self.code + " - " + self.name

class Course_Test(unittest.TestCase):
    def test_init(self):
        c = Course('CSCI1030U', 'Intro to CS')
        self.assertEqual(c.name, 'Intro to CS')
        self.assertEqual(c.code, 'CSCI1030U')
    def test_set_name(self):
        c = Course('CSCI1030U', 'Intro to CS')
        c.set_name('Introduction to Computer Science')
        self.assertEqual(c.name, 'Introduction to Computer Science')
    def test_set_code(self):
        c = Course('CSCI1030U', 'Intro to CS')
        c.set_code('CSCI1030')
        self.assertEqual(c.code, 'CSCI1030')
    def test_get_name(self):
        c = Course('CSCI1030U', 'Intro to CS')
        self.assertEqual(c.get_name(), 'Intro to CS')
    def test_get_code(self):
        c = Course('CSCI1030U', 'Intro to CS')
        self.assertEqual(c.get_code(), 'CSCI1030U')
    def test_str(self):
        c = Course('CSCI1030U', 'Inro to CS')
        self.assertEqual(print(c), 'CSCI1030U - Intro to CS')

# Data Structures

# Properties of a Stack
# Push -> add item to top of stack
# Pop -> remove item from top of stack
# Top -> return item on top
def print_stack(stack):
    top = len(stack) - 1
    print('--------------')
    while top >= 0:
        print(stack[top])
        top -= 1
stack = []
stack.append("Banana")
print_stack(stack)
stack.append("Apple")
print_stack(stack)
stack.pop()
print_stack(stack)
stack.append("Strawberry")
stack.append("Cherry")
print_stack(stack)
stack.pop()
print_stack(stack)
stack.pop()
print_stack(stack)
stack.append("Avocado")
print_stack(stack)
stack.pop()
print_stack(stack)

# Data Visualization
import matplotlib.pyplot as plt

semesters = [1, 2, 3, 4, 5, 6, 7, 8]
s1 = [2.8, 1.6, 2.0, 2.3, 3.1, 3.3, 2.8, 3.0]
s2 = [3.3, 4.0, 2.8, 2.8, 2.3, 3.0, 3.3, 4.0]

p1 = plt.plot(semesters, s1, 'g:')
p2 = plt.plot(semesters, s2, 'r-')
plt.legend((p1, p2), ("Student 1", "Student 2"))
plt.grid(True)
plt.title("Semester GPA")
plt.xlabel("Semester Number")
plt.ylabel("GPA")
plt.show()