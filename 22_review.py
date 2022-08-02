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