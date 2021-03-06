# Object Oriented Programming Example

# Student Class -> courses, grades, grade_average
class Student:
    def __init__(self):        
        self.courses = [] # instance variables
        self.grades = []
    def set_course_grade(self, course, grade):  # Setter method/mutator method
        # add course name to a list of courses
        self.courses.append(course)
        self.grades.append(grade)
        sum = 0
        for g in self.grades:
            sum += g
        self.average = sum / len(self.grades)
    def get_average(self):                      # Getter method/accessor method
        return self.average
    def __str__(self):
        return "Average: " + str(self.average)

class Course:
    def __init__(self, code, name):         # Constructor
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
        return self.code + ' - ' + self.name

# Implement Online Course
class OnlineCourse(Course):
    def __init__(self, code, name):
        Course.__init__(self, code, name)
        self.web_address = ""
        self.open_to_public = False
    def set_web_address(self, web_address):
        self.web_address = web_address
    def get_web_address(self):
        return self.web_address
    def is_open_to_public(self):
        return self.open_to_public
    def set_open_to_public(self, open_to_public):
        self.open_to_public = open_to_public

rachel = Student()
ross = Student()
course1 = Course("CSCI1030U", "Intro to Computer Science")
#course1.set_name("Intro to Computer Science")
#course1.set_code("CSCI1030U")
course2 = Course("MATH1010U", "Calculus I")
# course2.set_name("Calculus I")
# course2.set_code("MATH1010U")
online_course = OnlineCourse("CSCI1060U", "Programming Workshops I")
online_course.set_open_to_public(True)
# course2.set_open_to_public(True) -> throw an error -> no method set_open_to_public defined in Course
rachel.set_course_grade(course1, 64.0)
rachel.set_course_grade(course2, 85.0)
ross.set_course_grade(course1, 70.0)
ross.set_course_grade(course2, 80.0)
# rachel.set_course_grade("Calculus I", 85.0)
# rachel.set_course_grade("Calculus II", 60.0)
#print(rachel.get_average())
print(f'{course1.get_name()} - {course1.get_code()}') # expected -> Intro to Computer Science - CSCI1030U
print(f'{course2.get_name()} - {course2.get_code()}') # expected -> Calculus I - MATH1010U
print(course1)
print(course2)
print(rachel)
print(ross)
print(online_course)
