# 2. Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6 (*exceptuando el 1 y 2*).
#    1. [Ejercicios de Funciones](https://www.notion.so/Ejercicios-de-Funciones-3f5364b6d2504ed29663eb4bdc983a0e?pvs=21)

# Instrucciones Semana 6: 
# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def lowercase_and_uppercase_count(text):
    lower = 0
    upper = 0
    for i in text:
        if i.islower():
            lower += 1
        if i.isupper():
            upper += 1
    return lower, upper 

original_text = "In here we are mixing both Uppercase and Lowercase for PRACTICING purposes only"
lower_count, upper_count = lowercase_and_uppercase_count(original_text)
print("Lowercase count is:", lower_count)
print("Uppercase count is:", upper_count)

import unittest

class TestLetterCountSimple(unittest.TestCase):

    def test_all_lowercase(self):
        lower, upper = lowercase_and_uppercase_count("hello world python")
        self.assertEqual(lower, 16)
        self.assertEqual(upper, 0)

    def test_all_uppercase(self):
        lower, upper = lowercase_and_uppercase_count("HELLO WORLD PYTHON")
        self.assertEqual(lower, 0)
        self.assertEqual(upper, 16)

    def test_mixed_case_long_string(self):
        lower, upper = lowercase_and_uppercase_count("This Is A Long String With MANY Different CASE Letters TO Test The Counting FUNCTIONALITY")
        self.assertEqual(lower, 41)
        self.assertEqual(upper, 34)

if __name__ == '__main__':
    unittest.main()


