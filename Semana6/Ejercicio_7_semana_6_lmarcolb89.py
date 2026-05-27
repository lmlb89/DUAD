# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

def check_for_prime_numbers(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def user_input():
    input_numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in input_numbers.split()]
    prime_numbers = [num for num in numbers if check_for_prime_numbers(num)]
    print("Prime numbers in the list:", prime_numbers)


user_input()
