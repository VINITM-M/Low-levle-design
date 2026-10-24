
from request import Request
from elevator_strategy import  NearestElevatorStrategy
from elevator.elevator_observer import Display
from elevator.elevator import Elevator

class ElevatorSystem: 
    def __init__(self, num_elevators: int):

        self.selection_strategy = NearestElevatorStrategy()

        elevator_list = [] 
        display = Display() 
        
        for i in range(1, num_elevators + 1):
            elevator = Elevator(i)
            elevator.add_observer(display)  # Attach the observer

            elevator_list.append(elevator)

    @classmethod
    def get_instance(cls, num_elevators: int):
        return cls(num_elevators)
    
    def start(self):
        for elevator in self.elevators.values():
            self.executor_service.submit(elevator.run)
    
    def request_elevator(floor:int, direction:Direction) :

        print(f"\n>> EXTERNAL Request: User at floor {floor} wants to go {direction.value}") 
        request = Request(floor, direction, RequestSource.EXTERNAL)

        #strategy to find the best elevator 
        selected_elevator = select_elevator(list(self.elevators.values()), request) 