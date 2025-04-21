# 4. Cree las siguientes clases:
#     1. `Head`
#     2. `Torso`
#     3. `Arm`
#     4. `Hand`
#     5. `Leg`
#     6. `Feet`
#     7. Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos.

class Human:
    def __init__(self,torso):
        self.torso=torso

    def __str__(self):
        return 'Human > Torso(head,righ_arm,left_arm,left_leg,right_leg)'

class Torso:
    def __init__(self,head,righ_arm,left_arm,left_leg,right_leg):
        self.head=head
        self.righ_arm=righ_arm
        self.left_arm=left_arm
        self.right_leg=right_leg
        self.left_leg=left_leg

    def __str__(self):
        return 'Torso > head,righ_arm,left_arm,left_leg,right_leg'

class Head:
    def __init__(self):
        pass
    
    def __str__(self):
        return 'Head'

class Arm:
    def __init__(self,hand):
        self.hand=hand

    def __str__(self):
        return 'Arm > hand'

class Hand:
    def __init__(self):
        pass

    def __str__(self):
        return 'Hand'

class Leg:
    def __init__(self,feet):
        self.feet=feet

    def __str__(self):
        return 'Leg > feet'

class Feet:
    def __init__(self):
        pass
    
    def __str__(self):
        return 'Feet '

#hand
right_hand=Hand()
left_hand=Hand()
print(right_hand)
print(left_hand)

#arm
right_arm=Arm(right_hand)
left_arm=Arm(left_hand)
print(right_arm)
print(left_arm)

#feet
right_feet=Feet()
left_feet=Feet()
print(right_feet)
print(left_feet)

#leg
right_leg=Leg(right_feet)
left_leg=Leg(left_feet)
print(right_leg)
print(left_leg)


#head
head=Head()
print(head)

#torso
torso=Torso(head,right_arm,left_arm,left_leg,right_leg)
print(torso)

#human
human=Human(torso)
print(human)