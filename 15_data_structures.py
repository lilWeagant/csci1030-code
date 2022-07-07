# # Dictionaries

# customers = [
#     {
#         "first_name": "Rachel",
#         "last_name": "Green",
#         "credit": True,
#         "balance": 588.95,
#         "customer_since": "1994/04/05"
#     },
#     {
#         "first_name": "Monica",
#         "last_name": "Geller",
#         "credit": True,
#         "balance": 0.00,
#         "customer_since": "1995/06/07"
#     }
# ]

# print(len(customers))

# for cust in customers:
#     print(cust['first_name'], cust['last_name'])
#     cust['num_purchases'] = 0
#     cust['credit'] = False

# print(customers)

# # Stacks -> using Python List

# stack = []
# # push values onto stack
# stack.append(1)
# print(stack)
# stack.append(2)
# print(stack)
# stack.append(3)
# print(stack)
# print('top:', stack[-1])
# print('isEmpty: ', (len(stack) == 0))
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)
# print('isEmpty: ', (len(stack) == 0))

# Queues -> using Python list
queue = [] # new empty queue
queue.append(1) # enqueue(1)
print(queue)
queue.append(2) # enqueue(2)
print(queue)
queue.append(3) # enqueue(3)
print(queue)
print('front:', queue[0])
print('isEmpty?', (len(queue) == 0))
print(queue.pop(0)) # dequeue()
print(queue)
print(queue.pop(0)) # dequeue()
print(queue)
print(queue.pop(0)) # dequeue()
print(queue)
print('isEmpty?', (len(queue) == 0))
