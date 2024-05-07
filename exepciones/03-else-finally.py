
try:
    n1 = int(input("Ingresa primer número: "))
except ValueError as e: #Exception
    print("Ingresa un valor que corresponda !")
else:
    print("No ocurrio ningu error")
finally:
    print("Se ejecuta siempre")