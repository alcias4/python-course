

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"Product: {self.name} - price: {self.price}"
    
    
    
    
class Category:
    products = []
    
    def __init__(self, name, products):
        self.name = name
        self.products = products
        
    
    def add(self, product):
        self.products.append(product)
        
        
    def showProducts(self):
        for product in self.products:
            print(product)
            

kayak = Product("Kayak", 1000)
bicycle = Product("Bicycle", 750)
sufboard = Product("Sufboard", 500)

sports = Category("Sports", [kayak, bicycle])

sports.add(sufboard)
sports.showProducts()
