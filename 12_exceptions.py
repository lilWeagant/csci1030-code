def div(a, b):
    return a / b

print(f'1/2 is {div(1, 2)}')

# this try/except makes the error harder to find/fix
# this isn't great for programmer errors, but good for user errors
try:
    result = div(1, 0)
    print(result) # built-in exception -> ZeroDivisonError
except Exception as err:
    print(err)
finally:
    # code executes if there's an error or not
    # always runs
    # example, closing a file
    # clean up any resources
    print('in finally')

print('after exception')

# user defined exception