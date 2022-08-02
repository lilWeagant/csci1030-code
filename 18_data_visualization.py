import matplotlib.pyplot as plt
import numpy as np

# # Pie Chart

# labels = ['Biology', 'Forensics', 'Chemistry', 'CompSci']
# counts = [81, 92, 41, 17]
# colours = ['c', 'm', 'y', 'b']
# explode = [0, 0.1, 0, 0.1]
# plt.pie(counts, labels = labels, explode = explode, autopct='%1.1f%%', colors = colours, shadow = True)
# plt.show()

# # Legend

# indices = np.arange(5) # generates 5 sequential values, used as x axis categories
# #indices = [1, 2, 3, 4, 5] # cannnot concatenate list and float (indicies + width)
# #indices = range(5) # cannot add range and float types (indicies + width)
# spending = [17000, 21500, 10500, 9800, 16000]
# earnings = [28000, 20350, 11300, 12000, 14500]
# width = 0.3
# p1 = plt.bar(indices, spending, width, color = 'b')
# p2 = plt.bar(indices+width, earnings, width, color = 'r')
# plt.legend((p1, p2), ('Spending', 'Earnings'))
# plt.title("Spending vs. Earnings")
# plt.grid(True)
# plt.show()

# Exercises
# Problem 1 -> read data from file and make a scatter plot of midterm grades
# # read data from file
# data_list = []
# with open('data.csv', 'r') as file:
#     for line in file:
#         data = line.split(',')
#         # print(data)
#         data_list.append(data)

# # separate midterm_average and names
# plot_list = []
# name_list = []
# for data in data_list[1:]: # skip first row (headers)
#     plot_list.append(float(data[3])) # get midterm grades and convert to numeric
#     name_list.append(data[1]) # get name values for x axis

# # plot the values
# #plot_list = [71, 95, 75, 48, 82, 76]
# #name_list = ['Rachel', 'Ross', 'Phoebe', 'Joey', 'Monica', 'Chandler']
# plt.plot(name_list, plot_list, 'r^')
# plt.show()

# Problem 2 -> Create a pie chart to summarize the friends survey
import json
with open('survey_results.json', 'r') as file:
    data = json.load(file)
# print(data)
values = []
labels = []
for d in data:
   # print(data[d])
   values.append(data[d])
   labels.append(d)
#labels = ['Rachel', 'Monica', 'Ross', 'Phoebe', 'Chandler', 'Joey']
#values = [45, 22, 10, 34, 18, 30]
colours = ['g', 'm', 'r', 'c', 'b', 'y']
explode = [0, 0, 0.1, 0, 0, 0]
plt.pie(values, labels = labels, explode = explode, autopct='%1.1f%%', colors = colours, shadow = True)
plt.title('Which Friends main character do you relate to the most?')
plt.show()

# [] -> brackets (square brackets)
# () -> parenthesis (brackets)
# {} -> braces (curly brackets OR curly braces)