# 2. Experimente con el concepto de scope:
#    1. Intente accesar a una variable definida dentro de una función desde afuera.
#    2.  Intente accesar a una variable global desde una función y cambiar su valor.

#Commenting on exercise #1 so that number 2 can run (number 1 gives an expected error) 

# def test_function():
#    internal_variable = 100
#    print(internal_variable)

# print(f"{internal_variable}")

#Result =     print(f"{internal_variable}")
#             ^^^^^^^^^^^^^^^^^
# NameError: name 'internal_variable' is not defined


global_variable = 200

def scope_test():
    global global_variable
    global_variable= 400
    print(global_variable)

scope_test()

