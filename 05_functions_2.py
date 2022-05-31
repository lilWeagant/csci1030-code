# # Review of arguments and return values
# def print_message(message):
#     print(message)

# def add_to_message(message):
#     message += ' - From Riley' # += -> message = message + ' - From Riley'
#     return message

# mes = 'hello CSCI1030!'
# print_message(mes)
# print(add_to_message(mes))
# message = add_to_message(mes)
# print(message)
# print(mes)

# def times_two(x):
#     x = x*2

# x = 4
# print(x) # print 4
# times_two(x) # function call
# print(x) # what value will be printed to the console? -> 4 because of local variable and pass by value

# def add_to_list(list):
#     list.append(3)
#     return list

# list1 = [1, 2, 3]
# print(list1)
# list1 = add_to_list(list1)
# print(list1) # what value will be printed to the console? -> [1, 2, 3, 3] because pass by reference

# # Demonstrate Calling Stack -> do this at beginning on Tuesday May 31st

def func1(a, b):
    x = 1
    return a + b + x

def func2(x):
    y = 8
    z = func1(x, y)
    return z

print(func2(4))

# Coding Exercise

#x = 12345 # 12345/10 = 12340 with remainder of 5

# def to_str(num):
#     result = ''
#     while num > 0:
#         # % -> modulus operator
#         digit = num % 10
#         num = num//10 # floor division -> truncate decimal point
#         result += str(digit) # += -> shorthand for result = result + str(digit)
#     return result

# print(to_str(12345))