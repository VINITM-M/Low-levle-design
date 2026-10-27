
#--------------------Association----------------------#  
# class Employee : 
#     def __init__(self, name):
#         self.name = name  


#----------------------------------------Aggregation--------------------------# 

# class Forest : 
#     def __init__(self, name):
#         self.name = name  

#----------------------------------------Composition or Restricted Aggregation--------------------------#

# class Engine:
#     def __init__(self):
#         print("Engine created")

#----------------------------------------Dependency--------------------------#

# class Employee:
#     def __init__(self, name):
#         self.name = name


#-------------------------------------------------------------------------------# 

# Enum (Enumeration) is used when you have a fixed set of constant values.
# Only predefined values are allowed.

#-----------------------------------------------Interface----------------------# 

""" 
Inheritance → child gets code from parent.
Interface → child gets rules from interface and writes its own code.

If you want to become my child, You must implement all the methods which I have. 

Simple words: 
    If an interface has 5 methods, whoever implements that interface should implement those 5 methods."

Example: 

Interface class : 

from abc import ABC, abstractmethod
class Payment(ABC):

   @abstractmethod
    def pay(self):
       pass

The interface says:

Anyone who wants to be a Payment
must have a pay() method.
It does NOT say how to pay.

Child Class 1:

class CreditCardPayment(Payment):

    def pay(self):
        print("Paid using Credit Card")  

What if parent interface method has some data or values defined inside it?

Example 2:

class Payment(ABC):

    @abstractmethod
    def pay(self):
    print("Common Logic")

Technically Python allows it.

class UPI(Payment):
    def pay(self):
        super().pay()
        print("UPI Logic")

Output:

    Common Logic
    UPI Logic

But now it is acting more like an abstract base class than a pure interface. """  

#------------------------------------------Abstraction----------------------------------------------# 


# In Python, there is no separate interface keyword like Java or C#.
# That hiding of implementation details while exposing only the required functionality is Abstraction.

# Example: Remote accessories it shows btn , but when we press the remote inside some functonalities happends 
# that's absrtaction 

# Exmaple with code: 

# from abc import ABC, abstractmethod
# from datetime import datetime

# class Logger(ABC):
    
#     def __init__(self, level: str):
      
#         self._level = level
#         print(self._level)


#     # Abstract method: subclasses decide HOW to deliver the message
#     @abstractmethod
#     def log(self, message: str) -> None:
#         pass

#     # Concrete method: shared formatting logic inherited by all subclasses
#     def format_message(self, message: str) -> str:
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         return f"[{timestamp}] [{self._level}] {message}"

# class ConsoleLogger(Logger):
    
#     def __init__(self, level: str):
#         super().__init__(level)
        
#     def log(self, message: str) -> None:
#         print(self.format_message(message))

# class FileLogger(Logger):
    
#     def __init__(self, level: str, file_path: str):
#         super().__init__(level)
       
#         self._file_path = file_path

#     def log(self, message: str) -> None:
#         # In production, this would write to a file
#         print(f"Writing to {self._file_path}: {self.format_message(message)}")
        
# obj2 = FileLogger("INFO", ".docx") 

# print(obj2.log("Appplication")) 
