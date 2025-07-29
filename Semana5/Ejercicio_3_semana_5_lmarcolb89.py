# 3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
#    1. Ejemplos:
#    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list[0], my_list[-1] = my_list[-1], my_list[0]

print("List after swapping first and last elements:", my_list)