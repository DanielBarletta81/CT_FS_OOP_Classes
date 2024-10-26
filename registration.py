#Task 1: Vehicle Registration System

#- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.

# Code Example: Provide a basic structure for the Vehicle class without methods.

""" class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner """
# Expected Outcome: Completion of the Vehicle class with the update_ownermethod 
# and a demonstration script showing the creation of Vehicle objects and updating their owners.

class Vehicle:
       def __init__(self, reg_num, type, owner):
           self.reg_num = reg_num
           self.type = type
           self.owner = owner

       def update_owner(self, new_owner):
            self.owner = new_owner
            print(new_owner)

       def display_vehicles(self):
            print(f'Registration # : {self.reg_num}, Type: {self.type}, Owner: {self.owner}')
            
reg_vehicles_list = {}       

def register_vehicle(reg_num, type, owner):
     if reg_num in reg_vehicles_list:
          print(f'Error. Registration {reg_num} already exists.')
          return
     reg_vehicles_list[reg_num] = Vehicle(reg_num, type, owner)
     print(f'Vehicle {reg_num} successfully registered!')

def change_owner(reg_num, new_owner):
     if reg_num in reg_vehicles_list:
          reg_vehicles_list[reg_num].update_owner(new_owner)
          print(f'Owner of {reg_num} has been updated.')
     else:
          print('Vehicle not found in system.')

def show_all_vehicles():
     for vehicle in reg_vehicles_list.values():
          vehicle.display_vehicles()

while True:
         
         action = input("Which action would you like to perform?(register, update, display, exit) ").lower()

         if action == 'exit':
          break
         try:
    
            if action == "register":
                reg_num = input("What is the registration # ? ")
                type = input("What type of vehicle is being registered? ")
                owner = input("Enter the owners full name. ")
                register_vehicle(reg_num, type, owner)
           
            elif action == "update":
                reg_num = input("What is the registration # ? ")
                new_owner = input("Enter the new owner's name: ")
                change_owner(reg_num, new_owner)
           
            elif action == "display":
                show_all_vehicles()
           
         except Exception as e:
            print(f'{e}')

print("You have closed the DMV Registration System.")
