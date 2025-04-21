# 1. Un atributo de `max_passengers`.
# 2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
# 3. Un método para bajar pasajeros uno por uno (en cualquier orden).
import random
class Bus():

    def __init__(self):
        self.max_passengers=input('Enter the max number of passengers: ')
        self.max_passengers=int(self.max_passengers)
        self.passenger_list=[]
    def add_passengers(self,person):

        if len(self.passenger_list)+1 <= self.max_passengers:
            self.passenger_list.append(person.name)
            print(f'The passenger {person.name} has entered the bus.')
            #CHECK IF THE LIST IS INCREASING
            #print(self.passenger_list)
            return self.passenger_list

        else:
            print('The bus is Full')
    
    def remove_passengers(self):
        #print(self.passenger_list)
        #CHECK LEN OF LIST
        #print(len(self.passenger_list))
        number=random.randint(0,len(self.passenger_list)-1)
        #CHECK RANDOM NUMBER USED
        #print(number)
        self.passenger_list.pop(number)
        print('A passenger has left the bus.')


class Person():
    def __init__(self,name):
        self.name=name

#DEFINE THE MAX NUMBER OF PASSENGERS
add_passenger=Bus()
#DEFINE WHO IS ENTERING THE BUS
passenger_onboarding1=Person('Aaron')
passenger_onboarding2=Person('Jaz')
passenger_onboarding3=Person('Dani')
passenger_onboarding4=Person('Meli')
passenger_onboarding5=Person('Gabri')
#ADD PASSENGER TO THE PASSENGER LIST ON BUS ADD PASSENGERS CLASS
add_passenger.add_passengers(person=passenger_onboarding2)
add_passenger.add_passengers(person=passenger_onboarding1)
add_passenger.add_passengers(person=passenger_onboarding3)
add_passenger.add_passengers(person=passenger_onboarding4)
add_passenger.add_passengers(person=passenger_onboarding5)

#REMOVE PASSENGER
add_passenger.remove_passengers()

#ADD ONE LAST PASSENGER TO TEST REMOVE AND ADD PASSENGERS
passenger_onboarding5=Person('Gabri')
add_passenger.add_passengers(person=passenger_onboarding5)