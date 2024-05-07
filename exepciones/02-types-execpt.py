try:
    n1 = int(input("Ingresa primer número: "))

except ValueError as e: #Exception
    print("Ingresa un valor que corresponda !")

except NameError as e:
    print("Codigo mas escrito ej: dfsafs ")