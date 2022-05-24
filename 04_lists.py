# nums = [1, 2, 3, 4, 5] #integer list
# names = ["Rachel", "Monica", "Phoebe", "Ross", "Joey", "Chandler"] #list of strings

# print(nums[2]) # select element from nums at index 2 -> value of 3
# print(names[2]) # would print Phoebe to console

# friends = []
# friends.append("Joey") # add Joey to the end of "friends" list
# print(friends)
# friends.append("Chandler") # Chandler, Joey OR Joey, Chandler?
# print(friends)
# # insert Phoebe between Joey and Chandler
# friends.insert(1, "Phoebe") # (position, value)
# print(friends)
# friends.append("Ross") # [Joey, Phoebe, Chandler, Ross]
# print(friends)

# friends.append("Chandler")
# print(friends)

# print(friends.count("Chandler"))

# while friends.count("Chandler") > 0:
#     friends.remove("Chandler")

# print(friends)

# if "Chandler" in friends:
#     friends.remove("Chandler")
# else:
#     friends.append("Chandler")

# print(friends)

# friends.pop()
# print(friends)

# friends.append("Monica")
# print(friends)

# friends.pop(1) # remove element at index 1
# print(friends)

# if "Joey" in friends:
#     friends.remove("Joey")

# print(friends)

# if "Joey" not in friends:
#     friends.append("Joey")

# print(friends)

# friends.append("Joey")
# print(friends)
# print(friends.count("Joey")) #count number of occurrences of Joey in friends list

# # Matrices

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9]
# list_matrix = [list1, list2, list3] # -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(list_matrix[0][2])

# List Comprehension

# # x**2 from 0 to 10
# list1 = []
# for x in range(11):
#     list1.append(x**2)
# print(list1) # [0, 1, 2, 9, 16, 25, 36, ..., 100]

# list1 = [x**2 for x in range(11)]
# print(list1)

# # list only holds even numbers
# list2 = [x for x in range(11) if x%2==0]
# print(list2)

# Tuples
customer = "Ross Geller", "2016/04/13", 12
product = "Leather Pants", 79.99

print(f'The customer name is {customer[0]}')

samples = [
            ("Durham Region", "2021/06/26", 50),
            ("Durham Region", "2021/06/30", 26),
            ("Durham Region", "2021/07/10", 30)
        ]
# print(f'The number of cases in {samples[0][0]} on {samples[0][1]} is {samples[0][2]}')
for sample in samples:
    print(f'{sample[0]} had {sample[2]} cases on {sample[1]}')