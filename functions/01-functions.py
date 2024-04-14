
def greet(name, lastName="Not"):
    if lastName == "Not":
        print(f"Hello {name}, how are you?")
    else:
        print(f"Hello {name} {lastName}, how are you?")
        
    
greet("Jose")    
greet("Camilo", "Andrade")









# Arguments named 
greet(lastName="Martinez", name="Gabriela")
