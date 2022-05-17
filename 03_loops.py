# Loop Examples

# Principal/Interest Calculation
principal = 1000
interest_rate = 0.02 # 2% interest rate
x = 1 #represent number of interest periods
#update principal with the total amount
print(f'Initial amount: {principal}')
# # 1st Interest Period
# principal = principal + (principal * interest_rate)
# print(f'Total amount: {principal}')
# # 2nd Interest Period
# principal = principal + (principal * interest_rate)
# print(f'Total amount: {principal}')

# block of code
while (x <= 10):
    # calculate total
    principal = principal + (principal * interest_rate)
    print(f'Interest Period {x}: {principal}')
    x+=1

#DO WHILE LOOPS DO NOT EXIST IN PYTHON
# do {
#     #block of code
# } while (x < 10)