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


# https://www.geeksforgeeks.org/system-design/elevator-system-low-level-design-lld/
# https://github.com/ashishps1/awesome-low-level-design/tree/main/solutions/python/elevatorsystem
# https://algomaster.io/learn/lld/design-elevator-system
# https://akhileshmj.medium.com/lld-5-elevator-system-52dca7dde379


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