# 2. Cree un programa que use una lista para eliminar keys de un diccionario.
#    1. Ejemplos:
#    2. `list_of_keys = [’access_level’, ‘age’]`
#    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
#    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`

dictionary = {
    "country" : "USA",
    "state" : "Florida",
    "city" : "Doral",
    "street" : "25 ST",
    "apartment_number" : "102",
    "zip_code" : "33172",
}

keys = ["street", "apartment_number"]

for key in keys:
    dictionary.pop(key)

    print(dictionary)
    