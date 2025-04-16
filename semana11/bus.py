import random
class Person:
    def __init__(self, name):
        self.name=name


class Bus:

    def __init__(self,max_passengers):
        self.max_passengers=max_passengers
        self.onboard_passengers=[]

    def add_passengers(self,person):
        if len(self.onboard_passengers)< self.max_passengers:
            self.onboard_passengers.append(person)
            print(f'Passenger {person.name} is onboarding the bus')

        else:
            print('Sorry,the Bus is full')

    def drop_passengers(self):
        if len(self.onboard_passengers) != 0 :
            passenger_dropped=random.randint(0,len(self.onboard_passengers)-1)
            self.onboard_passengers.pop(passenger_dropped)
            print(f'A passenger is leaving the Bus')

bus_passengers= Bus(max_passengers=3)


p1=Person("Aaron")
p2=Person("Jaz")
p3=Person("Dani")
p4=Person("Ale")

bus_passengers.add_passengers(p1)
bus_passengers.add_passengers(p2)
bus_passengers.add_passengers(p3)
bus_passengers.add_passengers(p4)
bus_passengers.add_passengers(p4)
bus_passengers.drop_passengers()
bus_passengers.drop_passengers()
bus_passengers.add_passengers(p4)

