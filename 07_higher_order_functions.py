# def traverse(elements, op):
#     for element in elements:
#         op(element)

# def output(x):
#     print(x)

# traverse([1, 2, 3], output)

# # Lambda expression is essentially an unnamed function
# add = lambda x,y: x + y 
# z = add(1, 2)
# print(z)

# # 'map' Function -> e.g. converting fahrenheit to celsius
# def f_to_c(f):
#     return (f - 32) * 5 / 9

# f_temps = [60.0, 70.0, 80.0, 90.0, 100.0]
# c_temps = map(f_to_c, f_temps)
# for temp in c_temps:
#     print(temp)

# # 'reduce' Function -> e.g. get the sum of elements in a list
# from functools import reduce

# def add(x, y):
#     return x + y
# sum = reduce(add, [1, 2, 3, 4, 5])

# sum2 = reduce(lambda x,y: x + y, [1, 2, 3, 4, 5])
# print(sum)
# print(sum2)

# 'filter' Function -> e.g. filter grades > 80
grades = [64.5, 87.0, 94.0, 71.5, 46.0, 100.0]

def a_filter(x):
    return x > 80.0

# a_grades = filter(a_filter, grades)
# for x in a_grades:
#     print(x)
a_grades2 = list(filter(lambda x: x > 80.0, grades))
print(a_grades2)
