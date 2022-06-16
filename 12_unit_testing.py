class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
        self.marks = []
    
    def set_mark(self, mark):
        self.marks.append(mark)
    
    def get_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum / len(self.marks)

import unittest

class Student_Test(unittest.TestCase):
    def test_init(self):
        rachel = Student(0.0, 'Rachel')
        self.assertEqual(rachel.name, 'Rachel')
        self.assertEqual(rachel.gpa, 0.0)
    
    def test_set_mark(self):
        rachel = Student(0.0, 'Rachel')
        rachel.set_mark(75.0)
        self.assertTrue(rachel.marks == [75.0])
        rachel.set_mark(80.0)
        self.assertTrue(rachel.marks == [75.0, 80.0])

    def test_get_average(self):
        rachel = Student(0.0, 'Rachel')
        rachel.set_mark(70.0)
        rachel.set_mark(80.0)
        self.assertAlmostEqual(rachel.get_average(), 75.0)

if __name__ == '__main__':
    unittest.main()