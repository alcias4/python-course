# decorate property


class Dog:
    def __init__(self, name):
        self.name = name
    
    
    @property # only for function that return value
    def name(self):
        print("getter")
        return self.__name
    
    
    @name.setter
    def name(self, name):
        print("setter")
        if name.strip():
            self.__name = name
        return
    
dog = Dog("Camilo")

print(dog.name)
