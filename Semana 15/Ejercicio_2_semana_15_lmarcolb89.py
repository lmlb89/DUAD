
# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).



def reverse_bubble_sort(list):

    n = len(list)
    
    for i in range(n):
        for j in range(n-i-1, 0):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    return list

numbers = [100, 90, 120, 80, 70, 60, 130, 190]
sorted_numbers = reverse_bubble_sort(numbers.copy())
print("Original list:", numbers)
print("Sorted list:", sorted_numbers)