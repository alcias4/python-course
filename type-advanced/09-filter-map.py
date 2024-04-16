
users = [
    ["Camilo", 3],
    ["Jose", 1],
    ["Martin", 19]
]

name = list(map(lambda user: user[0], users))

filter_name = list(filter(lambda user: user[1] > 2 , users))

print(filter_name)