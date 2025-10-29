# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def week13_decorator(func):
    def function (*args):
        print(f"Input: {args}")
        result = func(*args)
        print(f"Output: {result}")
        return result
    return function


@week13_decorator
def add(a, b):
    return a + b

add(5, 5)