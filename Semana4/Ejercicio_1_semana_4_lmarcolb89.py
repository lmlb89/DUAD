#1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
   # 1. Si le salen errores, **no se asuste.** Lealos e intente comprender qué significan.
    #*Los errores son oportunidades de aprendizaje.*
    #2. Por ejemplo:
    #   1. string + string → ?
    #  2. string + int → ?
    # 3. int + string → ?
    #4. list + list → ?
    # 5. string + list → ?
    #6. float + int → ?
    #7. bool + bool → ?

#string + string

test = "This is a test"
test2 = "This is a second test"

print(test + test2)

#string + int

print(test + 5)

#int + string

print(10 + test2)

#list + list

my_test_list = [1, 2, 3, 4, 5]

my_test2_list = [6, 7, 8, 9, 10]

print(my_test_list + my_test2_list)

#string + list

print(test + my_test_list)

#float + int

new_float = 2.5

print( 3 + new_float)

#bool + bool

false_boolean = False
true_boolean = True

print(false_boolean + true_boolean)
