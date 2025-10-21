
# 2. Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6 (*exceptuando el 1 y 2*).
#    1. [Ejercicios de Funciones](https://www.notion.so/Ejercicios-de-Funciones-3f5364b6d2504ed29663eb4bdc983a0e?pvs=21)

# Instrucciones Semana 6: 
# 3. Cree una función que retorne la suma de todos los números de una lista.
#    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#    2. [4, 6, 2, 29] → 41

import unittest

def sum_numbers():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return print(sum(my_list))

def sum_numbers(numbers):
    return sum(numbers)


class TestSumNumbers(unittest.TestCase):
    
    def test_small_list(self):
        result = sum_numbers([1, 2, 3])
        assert result == 6, f"Expected 6, got {result}"
            
    def test_large_list(self):
        result = sum_numbers([10, 20, 30, 40, 50])
        assert result == 150, f"Expected 150, got {result}"
            
    def test_empty_list(self):
        result = sum_numbers([])
        assert result == 0, f"Expected 0, got {result}"

if __name__ == '__main__':

    unittest.main(verbosity=2)