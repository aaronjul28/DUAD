#7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
# [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
# Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.

#https://byjus.com/maths/how-to-find-prime-numbers/


def create_list():
    number_list=[]
    condition='yes'
    while condition!='no':
        number_list.append(input('Enter a number to add to the list: '))
        condition=input('Would you like to add another number?: ')

    return number_list

def check_prime():
    original_list=create_list()
    prime_list=[]

    for number in original_list:
        #working with less that 10
        if len(number) < 2:
            prime_one_to_ten=[2,3,5,7]
            if int(number) in prime_one_to_ten:
                prime_list.append(number)
        
        if len(number) > 1:
            value=str(number)
            value_list=[]
            sum_values=0
            blacklist_numbers=[0,2,4,6,8]
            for i in value:
                value_list.append(i)
            
            for i in value_list:
                sum_values=sum_values+int(i)


            if int(number) % 5 == 0 or int(number) % 2 == 0 or sum_values%3 == 0 :
                prime_list=prime_list
            else:
                prime_list.append(number)


    return prime_list

# EXPECTED OUTPUT 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
print(check_prime())


