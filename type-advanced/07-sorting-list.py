number = [2, 35,521, 531,1,3,5]

# number.sort(reverse=True)
number_second = sorted(number, reverse=True) # ->  return new list

print(number)
print(number_second)


users = [[4, "Camilo"], [1,"Jose"], [5,"Flea"]] # start position id 

users.sort()
print(users)

users_second = [["Camilo", 4], ["Jose", 2], ["Manuel", 1]]


def order(element):
    return element[1]

users_second.sort(key=order, reverse=True)
print(users_second)