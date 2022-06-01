# Classify a number as a low number (between 0 -9) -> return True if low, False otherwise

def is_low_num(num):
    if num in range(10): # range(10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        return True
    else:
        return False

# # Test is_low_num()
# print(is_low_num(6)) # should return True
# print(is_low_num(13)) # should return False

def count_low_nums(nums):
    count = 0
    for num in nums:
        if is_low_num(num): # return True or False
            count += 1 # += is shorthand for count = count + 1
    return count

# # Test count_low_nums()
# print(count_low_nums([1, 12, 4, 9, 20])) # should return 3
# print(count_low_nums([1, 23, 45, 6, 7, 8, 9])) # should return 5
# print(count_low_nums([12, 34, 56, 78, 91])) # should return 0

def rec_count_nums(nums):
    # base case -> when should our function exit?
    # n - 1 -> list without 1 element 
    if len(nums) == 0:
        return 0
    elif is_low_num(nums[0]): # if first number in list is low...
        return 1 + rec_count_nums(nums[1:]) # pass the list without the first element
        # return n * recursive_call(n-1) -> factorial example  
    else:
        return 0 + rec_count_nums(nums[1:])

# Test rec_count_nums()
print(rec_count_nums([1, 12, 4, 9, 20])) # should return 3
print(rec_count_nums([1, 23, 45, 6, 7, 8, 9])) # should return 5
print(rec_count_nums([12, 34, 56, 78, 91])) # should return 0