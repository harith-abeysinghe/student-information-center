'''
Answer for Question 5 - The Training Again

Name: 
SID: 
unikey:

'''

'''
We recommend you import your 'q4' module to complete this question. It will save 
trouble in needing to copy and paste code from previous question. However if you 
wish not to, you are free to remove the import below.
'''
from q4 import *


# you can make more functions here if you please
# or any global variables

def main():
    intro()
    travel_to_camp()
    while True:
        end(basic_hunt(setup_trap(), sound_horn()))
        train = input('''
Press Enter to continue training and "no" to stop training: ''')
        if train.lower() == "no":
            break



if __name__ == '__main__':
    main()
