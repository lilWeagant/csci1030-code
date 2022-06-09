import csv

with open('data.csv', 'r') as file:
    for line in file:
        data = line.split(',')
        print(data)

data_list = [['sid', 'first_name', 'last_name', 'average'],
            ['1001', 'Rachel', 'Green', '60.0'],
            ['1002', 'Monica', 'Geller', '95.0'],
            ['1003', 'Ross', 'Geller', '96.0']
            ]
# with open('data_writer.csv', 'a') as file:
#     for data in data_list:
#         for d in range(len(data)):
#             if d == len(data)-1:
#                 file.write(data[d] + '\n')
#             else:
#                 file.write(data[d] + ',')

with open('data_writer.csv', 'w', newline='\n') as file:
    writer = csv.writer(file, delimiter = ',')
    for data in data_list:
        writer.writerow(data)