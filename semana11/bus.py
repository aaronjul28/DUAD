class Bus():
    max_passengers=input('Enter the max number of passengers: ')
    max_passengers=int(max_passengers)
    def add_passengers(person):
        passenger_list=[]
        passenger_list.append(person)
        return passenger_list
        
class Person():
    def __init__(self,name):
        self.name=name
        return name

max_passengers=Bus.max_passengers
passenger_onboarding=Person.__init__(input('Enter Passenger name: '))
Bus.add_passengers(passenger_onboarding)
