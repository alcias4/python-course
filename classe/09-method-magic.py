

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self): # se ejecuta cuando se elemine la clase
        print(f"chao perro :{self.name}")
        
    def __str__(self):
        return f"clase perro: {self.name}"
    def speak(self):
        print(f"{self.name} say: Gua!")



dog = Dog("Camilo", 2)

del dog


