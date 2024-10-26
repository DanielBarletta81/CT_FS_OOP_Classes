#Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

# Code Example: Basic Event class without participant tracking.

"""     class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date """



class Event:
       attendance = 0

       def __init__(self, name, date, attendance):
         self.name = name
         self.date = date
         self.attendance = attendance

       def update_attendance(self, attendance):
            self.attendance += 1
            print(attendance)

       

       def display_guests(self):
            print(f'\n Name : {self.name} \n Date: {self.date} \n Guests Attended: {self.attendance} \n _________________')   
    
      

attended_event = {}
       
def add_participant(name, date, attendance):
             if name in attended_event:
                 print(f'Error. Registration {name} already exists.')
                 return
             attended_event[name] = Event(name, date, attendance)
             
             print(f'Attendee: {name} successfully added to Event list!!')
            

     
def display_info(attendance):
    attendance = len(attended_event)
    print(f' Total Guests: {attendance}') 
    for guest in attended_event.values():
          guest.display_guests()
       
           
            


while True:
     
       print("***  Event Participant Tracker ***")
       print("\n Menu:")
       print("\n 1. Add Participant")
       print("\n 2. View Participants and Total")
       print("\n 3. Exit")

       action = int(input("Please choose an option (1-3): "))
       if action == 3:
           break
       try:
            attendance = 0
            if action == 1:
                name = input("Please enter Name: ")
                date = input("What is the date of the event? (MM/DD/YYYY)")
                attended = input("Did this person attend? (yes/no) ")
                
                if attended == 'yes':
                    attendance = attendance + 1
                    add_participant(name, date, attendance)
   #             add_another = input("Would you like to add another guest? (yes/no)") 
    #            if add_another == 'yes':
                           

            elif action == 2:
                display_info(attendance)
                

       except ValueError as e:
        print(f'An exception occurred: {e}')