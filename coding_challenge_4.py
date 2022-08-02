# -----------------------
# QUESTION 1
# -----------------------
# GIVEN CODE
class Student():
    def __init__(self, name, age, courses = []):
        self.name = name
        self.age = age
        self.courses = courses
    def add_course(self, course_name):
        self.courses.append(course_name)
    def get_courses(self):
        return self.courses

# SOLUTION
import unittest

class Student_Test(unittest.TestCase):
    def test_init(self):
        s = Student('Riley', 29)
        self.assertEqual(s.name, 'Riley')
        self.assertEqual(s.age, 29)
    def test_add_course(self):
        s = Student('Riley', 29)
        s.add_course("CSCI1030U")
        self.assertTrue(s.courses == ['CSCI1030U'])
    def test_get_courses(self):
        s = Student('Riley', 29)
        s.add_course("CSCI1030U")
        self.assertTrue(s.get_courses == ['CSCI1030U'])

# -----------------------
# QUESTION 2
# -----------------------
import random
import matplotlib.pyplot as plt
class DiceGame:
    def roll_dice(self):
        self.d1 = random.randint(1, 6)
        self.d2 = random.randint(1, 6)
        return self.d1 + self.d2
    def run_simulation(self, num_rolls):
        self.rolls = []
        self.win_count = 0
        for x in range(num_rolls):
            self.rolls.append(self.roll_dice())
            if self.rolls[x] == 7:
                self.win_count += 1
    def get_summary(self):
        numBuckets = 11
        frequency = self.win_count/len(self.rolls) * 100
        plt.hist(self.rolls, numBuckets, facecolor='r')
        plt.title(f'Frequency of Dice Rolls ({frequency:0.2f}% 7s)')
        plt.show()
#g = DiceGame()
#g.run_simulation(100)
#g.get_summary()

# ---------------------
# QUESTION 3
# ---------------------
class SubstitutionCipher:
    def __init__(self, cipher):
        self.cipher = cipher
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def encrypt(self, message):
        ciphertext = ''
        for ch in message:
            index = self.alphabet.index(ch)
            ciphertext += self.cipher[index]
        return ciphertext
    def decrypt(self, ciphertext):
        message = ''
        for ch in ciphertext:
            index = self.cipher.index(ch)
            message += self.alphabet[index]
        return message

c = SubstitutionCipher('QWERTYUIOPASDFGHJKLZXCVBNM')
print(c.encrypt('CODINGISFUN')) # expect EGROFUOLYXF
print(c.decrypt('LTEKTZDTLLQUTLQKTEGGS'))