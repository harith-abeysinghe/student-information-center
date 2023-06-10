'''
Write your solution for Question 1 and Question 2 here.
You may add additional functions but the existing functions given in the scaffold must exists.

Name:
SID:
unikey:

'''
import os.path
import sys

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
    try:
        if not os.path.exists("home/saved/"+fobj+".txt"):
            return ""
        with open("home/saved/"+fobj+".txt","r") as f:
            t = f.read().split("\n")
            if "Start game" in t and "End game" in t:
                start = t.index("Start game")  
                end = t.index("End game")
                gold = 0
                chedaar = 0
                total_sound = 0
                total_misses = 0
                total_forgot = 0
                total_brown = 0
                market = 0
                hunt = 0
                for i in range(start, end):
                    text = t[i]
                    if text == "Start shop":
                        market = 1
                    if text == "End shop":
                        market = 0
                    if text == "Start hunt":
                        hunt = 1
                    if text == "Stop hunt":
                        hunt = 0
                    if market and "Bought" in text:
                        temp = text.split()
                        chedaar += int(temp[1])
                        gold += int(temp[1]) * 10
                    if hunt and text == "Nothing happens.":
                        total_misses += 1
                    if hunt and text == "Nothing happens. You are out of cheese!":
                        total_forgot += 1
                    if hunt and text == "Caught a Brown mouse!":
                        total_brown += 1
                total_sound = total_brown + total_misses + total_forgot
                goldearn = total_brown * 125
                    

                return f"""You have spent {gold} gold in The Cheese Shop.
Total cheddar bought: {chedaar}
You have sounded the horn {total_sound} times during The Hunt.
Total Brown mouse caught: {total_brown}
Total empty catches: {total_misses}
Total hunt without cheese: {total_forgot}
You have earned {goldearn} gold from The Hunt."""

            else:
                return ""
    except Exception:
        return ""


def main(args):
    '''
    Checks if game analysis feature works correctly
    Parameters:
        args: list of command line arguments
    Returns:
        result: str, formatted string displaying the game analysis results
    '''
    if len(args) != 1:
        print("Format: python3 fe.py <name>")
        return 
    
    print(analyze_game(args[0]))

if __name__ == "__main__":
    main(sys.argv[1:])
