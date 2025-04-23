#CONTROLLER

#HERE WE WELL DEFINE AN ATTRIBUTE FOR EACH ONE OF THE ARROWS AND PRINT > MOVE TO XXXX
class Arrows:
    
    def up_arrow(self):
        return 'You moved up'
    def down_arrow(self):
        return 'You moved down'
    def left_arrow(self):
        return 'You moved left'
    def right_arrow(self):
        return 'You moved right'

#HERE WE WELL DEFINE AN ATTRIBUTE FOR EACH ONE OF THE BUTTON AND PRINT > YOU XXXX 
class Buttons:
    def circle(self):
        return 'You Kicked'
    def square(self):
        return 'You Punched'
    def cross(self):
        return 'You Jumped'
    def triangle(self):
        return 'You Couched'

#THIS CHILD CLASS INHERITED BOTH PLAY AND BUTTONS
class Play(Arrows,Buttons):
    pass

action=Play()

#TEST INHERIT ARROW
print(action.up_arrow())
print(action.down_arrow())
print(action.left_arrow())
print(action.right_arrow())

#TEST INHERIT BUTTONS
print(action.circle())
print(action.square())
print(action.triangle())
print(action.cross())
