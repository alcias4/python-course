# property 


class Dog: 
    paws = 4
    def __init__(self, name, age):
        self.name = name
        self.ege = age

        
        
    def speaks(self):
        print(f"i am {self.ege} years  old, i am dog")
        

Dog.paws = 14 # update paws for all the class

my_dog = Dog("Camilo", 23)

my_dog.speaks()

print(my_dog.paws)