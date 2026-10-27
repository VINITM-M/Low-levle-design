# Rule of thumb : 

# Inheritance  : Manager ----▷ Employee       (is-a)

# Association  : Report ------> Employee      (uses/knows)

# Aggregation  : Department ◇--> Employee     (weak has-a)

# Composition  : Car ◆-----> Engine           (strong has-a)

# Dependency   : Report - - -> Employee       (temporary use)

# Relization -- Combines Dependency + Inheritance 

# ------------------------------Association------------------------------------#

# Association  -- object of one classes send to other classes as reference  ,refernces classes can able to access 
# attributes, methods from orginated classes 
# association refernce class always awaits object from orginated class 
# refence class ---->  base class 

# from Employee import Employee
# class Report:
#     def __init__(self, employee: Employee):
#         self.employee = employee

#     def print_name(self):
#         print(self.employee.name)

# obj1 = Employee("vinith")
# obj2 = Report(obj1)

# obj2.print_name() 


#----------------------------------------Aggregation--------------------------# 

# child can exisit without patent object, it acts as independtly. 
# Aggregation is a HAS-A relationship where one object contains or uses another object, but the contained object can exist independently.
# Forest ◇---- Tree

# from Employee import Forest

# class Tree: 
#     def __init__(self):
#         self.bucket = [] 

#     def add(self, tree):
#         self.bucket.append(tree.name)
#         print(self.bucket, end = '') 

# obj1 = Forest("Banana")
# obj2 = Tree() 
# obj2.add(obj1) 

#----------------------------------------Composition or Restricted Aggregation--------------------------#
 
# Composition is a strong HAS-A relationship.
# The child object cannot be exist without the parent object.

# from Employee import Engine
# class Car:
#     def __init__(self):
#         self.engine = Engine()

# obj1 = Car() 

#----------------------------------------Dependency--------------------------#

# Dependency means one class uses another class temporarily.
# The object is not stored as an instance variable.

# from Employee import Employee 
# class Report:
#     def print_report(self, employee:Employee):
#         print(employee.name) 

# Why Dependency ?
#       Report uses Employee classes only inside a method 

# emp = Employee('vinith') 
# rep = Report()

# rep.print_report(emp) 
