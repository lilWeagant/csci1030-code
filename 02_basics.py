#Basic Python Programming and Debugging

# print('Riley\'s Course')
# print("Riley's Course")

# x = 10
# print(x)

#int x = 10, y = 11;
#int x = 10;
#int y = 11;
#x++; #increment value of x by 1 (in C++)
# x, y = 10, 11
# print (x)
# print (y)
# x += 1 # adds 1 to x -> 10 + 1 = 11
# x = x + 1 # adds 1 to x -> 11 + 1 = 12
# print (x) # print 12 
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

# course_name = 'CSCI1030U'
# print(course_name[30]) # index is out of bounds 

# EXERCISE 1 - INTEREST RATE

principal = 1000 # initial amount
interest_rate = 0.02 # 2% interest rate

# either use principal amount to hold total amount -> update principal variable 
# or use a different variable to hold total amount

total = principal + (principal * interest_rate) # after 1 interest period -> 1020.00
# total = principal + (principal * interest_rate) # after 2 interest periods
print (f'1 interest period: {total}')
total = total + (total * interest_rate) #after 2 interest periods -> 1020 is the new amount that we are using to calculate interest
print (f'2 interest periods: {total}')
total = total + (total * interest_rate) #after 3 interest periods -> 1020 is the new amount that we are using to calculate interest
print (f'3 interest periods: {total}')
total = total + (total * interest_rate) #after 4 interest periods -> 1020 is the new amount that we are using to calculate interest
print (f'4 interest periods: {total}')
total = total + (total * interest_rate) #after 5 interest periods -> 1020 is the new amount that we are using to calculate interest
print (f'5 interest periods: {total}')
total = total + (total * interest_rate) #after 6 interest periods -> 1020 is the new amount that we are using to calculate interest
print (f'6 interest periods: {total}')

