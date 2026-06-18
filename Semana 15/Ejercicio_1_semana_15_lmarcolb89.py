
# Crea un bubble_sort por tu cuenta sin revisar el código de la lección.



def bubble_sort(list):

    n = len(list)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    return list

numbers = [100, 90, 120, 80, 70, 60, 130, 190]
sorted_numbers = bubble_sort(numbers.copy())
print("Original list:", numbers)
print("Sorted list:", sorted_numbers)
