# 3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
    #1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random

random_number = random.randint(1, 10)

number = int(input("Guess the secret number. Enter a number between 1 and 10: "))

while number != random_number:
        print("Try again")
        number = int(input("New attempt: "))
        
if (number == random_number):
		print ("You won!")

        