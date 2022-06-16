# # Reading File (File Input)
# plain_text_file = open('plain_text_file.txt', 'r')
# print(plain_text_file.read())
# plain_text_file.close()

# line_list = []
# with open('plain_text_file.txt', 'r') as plain_text_file:
#     for line in plain_text_file:
#         # print(line, end='')
#         line_list.append(line)

# print(line_list)
# print('\ndone reading file')

# Writing to Files (File Output)

# student_names = ['Rachel', 'Monica', 'Phoebe']
# with open('output_data.txt', 'w') as student_file:
#     for name in student_names:
#         student_file.write(f'{name}\n')

# # Append to File
# new_students = ['Ross', 'Chandler', 'Joey']
# with open('output_data.txt', 'a') as student_file:
#     for name in new_students:
#         student_file.write(f'{name}\n')

# # Read JSON
# import json

# # with open('student_info.json', 'r') as grades_file:
# #     grades = json.load(grades_file)
# #     print(grades["grades"])

# products = [
#     {
#         'product_id': '1',
#         'name': 'Leather Pants',
#         'price': '$79.99'
#     },
#     {
#         'product_id': '2',
#         'name': 'Sandwich',
#         'price': '$1.50'
#     }
# ]

# with open('products.json', 'w') as products_file:
#     json.dump(products, products_file)

# Read CSV file (without csv library)
csv_list = []
with open('data.csv', 'r') as file:
    for line in file:
        data = line.split(',')
        # print(data)
        csv_list.append(data)
print(csv_list)

data_list = [
    ['sid', 'first_name', 'last_name', 'average'], #length = 4, last index = 3
    ['1001', 'Rachel', 'Green', '60.0'],
    ['1002', 'Monica', 'Geller', '95.0'],
    ['1003', 'Ross', 'Geller', '96.0']
]

# with open('csv_writer.csv', 'a') as file:
#     for data in data_list:
#         # file.write(f'{data}\n')
#         for d in range(len(data)):
#             # file.write(f'{d}, ')
#             if d == len(data)-1: # if last element in list
#                 file.write(f'{data[d]}\n')
#             else: # all the other elements in list
#                 file.write(f'{data[d]}, ')

import csv

with open('csv_writer.csv', 'w', newline='\n') as file:
    writer = csv.writer(file, delimiter = ',')
    for data in data_list:
        writer.writerow(data) 