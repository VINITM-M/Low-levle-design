class Door:

    def __init__(self, action):
        self.action = action 
    
    def open(self):
        print(self.action)
        print("Opening") 
    
    def close(self):
        print("Closing")


user_input = input("Enter action Open/close: ")

if user_input.lower() ==  "open":
    obj1 = Door(user_input).open() 
    print(obj1)

elif user_input.lower() == "close":
    obj1 = Door(user_input).close()  