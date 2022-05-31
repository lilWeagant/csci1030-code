# # Direct recursion -> forever() calls itself forever
# def forever(message):
#     print(message)
#     forever(message)

# forever("hello")

# # Indirect recursion -> forever1 calls forever2 which calls forever1 forever
# def forever1():
#     print("hello")
#     forever2()

# def forever2():
#     forever1()

# forever1()

# # Recursion with exit condition
# def repeat_n_times(n, message):
#     if n < 1:
#         return
#     print(n)
#     print(message)
#     repeat_n_times(n - 1, message)

# repeat_n_times(10, "hello")

# # More efficient than tail recursion
# def repeat_n_times(n, message):
#     for i in range(n):
#         print(i)
#         print(message)

# repeat_n_times(10, "hello")

# # # Iteration 1
# # n = 10
# # repeat_n_times(n -1, message) -> n = 10 - 1 = 9 -> repeat_n_times(9, message)
# # # Iteration 2
# # n = 9
# # repeat_n_times(n - 1, message) -> n = 9 - 1 = 8 -> repeat_n_times(8, message)
# # # Iteration 3
# # n = 8
# # repeat_n_times(n - 1, message) -> n = 8 - 1 = 7 -> repeat_n_times(7, message)
# # ...
# # # Iteration 10
# # n = 1
# # repeat_n_times(n - 1, message) -> n = 1 -1 = 0 -> repeat_n_times(0 , message)

# # Factorial Problem -> recursion
# def solve_factorial(n): # solve n!
#     # base case (exit condition) is n = 0 or n = 1
#     print(n)
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * solve_factorial(n-1)

# print(solve_factorial(5))

# Solution to Coding Exercise -> Fibonacci Sequence

def fib(n): #calculate the nth number in fibonacci sequence
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n-2)

x = 8
print(f'The {x}th fibonacci number is {fib(x)}')