#Compression list


users = [
    ["Camilo", 3],
    ["Jose", 1],
    ["Martin", 19]
]

name = [user[0] for user in users] # Transform list

# filter_name = [user for user in users if user[1] > 2] #  just filter
filter_name = [user[0] for user in users if user[1] > 2] # just filter and transform
print(filter_name)