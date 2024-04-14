

# for - else
numberSearch = 10


for number in range(5): # Iterable 
    if number == numberSearch:
        print(f"Number found is: {number}")
        break
else:  
    print("Number not found")


# Second example

# List , Tuples , string


name = "Camilo Andrade"

for char in name:
    print(char)