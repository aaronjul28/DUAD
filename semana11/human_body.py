# 4. Cree las siguientes clases:
#     1. `Head`
#     2. `Torso`
#     3. `Arm`
#     4. `Hand`
#     5. `Leg`
#     6. `Feet`
#     7. Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos.

class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self,head,righ_arm,left_arm,left_leg,right_leg):
        self.head=head
        self.righ_arm=righ_arm
        self.left_arm=left_arm
        self.right_leg=right_leg
        self.left_leg=left_leg


class Arm:
    def __init__(self,hand):
        self.hand=hand

class Hand:
    def __init__(self):
        pass

class Leg:
    def __init__(self,feet):
        self.feet=feet

class Feet:
    def __init__(self):
        pass

#hand
right_hand=Hand()
left_hand=Hand()

#arm
right_arm=Arm(right_hand)
left_arm=Arm(left_hand)

#feet
right_feet=Feet()
left_feet=Feet()

#leg
right_leg=Leg(right_feet)
left_leg=Leg(left_feet)

#head
head=Head()


#torso
torso=Torso(head,right_arm,left_arm,left_leg,right_leg)