pets = ["Pelusa", "Flea" , "Felipe", "Chanchito Happy", "Felipe", "Flea"]


pets.insert(0, "Melvin") 

pets.append("Jose sad")
pets.remove("Flea")
pets.pop() # remove the last element
pets.pop(0)

del pets[0] # delete
pets.clear() # remove all elements
print(pets)