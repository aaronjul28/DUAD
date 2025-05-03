# Cree una clase de User que:
# - Tenga un atributo de `date_of_birth`.
# - Tenga un property de `age`.

# Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

import datetime

def adult_check(func):
    def wrapper(user, *args):
        if user.age >= 18:
            print('El usuario ingresado es mayor de edad')
        else:
            raise ValueError('El usuario es menor de edad')
        func(user, *args)
    return wrapper



class User:
#expected format day/month/year
    def __init__(self, date_of_birth):
        date_of_birth=date_of_birth.split('/')
        self.date_of_birth=date_of_birth

    @property
    def age(self):
        current_time=datetime.datetime.now()
        current_age=(current_time.year-int(self.date_of_birth[2]))-1
        if current_time.month >= int(self.date_of_birth[1]) and current_time.day >= int(self.date_of_birth[0]):
            current_age=current_age+1
        return current_age

@adult_check
def  adult_check2(user):
    print(f'La persona tiene {user.age} años.')


person=User('05/07/1999')
adult_check2(person)