
# 1. Cree los siguientes unit tests para el algoritmo `bubble_sort`:
#    1. Funciona con una lista pequeña.
#    2. Funciona con una lista grande (de más de 100 elementos.)
#    3. Funciona con una lista vacía.
#    4. No funciona con parámetros que no sean una lista.


import unittest
import random

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

class TestBubbleSort(unittest.TestCase):

    def test_1_small_list(self):
        input_list = [5, 2, 8, 1, 9]
        expected = [1, 2, 5, 8, 9]
        result = bubble_sort(input_list.copy())
        self.assertEqual(result, expected)
        
        self.assertTrue(all(result[i] <= result[i+1] for i in range(len(result)-1)))

    def test_2_large_list(self):
        large_list = [random.randint(1, 1000) for _ in range(100)]
        
        expected = sorted(large_list.copy())
        result = bubble_sort(large_list.copy())
        
        self.assertTrue(all(result[i] <= result[i+1] for i in range(len(result)-1)))
        

    def test_3__empty_list(self):
        input_list = []
        expected = []
        result = bubble_sort(input_list.copy())
        
        self.assertEqual(result, expected)
        self.assertEqual(len(result), 0)

    def test_4_non_list_items(self):

        with self.assertRaises(TypeError):
            bubble_sort("not a list")
        
        with self.assertRaises(TypeError):
            bubble_sort(42)
        

if __name__ == '__main__':

    unittest.main(verbosity=2)