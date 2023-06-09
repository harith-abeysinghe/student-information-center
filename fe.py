'''
Write your solution for Question 1 and Question 2 here.
You may add additional functions but the existing functions given in the scaffold must exists.

Name:
SID:
unikey:

'''
import os.path

def refresh_file(filename):
    '''
    Creates an empty file if filename exists.
    Parameters:
        filename: str, abs path to file. 
    '''
    if os.path.exists(filename):
        open(filename, 'w')
    else:
        print("File path does not exist.")

def log_events(event, filename='home/saved/temp.txt'): #TODO: change path to /home/saved/temp.txt when run in linux to save it in home directary
    '''
    Write the received event into filename.
    If filename argument is missing, default file: /home/saved/temp.txt
    Parameters:
        event: str, event to be written to file
        filename: str, abs path to file.
    Returns:
        success: bool, True if written successfully. Else False.
    '''
    try:
        if not os.path.exists(filename):
            f = open(filename, 'w')
            f.close()

        with open(filename, 'a') as f:
            f.write(event + "\n")

        return True
    except Exception as e:
        print(e)
        return False


def analyze_game(fobj):
    '''
    Analyzes the contents of an open file object to extract game information.
    The parameter is NOT a str object! 
    Parameters:
        fobj: open file object in read mode
    Returns:
        output: str, formatted string displaying the game analysis results.
    '''
    pass

def main(args):
    '''
    Checks if game analysis feature works correctly
    Parameters:
        args: list of command line arguments
    Returns:
        result: str, formatted string displaying the game analysis results
    '''
    print(log_events("test55"))

if __name__ == "__main__":
    main(5)
