
import elevator 
from Button import directions 



class  ElevatorSystem: 
    
    def main() :

        # Setup: A building with 2 elevators
        num_elevators = 2

        # The get_instance method now initializes the elevators and attaches the Display (Observer).
        elevator_system = elevator.get_instance(num_elevators)

        # Start the elevator system
        elevator_system.start()
        print("Elevator system started. ConsoleDisplay is observing.\n")

        # --- SIMULATION START ---

        # 1. External Request: User at floor 5 wants to go UP.
        # The system will dispatch this to the nearest elevator (likely E1 or E2, both at floor 1). 

        floor = input("Enter the floor number which you're in: ")
        direction = input("Enter which direction you need to go either up or down: ") 

        elevator_system.request(floor, directions(direction) )


if __name__ == "__main__":
    ElevatorSystem.main()