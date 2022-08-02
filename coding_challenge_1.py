# ----------------------------
# QUESTION 1
# ----------------------------
# THE STARTER CODE
numlist = [10, 5, 14, 8, 74]
result = []
# for each elem in numlist insert a value into result
for num in numlist:
    num_elem = len(result)
    if num_elem==0:
        result.append(num)
    else:
        result.append(result[num_elem-1] + num)
# the final result
print(result)

# SOLUTION
# What does the code snippet do?
# - checks if result list is empty. if empty, appends the first num
# - if not empty, appends sum of previous element and num
def sum_list(numlist):
    result = []
    for num in numlist:
        num_elem = len(result)
        if num_elem == 0:
            result.append(num)
        else:
            result.append(result[num_elem - 1] + num) 
    return result

print(sum_list([10, 5, 14, 8, 74]))

# --------------------------
# QUESTION 2
# --------------------------

def calculate_score(actual_length, actual_weight, guess_length, guess_weight):
    length_score = (abs(actual_length - guess_length)*2)*5
    weight_score = abs(actual_weight - guess_weight)*5
    return length_score + weight_score

actual_length = 19 # actual length is 19 inches
actual_weight = 108 # actual weigth is 108 ounces
riley = calculate_score(actual_length, actual_weight, 22, 115)
prateek = calculate_score(actual_length, actual_weight, 18, 96)

if riley > prateek:
    print(f'Prateek is the winner with {prateek} points')
else:
    print(f'Riley is the winner with {riley} points')