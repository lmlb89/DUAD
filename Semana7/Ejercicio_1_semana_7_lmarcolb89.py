# 1. Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# Suma
# Resta
# Multiplicación
# División
# Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator(previous_result=None):
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Delete current input")

    try:
        choice = input("Enter choice 1,2,3,4,5,): ")

        if choice == '5':
            print("Deleted current input. Please enter new numbers.")
            calculator()
            return

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid option.")
            calculator(previous_result)  
            return

        if previous_result is not None:
            num1 = previous_result
        else:
            num1 = int(input("Enter first number: "))

        num2 = int(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"{result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{result}")

        
        calculator(result)

    except ValueError as error:
        print(f"Invalid input: {error}")
        calculator(previous_result) 
    except Exception as error:
        print(f"An error occurred: {error}")
        calculator(previous_result) 

calculator()