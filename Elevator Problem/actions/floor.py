class Floor:
    def __init__(self, n):
        
        if not isinstance(n, int):
            raise ValueError("Floor number must be an integer")

        if n < 1 or n > 9:
            raise ValueError("Floor number must be between 1 and 9")

        self.n = n

n = int(input("Enter floor number: "))
obj_floor = Floor(n)

print(obj_floor.n)