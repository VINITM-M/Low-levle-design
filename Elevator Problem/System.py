
import elevator 
from Button.directions import Directions 
import sys
from 
from elevator.elevator_system import ElevatorSystem 

class ElevatorSystemDemo: 
    
    def main() :

        num_elevators = 1 
        elevator_system = ElevatorSystem.get_instance(num_elevators)

        # Start the elevator system
        elevator_system.start()
        print("Elevator system started. ConsoleDisplay is observing.\n")

        # --- SIMULATION START ---
        # External Request: User at floor 5 wants to go UP.
 
        floor = input("Enter the floor number which you're in: ")
        direction = input("Enter which direction you need to go either up or down idle: ") 

        elevator_system.request_elevator(floor, Directions(direction) ) 
        time.sleep(0.3)




if __name__ == "__main__":
    ElevatorSystem.main()