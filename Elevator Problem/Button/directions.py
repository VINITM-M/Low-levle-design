class Directions: 

    def __init__(self, move):
        self.move = move

    def move_up(self):
        print("Lift is going UP") 
    
    def move_down(self):
        print("Lift is going down direction")


user_dir =  input("Enter a direction UP / DOWN/ IDLE: ") 

if user_dir.upper() == "UP": 

    obj1 = Directions(user_dir)
    obj1.move_up()

elif user_dir.upper() == 'DOWN':

    obj2 = Directions(user_dir) 
    obj2.move_down()