import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add(someone):
    global queue
    print(f"You have {str(len(queue.get_queue()))} clients before you")
    queue.enqueue(someone)
    print("You have add someone to the queue")

def dequeue():
    pass

def save():
    pass

def load():
    pass 
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 3:
        print_queue()
    elif option == 1:
        print("Add someone") 
        someone =input()
        add(someone)
    elif option == 2:
        print("Remove someone") 
        someone =input()
        dequeue()
        print("")
    elif option == 3:
        count = 1
        for person in queue.get_queue():
            print(str(count)+'. '+str(person))
            count = count + 1
    elif option == 4:
        print("")
    elif option == 5:
        print("")
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
