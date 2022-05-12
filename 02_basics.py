#Basic Python Programming and Debugging

# print('Riley\'s Course')
# print("Riley's Course")

from re import X


x = 10
print(x)

#int x = 10, y = 11;
#int x = 10;
#int y = 11;
#x++; #increment value of x by 1 (in C++)
x, y = 10, 11
print (x)
print (y)
x += 1 # adds 1 to x -> 10 + 1 = 11
x = x + 1 # adds 1 to x -> 11 + 1 = 12
print (x) # print 12 
# -=, /=, *=
# int x = 10, y = 11;
# int tmp = x;
# x = y;
# y = tmp;
# x, y = 10, 11
# print(f'x: {x}, y: {y}')
# x, y = y, x
# print(f'x: {x}, y: {y}')

# int x = 10;
# x = "Riley"; # C++ would throw an error

# x = 10 #integer
# print(x)
# x = "Riley" #string
# print(x)


# name = "Rachel Green"
# print("Name:", name)
# print(f'Name: {name}')

# cost = 2.14
# total_cost = 5 * cost
# print(f'Cost per item: {cost}, Total cost: {total_cost}')

course_name = 'CSCI1030U'
print(course_name[3])