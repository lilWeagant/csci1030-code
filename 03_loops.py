# Loop Examples

# # Principal/Interest Calculation
# principal = 1000
# interest_rate = 0.02 # 2% interest rate
# x = 1 #represent number of interest periods
# #update principal with the total amount
# print(f'Initial amount: {principal}')
# # 1st Interest Period
# principal = principal + (principal * interest_rate)
# print(f'Total amount: {principal}')
# # 2nd Interest Period
# principal = principal + (principal * interest_rate)
# print(f'Total amount: {principal}')

# # While Loop
# x = 1
# while (x <= 10):
#     # calculate total
#     principal = principal + (principal * interest_rate)
#     print(f'Interest Period {x}: {principal}')
#     x+=1

#DO WHILE LOOPS DO NOT EXIST IN PYTHON (below is C++)
# do {
#     #block of code
# } while (x < 10)

#For Loop

# # C++ For Loop
# for (int i = 0; i < 10; i++){
#     #code block
# }

# for name in ["Rachel", "Ross", "Phoebe", "Monica", "Joey", "Chandler"]:
#     #code block
#     print(name)

# range function
# range(10) # -> min -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(1, 10) # -> min, max -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(0, 10, 2) # -> min, max, step -> [0, 2, 4, 6, 8]

# for x in range(0, 10, 2):
#     print(x)

# for x in range(1, 10, 2):
#     print(x)

# ESTIMATE SQUARE ROOT

x = 8 # just for testing, sqrt of 16 is 4

lower = 0.0 # we know that the sqrt cannot be less than 0
upper = x # we know that the sqrt of x cannot be greater than x itself

guess = (lower + upper)/2 # guess at the halfway point

#while guess**2 != x: # does not work with floating point numbers 
while abs((guess**2) - x) >= 0.00000000000001: # difference should be very small 
    if guess**2 < x:
        # guess is too low
        lower = guess # adjust lower limit
    elif guess**2 > x:
        # guess is too high
        upper = guess # adjust upper limit
    # once we've adjusted the limits, make another guess
    guess = (lower + upper)/2

print(f'The square root of {x} is {guess}')