# INSERT-SORT(A)
# 1  for j = 2 to length[A] do              # for loop iterates over list A starting at second index
# 2     key = A[j]
# 3     i = j-1
# 4     while i > 0 and A[i] > key do
# 5        A[i+1] = A[i]
# 6        i = i-1
# 7     A[i+1] = key

def insert_sort(A):
    op_count = 0
    for j in range(1, len(A)): # give us a list of indexes that we can use to access elements in A
        key = A[j] # sets current value
        i = j - 1
        while i >= 0 and A[i] > key: # compares key to values on the left
            A[i+1] = A[i]
            op_count += 1 
            i = i - 1
        A[i+1] = key # insert key value
        op_count += 1
    return op_count

# Test insert_sort()
A_list = [17, 9, 22, 12, 21, 6, 16]
B_list = [3, 16, 7, 28, 2, 9, 22, 33, 17, 13]
print(f'Unsorted A: {A_list}')
print(f'A_list: {insert_sort(A_list)}')
print(f'Sorted A: {A_list}')
print(f'Unsorted B: {B_list}')
print(f'B_list: {insert_sort(B_list)}')
print(f'Sorted B: {B_list}')

import random
# n = 1000
values = []
for n in range(1000): # generate 1000 random values
    values.append(random.randint(0, 100))

print(f'Unsorted values: {values}')
print(f'Values op_count: {insert_sort(values)}')
print(f'Sorted values: {values}')
