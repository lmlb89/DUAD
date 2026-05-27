# 5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#    1. Ejemplos:
#    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

number1 = int(input("Enter 10 numbers. Let's start with  the 1st number: "))
number2 = int(input("2nd: "))
number3 = int(input("3rd: "))
number4 = int(input("4th: "))
number5 = int(input("5th: "))
number6 = int(input("6th: "))
number7 = int(input("7th: "))
number8 = int(input("8th: "))
number9 = int(input("9th:"))
number10 = int(input("10th:"))

my_numbers = number1, number2, number3, number4, number5, number6, number7, number8, number9, number10

print(f"You entered: {my_numbers}")
print("The highest number is", max(my_numbers))
