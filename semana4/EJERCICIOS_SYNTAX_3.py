import random

random_number=random.randint(0,10)
#print(random_number)

guess_number=int(input('Guess a number between 0 and 10: '))

while (guess_number != random_number):
    guess_number=int(input('Ups! Try another number: '))

print(f"Well done, the secret number was {random_number}")

#I HAD TO SPECIFY THE DATA TYPE, OTHERWISE IT WOULD NEVER UNDERSTAND THE NUMBERS WERE EQUAL