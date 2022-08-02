# --------------------------
# QUESTION 2
# --------------------------
# GIVEN CODE
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, courses = []):
        Person.__init__(self, name, age)
        self.courses = courses
    def add_course(self, course_name):
        self.courses.append(course_name)
    def get_courses(self):
        return self.courses

# SOLUTION
s = Student("Riley", 29)
s.add_course("CSCI1030U")
print(s.get_courses())

# -------------------------------
# QUESTION 3
# -------------------------------

import json
class Processing: # define a class called Processing
    def __init__(self, filename): # constructor
        # what should our dictionary look like?
        # {'1001': {
        # 'first_name': 'Rachel',
        # 'last_name' : 'Green',
        # 'midterm_average': 71.0
        # },
        #  '1002': {
        # 'first_name': 'Ross',
        # 'last_name': 'Geller',
        # 'midterm_average': 95.0
        # }
        # }
        data_list = []
        with open(filename, 'r') as file:
            for line in file:
                data = line.split(',')
                data_list.append(data)
#        print(data_list)
        self.data_dict = {}
        for data in data_list[1:]:
            #print(data)
            self.data_dict[data[0]] = {
                'first_name':data[1],
                'last_name':data[2],
                'midterm_average':float(data[3])
            }
    
    def get_average(self):
#        print(self.data_dict)
        # return the average of midterm grades
        total = 0
        count = 0
        for d in self.data_dict:
            #print(self.data_dict[d]['midterm_average'])
            total += self.data_dict[d]['midterm_average']
            count += 1
        #print(total/count)
        return total/count
    
    def get_names(self):
        name_list = []
        for d in self.data_dict:
            name = self.data_dict[d]['first_name'] + self.data_dict[d]['last_name']
            name_list.append(name)
        #print(name_list)
        return name_list
    
    def add_student(self, sid, first_name, last_name, midterm_average):
        self.data_dict[str(sid)] = {
            'first_name':first_name,
            'last_name': last_name,
            'midterm_average':midterm_average
        }
        #print(self.data_dict)
    
    def write_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data_dict, file)

    def __str__(self):
        result = ''
        for d in self.data_dict:
            result += d + ','
            result += self.data_dict[d]['first_name'] + ','
            result += self.data_dict[d]['last_name'] + ', '
            result += str(self.data_dict[d]['midterm_average']) + '\n'
        return result