
#Cree un programa que le pida al usuario su nombre, apellido, y age, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.


name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if (age < 2):
    print ("Your are a baby")
elif (age < 10):
        print("You are a child")
elif(age < 14):
        print("You are a pre-teen")
elif(age < 18):
        print("You are a teenager")
elif(age < 25):
        print("You are a young adult")
elif(age < 65):
        print("You are an adult")
elif(age > 65):
        print("You are a senior citizen")