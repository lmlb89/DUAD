# 1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#    1. Ejemplos:
#    2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
#    `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
#    → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`


motorcycle_brand = ["BMW", "KTM", "Ducati", "Yamaha", "Honda", "Suzuki"]

country_of_origin = ["Germany", "Austria", "Italy", "Japan", "Japan", "Japan"]

my_dictionary = dict(zip(motorcycle_brand, country_of_origin))

print(my_dictionary)