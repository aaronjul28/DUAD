#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def first_print():
    first_phrase = 'This is the first print'
    return first_phrase, second_print()
    

def second_print():
    second_phrase= 'This is the second print'
    return second_phrase

print(first_print())