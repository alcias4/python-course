# sets = collection


first = {1,1,2,2,3,3,4,5,6} # python remove duplicates

first.add(7)
first.remove(1)

second = [3,2,5]
second = set(second) # create a set from an iterable 
print(second)
print(first | second) # join 
print(first & second) # intersection
print(first - second) # remove from first set the elements that are  in the  second set
print(first ^ second) # do not match between sets
