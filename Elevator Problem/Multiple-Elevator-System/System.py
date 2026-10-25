
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

    # 2. Internal Request: Assume E1 took the previous request.
        # The user gets in at floor 5 and presses 10.
        # We send this request directly to E1.

        # Note: In a real simulation, we'd wait until E1 reaches floor 5, but for this demo,
        # we simulate the internal button press shortly after the external one

        elevator_system.select_floor(1, 10)
        time.sleep(0.2)

     # 3. External Request: User at floor 3 wants to go DOWN.
        # E2 (likely still idle at floor 1) might take this, or E1 if it's convenient.
        elevator_system.request_elevator(3, Direction.DOWN)
        time.sleep(0.3)

        # 4. Internal Request: User in E2 presses 1.
        elevator_system.select_floor(2, 1)

        # Let the simulation run for a while to observe the display updates
        print("\n--- Letting simulation run for 1 second ---")
        time.sleep(1)

        # Shutdown the system
        elevator_system.shutdown()
        print("\n--- SIMULATION END ---")
    



if __name__ == "__main__":
    System.main()