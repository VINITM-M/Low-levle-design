
from abc import ABC, abstractmethod

class ElevatorSelectionStrategy(ABC): 

    @abstractmethod
    def select_elevator(self, elevators: List, request: Request) -> Optional:
        pass

class NearestElevatorStrategy(ElevatorSelectionStrategy):

    def select_elevator(self, elevators: List, request: Request) -> Optional:
        return best_elevator