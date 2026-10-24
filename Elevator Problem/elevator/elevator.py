
class Elevator:
    def __init__(self, elevator_id: int):

        self.id = elevator_id 
        self.current_floor = 1
        self.current_floor_lock = threading.Lock()
        self.state = IdleState()
        self.is_running = True 

        self.up_requests = set()
        self.down_requests = set()

        self.observers = []
    
    def add_observer(self, observer: ElevatorObserver):
        self.observers.append(observer)
        observer.update(self)  # Send initial state