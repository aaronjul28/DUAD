#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def print_attributes(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        print(result)
        return result
    return wrapper

class Person():
    @print_attributes
    def person_data(self,name,age):
        return age , name
    
    @print_attributes    
    def bio_data(self,weight,height):
        return weight,height


person=Person()
person.person_data('Aaron',25)
person.person_data(76,1.80)