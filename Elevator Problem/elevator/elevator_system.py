
from concurrent.futures import ThreadPoolExecutor
from elevator.elevator_strategy import  NearestElevatorStrategy
from elevator.elevator_observer import Display
from elevator.elevator import Elevator
from actions.directions import Direction
from request.request_source import RequestSource 
from request.request import Request 
class ElevatorSystem: 

    def __init__(self, num_elevators: int):

        self.selection_strategy = NearestElevatorStrategy()
        self.executor_service = ThreadPoolExecutor(max_workers=num_elevators)

        elevator_list = [] 
        display = Display() 
        
        for i in range(1, num_elevators + 1):
            elevator = Elevator(i)
            elevator.add_observer(display)  # Attach the observer
            elevator_list.append(elevator)
        
        self.elevators = {elevator.get_id(): elevator for elevator in elevator_list} 
        self._initialized = True

    @classmethod
    def get_instance(cls, num_elevators: int):
        return cls(num_elevators)
    
    def start(self):
        for elevator in self.elevators.values():
            self.executor_service.submit(elevator.run)
    
    # EXTERNAL Request (Hall Call)
    def request_elevator(self, floor:int, direction:Direction) :

        print(f"\n>> EXTERNAL Request: User at floor {floor} wants to go {direction.value}")
        request = Request(floor, direction, RequestSource.EXTERNAL)

        # Use strategy to find the best elevator
        selected_elevator = self.selection_strategy.select_elevator(list(self.elevators.values()), request)

        if selected_elevator:
            selected_elevator.add_request(request)
        else:
            print("System busy, please wait.")