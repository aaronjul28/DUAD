
class Person():
    def __init__(self, name):
        print(f"Ha nacido una persona llamada {name}!")
        self.age = 0
person_1 = Person("John")
print(person_1.age)