nums = [1, 2, 3, 4, 5] #integer list
names = ["Rachel", "Monica", "Phoebe", "Ross", "Joey", "Chandler"] #list of strings

print(nums[2])
print(names[2])

friends = []
friends.append("Joey")
print(friends)
friends.append("Chandler") # Chandler, Joey OR Joey, Chandler?
print(friends)
# insert Phoebe between Joey and Chandler
friends.insert(1, "Phoebe") # (position, value)
print(friends)
friends.append("Ross") # [Joey, Phoebe, Chandler, Ross]
print(friends)

friends.remove("Chandler")
print(friends)

friends.pop()
print(friends)

friends.append("Monica")
print(friends)

friends.pop(1) # remove element at index 1
print(friends)

if "Joey" in friends:
    friends.remove("Joey")

print(friends)

if "Joey" not in friends:
    friends.append("Joey")

print(friends)

friends.append("Joey")
print(friends)
print(friends.count("Joey")) #count number of occurrences of Joey in friends list
