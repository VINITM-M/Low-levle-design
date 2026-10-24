
class elevator : 

    def __init__(self, num_elevators):
        self.num_elevators = num_elevators 
    
    @classmethod
    def get_instance(cls, num_elevators: int):
        return cls(num_elevators)