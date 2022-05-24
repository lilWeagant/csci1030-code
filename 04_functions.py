#Function with no arguments or return value

def say_hello():
    print("Hello!")

say_hello()

#Function with return value (but no arguments)

def get_answer():
    return 42

# print the value directly
print(get_answer())
# assign to a variable
answer  = get_answer()
print(answer)

# Function with return value and arguments
def times_two(x):
    answer = x*2
    return answer
#print(number) #number is local to times_two function
print(times_two(4)) # print 8
print(times_two(7)) # print 14
print(answer) # print 14, or 42?