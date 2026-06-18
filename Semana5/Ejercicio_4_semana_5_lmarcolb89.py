# 4. Cree un programa que elimine todos los números impares de una lista.
#    1. Ejemplos:
#    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

removing_odd_numbers = [num for num in my_list if num %2 ==0]

print(removing_odd_numbers)

