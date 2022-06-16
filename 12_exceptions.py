# # custom error class
# class DontDivideByZero(Exception):
#     pass

# def div(a, b):
#     if b == 0:
#         # return "You can't divide by 0" # this is not good, type might be unexpected
#         raise DontDivideByZero('cannot divide by zero')
#     return a/b

#print(f'1/0 is {div(1, 0)}') # try dividing by zero
# numer = 1
# denom = 0
# result = div(numer, denom)
# print(result + 1)

# this makes it more difficult to find the error in the program
# try:
#     result = div(1, 0)
#     print(f'1/0 is {result}')
# except ZeroDivisionError as error:
#     # executes when the program raises an error
#     print(error)
# finally:
#     # executes no matter what
#     # clean up any resources that were used by the try code
#     print("in finally")

# try/except block is used to catch user-caused errors, and you want to guide the user to fix the error

# Raise Exception if user is under 18 years of age

class IsUnder18(Exception):
    pass

age = int(input("Please enter your age: "))
# print(type(age))
if age < 18:
    raise IsUnder18("Sorry, you cannot access this page")