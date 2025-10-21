
# 2. Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6 (*exceptuando el 1 y 2*).
#    1. [Ejercicios de Funciones](https://www.notion.so/Ejercicios-de-Funciones-3f5364b6d2504ed29663eb4bdc983a0e?pvs=21)

# Instrucciones Semana 6: 
# 4. Cree una función que le de la vuelta a un string y lo retorne.
#    1. Esto ya lo hicimos en iterables.
#    2. “Hola mundo” → “odnum aloH”

import unittest

def backwards_test():
    backwards = "Just testing, don't worry"
    return print(backwards[::-1])
    return backwards[::-1]


def process_list(input_list):
    processed_list = [item.upper() if isinstance(item, str) else item for item in input_list]
    return processed_list[::-1]

import unittest

class TestProcessList(unittest.TestCase):

    def test_numbers_in_list(self):
        input_list = [1, 2, 3, 4, 5]
        result = process_list(input_list)
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(result, expected)

    def test_lowercase_uppercase_mixed(self):
        input_list = ['hello', 'WORLD', 'MIXEd', 'CASE']
        result = process_list(input_list)
        expected = ['CASE', 'MIXED', 'WORLD', 'HELLO']
        self.assertEqual(result, expected)

    def test_long_list(self):
        input_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        result = process_list(input_list)
        expected = ['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()