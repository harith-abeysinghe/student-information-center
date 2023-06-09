'''
Answer for Question 4 - The Training

Name: 
SID:
unikey: 

'''
import getpass
import sys

def escape_key():
    while True:
        char = getpass.getpass(prompt='', stream=sys.stderr)
        if char == '\x1b':
            char = getpass.getpass(prompt='', stream=sys.stderr)
            if char == '\r':
                sys.exit()
        break

def intro():
    print("Larry: I'm Larry. I'll be your hunting instructor.")

def travel_to_camp():
    print("Larry: Let's go to the Meadow to begin your training!")
    input("Press Enter to travel to the Meadow...")
    print("""Travelling to the Meadow...
Larry: This is your camp. Here you'll set up your mouse trap.""")
    

def setup_trap() -> tuple:
    print("Larry: Let's get your first trap...")
    input("Press Enter to view traps that Larry is holding...")
    trap = str(input('''Larry is holding...
Left: High Strain Steel Trap
Right: Hot Tub Trap
Select a trap by typing "left" or "right": ''')).strip()
    if trap.lower() == "left" or trap.lower() == "right":
        if trap.lower() == "left":
            trap = "High Strain Steel Trap"
        else:
            trap = "Hot Tub Trap"
        cheese = 1
        print(f'''Larry: Excellent choice.
Your "{trap}" is now set!
Larry: You need cheese to attract a mouse.
Larry places one cheddar on the trap!''')
    else:
        trap = "Cardboard and Hook Trap"
        cheese = 0
        print("""Invalid command! No trap selected.
Larry: Odds are slim with no trap!""")
    
    return cheese


def sound_horn() -> str:
    print("Sound the horn to call for the mouse...")
    horn_input = input('Sound the horn by typing "yes": ')

    return horn_input


def basic_hunt(cheese: int, horn_input: str) -> bool:  
    if cheese == 0 and horn_input.lower() != "yes":
        print("Nothing happens.")
        hunt_status = False
    if cheese == 1 and horn_input.lower() == "yes":
        print("""Caught a Brown mouse!
Congratulations. Ye have completed the training.""")
        hunt_status = True
    if cheese == 0 and horn_input.lower() == "yes":
        print("""Nothing happens.
To catch a mouse, you need both trap and cheese!""")
        hunt_status = False
    if cheese == 1 and horn_input.lower() != "yes":
        print("""Nothing happens.
To catch a mouse, you need both trap and cheese!""")
        hunt_status = False

    return hunt_status
    
    
def end(hunt_status: bool):
    if hunt_status == True:
        print("Good luck~")
    

def main():
    intro()
    travel_to_camp()
    end(basic_hunt(setup_trap(), sound_horn()))
    
     
    
    '''
    Call your functions here.
    Apart from good design, this is so if you import this file in train.py 
    (question 5), it will not run this code. Because this code's __name__ 
    will not be '__main__', but it will instead be 'q4', allowing you to
    import this file to use your functions without running unwanted calling code.
    ''' 


'''
This statement is true if you run this script.
This statement is false if this file is to be imported from another script. 
'''
if __name__ == '__main__':
    main()
