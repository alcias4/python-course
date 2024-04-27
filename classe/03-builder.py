# builder of class


class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.ege = age

        
        
    def speaks(self):
        print(f"i am {self.ege} years  old, i am dog")
        

my_dog = Dog("Camilo", 23)
my_dog_2 = Dog("Felipe", 1)


my_dog.speaks()