# 3. Cree una clase de `User` que:
#    - Tenga un atributo de `date_of_birth`.
#    - Tenga un property de `age`.
#    
#    Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import datetime, date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

def check_adult(func):
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("The first argument must be a User instance")
        if user.age < 18:
            raise ValueError("User must be at least 18 years old")
        return func(user, *args, **kwargs)
    return wrapper


@check_adult
def perform_adult_action(user):
    print(f"Action performed for user aged {user.age}")

adult_user = User(date(1990, 1, 1))
perform_adult_action(adult_user) 

child_user = User(date(2010, 1, 1))
perform_adult_action(child_user)  