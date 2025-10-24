
# 2. Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6 (*exceptuando el 1 y 2*).
#    1. [Ejercicios de Funciones](https://www.notion.so/Ejercicios-de-Funciones-3f5364b6d2504ed29663eb4bdc983a0e?pvs=21)

# Instrucciones Semana 6: 
# 4. Cree una función que le de la vuelta a un string y lo retorne.
#    1. Esto ya lo hicimos en iterables.
#    2. “Hola mundo” → “odnum aloH”

import unittest
from io import StringIO
import sys

def backwards_test():
    backwards = "Just testing, don't worry"
    return print(backwards[::-1])

class TestBackwardsTest(unittest.TestCase):
    
    def test_output_contains_numbers_when_present(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        
        backwards_test()
        
        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__
        
        expected = "yrrow t'nod ,gnitset tsuJ"
        self.assertEqual(output, expected)
    
    def test_lowercase_uppercase_preservation(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        
        backwards_test()
        
        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__
        
        self.assertTrue(output[0].islower())  
        self.assertTrue(output[-1].isupper())  
    
    def test_long_string_reversal(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        
        backwards_test()
        
        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__
        
        original_length = len("Just testing, don't worry")
        self.assertEqual(len(output), original_length)
        

        self.assertEqual(output[0], 'y')  
        self.assertEqual(output[-1], 'J')  

if __name__ == '__main__':
    unittest.main()