# Private


class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    
    def get_name(self):
        return self.__name   
    
    def set_name(self, name):
        self.__name = name

    def speak(self ): # class cls = Dog
        print(f"Gaua! {self.__name}")
        
    @classmethod # method fo class
    def factory(cls):
        return cls("Felipe", 4)
        

my_dog = Dog.factory()


my_dog.speak()

print(my_dog._Dog__name) # dictionary contain the property