

# Analice el algoritmo de bubble_sort usando la Big O Notation.


def bubble_sort(list):

    n = len(list)
    
    for i in range(n): # O(n)
        for j in range(0, n-i-1): # O(n)
            if list[j] > list[j+1]: # O(1)
                list[j], list[j+1] = list[j+1], list[j] # O(1)
    
    return list # O(1)

numbers = [100, 90, 120, 80, 70, 60, 130, 190] # O(1)
sorted_numbers = bubble_sort(numbers.copy()) # O(1)
print("Original list:", numbers) # O(1)
print("Sorted list:", sorted_numbers) # O(1)



