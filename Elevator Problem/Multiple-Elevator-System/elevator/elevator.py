import threading 
import time 
from typing import Set
from elevator.elevator_state import ElevatorState, IdleState
from elevator.elevator_observer import ElevatorObserver
from request.request import Request
from actions.directions import Direction 

class Elevator:
    def __init__(self, elevator_id: int):

        self.id = elevator_id   
        self.current_floor = 1
        self.current_floor_lock = threading.Lock()
        self.state = IdleState() 

        self.up_requests = set()
        self.down_requests = set()
        self.is_running = True 

        # Observer Pattern: List of observers
        self.observers = []

     # --- State Pattern Methods ---
    def set_state(self, state: ElevatorState):
        self.state = state
        self.notify_observers()  # Notify observers on direction change
    
    def move(self):
        self.state.move(self)
    
    def get_up_requests(self) -> Set[int]:
        return self.up_requests 

    def get_down_requests(self) -> Set[int]:
        return self.down_requests

    def set_current_floor(self, floor: int):
        with self.current_floor_lock:
            self.current_floor = floor
        self.notify_observers()  # Notify observers on floor change 
    
    def get_current_floor(self) -> int:
        with self.current_floor_lock:
            return self.current_floor
        
    # --- Observer Pattern Methods ---
    def add_observer(self, observer):
        self.observers.append(observer)
        observer.update(self)  # Send initial state 

    def get_direction(self) -> Direction:
        return self.state.get_direction()
    
    # --- Request Handling ---
    def add_request(self, request: Request):
        print(f"Elevator {self.id} processing: {request}")
        self.state.add_request(self, request)
    
       # --- Getters and Setters ---
    def get_id(self) -> int:
        return self.id

    def get_up_requests(self) -> Set[int]:
        return self.up_requests

    def get_down_requests(self) -> Set[int]:
        return self.down_requests

    def is_elevator_running(self) -> bool:
        return self.is_running

    
    def run(self):

        while self.is_running:
            self.move()
            try: 
                time.sleep(1) 
            except KeyboardInterrupt:
                self.is_running = False
                break