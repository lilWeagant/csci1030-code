def div(a, b):
    return a / b

print(f'1/2 is {div(1, 2)}')

# this try/except makes the error harder to find/fix
# this isn't great for programmer errors, but good for user errors
try:
    result = div(1, 0)
    print(result) # built-in exception -> ZeroDivisonError
except Exception as err:
    print(err)
finally:
    # code executes if there's an error or not
    # always runs
    # example, closing a file
    # clean up any resources
    print('in finally')

print('after exception')

# user defined exception
import unittest

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def set_mark(self, course, mark):
            self.marks.append(mark)

    def get_average(self):
            sum = 0
            for mark in self.marks:
                sum += mark
            return sum / len(self.marks)
    
import unittest 

class Student_Test(unittest.TestCase):
    def test_init(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertEqual(clarissa.name, 'Clarissa')
        self.assertEqual(clarissa.gpa, 0.0)

    def test_set_mark(self):
        barbara = Student(0.0, 'Barbara')
        barbara.set_mark('CSCI1030U', 75)
        self.assertTrue(barbara.marks == [75])
        barbara.set_mark('CSCI1060U', 71)
        self.assertTrue(barbara.marks == [75, 71])

    def test_get_average(self):
        barbara = Student(0.0, 'Barbara')
        barbara.set_mark('CSCI1030U', 75)
        barbara.set_mark('CSCI1060U', 71)
        self.assertAlmostEquals(barbara.get_average(), 73)