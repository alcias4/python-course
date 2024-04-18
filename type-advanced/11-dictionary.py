
# Dictionary 


point = {
    "x":25,
    "y":50
    }

point["z"] = 10


if "lala" in point:
    print("lala", point["lala"])

print(point)

print(point.get("x")) # value
print(point.get("lala", 100)) # value default

del point["x"]

print(point)

for value in point:
    print(point.get(value))
    
for key , value in point.items(): # return tuples
    print(key, value)
    
users = [
    {"id": 1, "name":  "Camilo"},
    {"id": 2, "name":  "Jose"},
    {"id": 3, "name":  "Nicolas"},
    {"id": 4, "name":  "Juan"},
]

for user in users:
    print(user["name"])