import matplotlib.pyplot as plt
import random
import numpy as np
# indices = np.arange(5)  # returns evenly spaced values within given interval

# plt.plot([1, 2, 3, 4, 5],[7, 4, 11, 13, 9], "b-",
#         [1, 2, 3, 4, 5], [11, 7, 10, 9, 4], "r:")     # Line plot
# plt.plot([1, 2, 3, 4, 5],[7, 4, 11, 13, 9], "bs",
#         [1, 2, 3, 4, 5], [11, 7, 10, 9, 4], "ro")       # Scatter plot
# #plt.xlabel("Week")
# plt.ylabel("Score")
# plt.title("Performance")
# plt.axis([0, 6, 0, 15])
# plt.grid(True)
# Saving your plot as an image
# figure = plt.gcf() # get current figure
# figure.set_size_inches(8.0, 5.0)
# figure.savefig('images/test_results.png', dpi=100) 
#plt.show()

# Histogram
# x = []
# for y in range(1000):
#     x.append(random.randint(0, 100))
# OR
# x = [random.randint(0, 100) for y in range(1000)] # list comprehension
# numBuckets = 50
# plt.hist(x, numBuckets, facecolor='c')
# plt.grid(True)
# plt.show()

# Bar Chart
indices = np.arange(5) # generates 5 sequential values, used as x axis categories
#indices = [1, 2, 3, 4, 5] # cannnot concatenate list and float (indicies + width)
#indices = range(5) # cannot add range and float types (indicies + width)
spending = [17000, 21500, 10500, 9800, 16000]
earnings = [28000, 20350, 11300, 12000, 14500]
width = 0.3
plt.bar(indices, spending, width, color = 'b')
plt.bar(indices+width, earnings, width, color = 'r')
plt.grid(True)
plt.show()