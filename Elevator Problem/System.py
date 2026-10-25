
from actions.directions import Direction
import time 
from elevator.elevator_system import ElevatorSystem 

class System: 
    def main() :

        num_elevators = 1 
        elevator_system = ElevatorSystem.get_instance(num_elevators)

        # Start the elevator system
        elevator_system.start()
        print("Elevator system started. ConsoleDisplay is observing.\n")

    # ----------------------------- SIMULATION START ------------------------- 
    # 1. External Request: User at floor 5 wants to go UP.
 
        floor = input("Enter the floor number which you're in: ")

        elevator_system.request_elevator(int(floor), Direction.UP ) 
        time.sleep(0.3)


if __name__ == "__main__":
    System.main()