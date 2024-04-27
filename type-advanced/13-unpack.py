



number = [1,2,3,4,5]

print(number)


print(*number)


number2 = [5,6,7]

join = [*number, *number2]

point_1 = {"x": 19}
point_2 = {"y": 15}

new_point = {**point_1, **point_2}

print(new_point)