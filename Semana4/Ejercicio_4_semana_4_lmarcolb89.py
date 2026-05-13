#Cree un programa que le pida tres números al usuario y muestre el mayor.


number1 = int(input("Enter the first number: "))
number2 = int(input("enter the second number: "))
number3 = int(input("Enter the third number:"))

highest = max(number1, number2, number3)

print(f"The highest number is: {highest}")