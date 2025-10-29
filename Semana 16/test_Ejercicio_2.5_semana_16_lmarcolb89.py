# 2. Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6 (*exceptuando el 1 y 2*).
#    1. [Ejercicios de Funciones](https://www.notion.so/Ejercicios-de-Funciones-3f5364b6d2504ed29663eb4bdc983a0e?pvs=21)


# Instrucciones Semana 6: 
# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

def check_for_prime_numbers(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def user_input():
    input_numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in input_numbers.split()]
    prime_numbers = [num for num in numbers if check_for_prime_numbers(num)]
    print("Prime numbers in the list:", prime_numbers)

def find_primes_in_list(number_list):
    return [num for num in number_list if check_for_prime_numbers(num)]




import unittest

class TestPrimeNumbers(unittest.TestCase):

    def test_large_list_of_numbers(self):
        test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19]
        
        result = find_primes_in_list(test_numbers)
        self.assertEqual(result, expected_primes)
    
    def test_no_prime_numbers(self):
        test_numbers = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28]
        
        result = find_primes_in_list(test_numbers)
        self.assertEqual(result, [])  
    
    def test_with_letters_handling(self):
        with self.assertRaises(ValueError):
            numbers = [int(num) for num in ["1", "2", "a", "4"]]

if __name__ == '__main__':
    unittest.main()
