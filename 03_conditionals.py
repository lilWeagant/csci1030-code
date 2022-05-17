# Conditional Examples

# Pass/Fail -> 50 is a pass

from re import X


grade = 78

if grade > 0 and grade < 50: # accept values between 0 and 50
    print("You got an F")
elif grade >= 50 and grade < 60: # between 50 and 59
    print("You got a D")
elif grade >= 60 and grade < 67: # between 60 and 66
    print("You got a C")
elif grade >= 67 and grade < 70: # between 67 and 69
    print("You got a C+")
elif grade >= 70 and grade < 73: # between 70 and 72
    print("You got a B-")
elif grade >= 73 and grade < 77: 
    print("You got a B")
elif grade >= 77 and grade < 80:
    print("You got a B+")
elif grade >= 80 and grade < 85:
    print("You got an A-")
elif grade >= 85 and grade < 90:
    print("You got an A")
elif grade >= 90 and grade <= 100:
    print("You got an A+")
else: # code block will be executed if condition is false
    print("Please enter a valid grade") # assumes that all grades entered are between 0 - 100

x = 9
y = 5

# if x > y:
#     max = x
# else:
#     max = y
# print(max)

# Ternary Operator
max = x if x>y else y
print(max)
