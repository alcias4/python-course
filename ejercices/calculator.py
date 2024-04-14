# Calculator
import os




while True:
    os.system("clear")
    print("""
---- Welcome: Calculator ----
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Exit
        """)
    command = int(input("Enter a number from one to four: "))
    if command == 1:
        os.system("clear")
        print("---- Addition ----")
        number_one = float(input("Enter number one: "))
        number_second = float(input("Enter second number: "))
        print(f"Result addition is : {number_one + number_second}")
        input("$")
    elif command == 2:
        os.system("clear")
        print("---- Subtraction ----")
        number_one = float(input("Enter number one: "))
        number_second = float(input("Enter second number: "))
        print(f"Result Subtraction  is : {number_one - number_second}")
        input("$")
    elif command == 3:
        os.system("clear")
        print("---- Multiplication ----")
        number_one = float(input("Enter number one: "))
        number_second = float(input("Enter second number: "))
        print(f"Result Multiplication is : {number_one * number_second}")
        input("$")
    elif command == 4:
        os.system("clear")
        print("---- Division ----")
        number_one = float(input("Enter number one: "))
        number_second = float(input("Enter second number: "))
        if number_second != 0: 
            print(f"Result Division is : {number_one / number_second}")
            input("$")
    elif command == 5:
        break