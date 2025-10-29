#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.


from functools import wraps

def require_numeric_parameters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"All parameters must be numbers.")
        

        for arg_name, arg_value in kwargs.items():
            if not isinstance(arg_value, (int, float)):
                raise TypeError(f"Parameter '{arg_name}' must be a number. Got {type(arg_value)}")
        
        return func(*args, **kwargs)
    return wrapper

@require_numeric_parameters
def add_numbers(a, b):
    return a + b


print(add_numbers(100, 200)) 

add_numbers("100", 200) 
add_numbers(1, b="two") 