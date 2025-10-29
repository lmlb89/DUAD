# 2. Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6 (*exceptuando el 1 y 2*).
#    1. [Ejercicios de Funciones](https://www.notion.so/Ejercicios-de-Funciones-3f5364b6d2504ed29663eb4bdc983a0e?pvs=21)

# Instrucciones Semana 6: 
# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def sorting_phrase():
    phrase = "this-is-a-random-list-of-words-like-resume-company-position-that-we-need-to-sort-alphabetically"
    new_phrase = phrase.split("-")
    new_phrase.sort()
    final = ' '.join(new_phrase)
    return print(final)

sorting_phrase()

import unittest
from io import StringIO
import sys

class TestSortingPhrase(unittest.TestCase):

    def test_string_with_no_dash(self):
        code = """
def sorting_phrase():
    phrase = "hello world python programming"
    new_phrase = phrase.split("-")
    new_phrase.sort()
    final = ' '.join(new_phrase)
    return print(final)
"""
        exec(code, globals())
        
        captured_output = StringIO()
        sys.stdout = captured_output
        globals()['sorting_phrase']()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue().strip()
        expected = "hello world python programming"
        self.assertEqual(output, expected)

    def test_long_string_of_text(self):
        long_phrase = "the-quick-brown-fox-jumps-over-the-lazy-dog-and-then-runs-very-fast-through-the-forest-while-chasing-a-small-rabbit-that-is-trying-to-escape-from-the-hungry-fox"
        
        code = f"""
def sorting_phrase():
    phrase = "{long_phrase}"
    new_phrase = phrase.split("-")
    new_phrase.sort()
    final = ' '.join(new_phrase)
    return print(final)
"""
        exec(code, globals())
        
        captured_output = StringIO()
        sys.stdout = captured_output
        globals()['sorting_phrase']()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue().strip()
        words = output.split()
        self.assertEqual(words, sorted(words))

    def test_string_with_numbers(self):
        code = """
def sorting_phrase():
    phrase = "5-product-2-item-1-10-test-3"
    new_phrase = phrase.split("-")
    new_phrase.sort()
    final = ' '.join(new_phrase)
    return print(final)
"""
        exec(code, globals())
        
        captured_output = StringIO()
        sys.stdout = captured_output
        globals()['sorting_phrase']()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue().strip()
        expected = "1 10 2 3 5 item product test"
        self.assertEqual(output, expected)

if __name__ == '__main__':

    unittest.main()