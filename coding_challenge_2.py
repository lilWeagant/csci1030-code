from functools import reduce

from attr import validate
# ---------------------------------
# QUESTION 1
# ---------------------------------

# *************************************
# ************* PART 1 ****************
# *************************************

# GIVEN CODE 
num_list = [48, 60, 85, 54, 76]

x = reduce(lambda x,y: x + y, num_list)
y = x/len(num_list)

print(y)

# SOLUTION
def calculate_average(num_list):
    sum = 0
    for x in num_list:
        sum += x
    return sum/len(num_list)

# *************************************
# ************* PART 2 ****************
# *************************************

# GIVEN CODE
grade_list = [48, 60, 85, 54, 76]
result = []
for grade in grade_list:
    if grade >= 50:
        result.append(grade)
print(f'You passed {len(result)}/{len(grade_list)} courses')

# SOLUTION
result = list(filter(lambda x: x >= 50, grade_list))
print(f'You passed {len(result)}/{len(grade_list)} courses')

# -------------------------
# QUESTION 2
# -------------------------
import re
def validate_postal_code(code):    
    postalRE = re.compile("[A-Za-z]\d[A-Za-z](\s)?\d[A-Za-z]\d")
    match = postalRE.match(code)
    if match:
        return True
    else:
        return False

def calculate_shipping(pcode, weight, distance):
    coverage = ["L6A", "L4A", "K0J", "K6J", "K2P", "L1H", "P7K", "L8H", "L6K"]
    code = pcode[:3] # grab the first 3 characters to compare with coverage list
    if validate_postal_code(pcode) and (code in coverage):
        if (distance < 15):
            cost = weight * 0.20
        elif (distance < 40):
            cost = weight * 0.28
        elif (distance < 75):
            cost = weight * 0.36
        elif (distance >= 75):
            cost = weight * 0.52
        return (f'The estimated price is CAD{cost:0.2f}')
    elif (not validate_postal_code(pcode)):
        return ("This postal code is not valid")
    elif (code not in coverage):
        return ("Sorry, we do not deliver to the desired destination") 

        

print(calculate_shipping('L1H8A4', 100, 35)) #expected 28.00
print(calculate_shipping('M4K2J2', 100, 35)) #expected 'Sorry, we do not deliver...'
print(calculate_shipping('444kkk', 100, 35)) #expected "This postal code is not valid"
