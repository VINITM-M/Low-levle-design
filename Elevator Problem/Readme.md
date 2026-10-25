# Requirements

# perform user actions either goes in up direction or down direction 
# systems pick the nearest elevator to reach the up or down 
# display updates the automatically along with elevators moving. 
# reaches the target , wait for time 2s or 5s, perform open actions and close actions
# user enter floor number should be > current floor, if it's lesser perform complete action which is last extreme high floor
# make sure that system not inter-conflict each other 
# weight calculation 
# waiting time 
# concurency 

https://github.com/Yeagerist0/elevatorlld/blob/main/src/Main.java
https://github.com/atul-X/lld-problem/tree/master/src/elevatordesign
ElevatorSystem: Manages the fleet and delegates dispatching decisions to an assignment strategy.
Elevator: Represents an autonomous physical car executing as a Runnable worker.
RequestProcessingStrategy: Encapsulates floor selection logic (e.g., SCAN, LOOK, FCFS) per elevator.

==================================
      ELEVATOR SYSTEM
==================================

Elevator-1 : Floor 1 [IDLE]
Elevator-2 : Floor 5 [IDLE]
Elevator-3 : Floor 9 [IDLE]

User at Floor 7 pressed UP

Dispatcher:
Assigned Elevator-2

Display:
Elevator-2 moving DOWN
Current Floor: 5
Current Floor: 6
Current Floor: 7

Door Opening...
Passenger Entered

Enter destination floor: 15

Door Closing...

Elevator-2 moving UP
Current Floor: 8
Current Floor: 9
Current Floor: 10
Current Floor: 11
Current Floor: 12
Current Floor: 13
Current Floor: 14
Current Floor: 15

Door Opening...
Reached Floor 15

Door Closing...

Elevator-2 State -> IDLE



#perform directions either up or down 

user_direction = input("Enter direction 2, 1: ")

#choose the elevator nearby user and assign to him respective direction 

#update display automatically 

#perform door actions 

#enter the floor number inside the elevator , condition:  > cur or < cur as it's follow, same = no 
actions 

#weight or limit cases 

# priority specific floor 

# priority specific floor for more waiting time 

#minimize waiting time 

#multiple requests concurrently  

# prevent race condition


