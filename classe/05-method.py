# method 


class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        

    def speak(self ): # class cls = Dog
        print(f"Gaua! {self.__name}")
        
    @classmethod # method fo class
    def factory(cls):
        return cls("Felipe", 4)
        

my_dog = Dog.factory()


my_dog.speak()

my_dog.__name = "Camilo"
print(my_dog.__name)