'''
Answer for Question 3 - Function

Name: 
SID: 
unikey: 

'''

def is_valid_length(name: str) -> bool:
    length_of_name = len(name)

    if name and len(name.strip(' ')) > 0 and length_of_name < 10:
        is_valid_length = True
    else:
        is_valid_length = False

    return is_valid_length


def is_valid_start(name: str) -> bool:
    length_of_name = len(name)
    if name and len(name.strip(' ')) > 0 and length_of_name > 0 and name[:1].isalpha():
        is_valid_start = True
    else:
        is_valid_start = False

    return is_valid_start


def is_one_word(name: str) -> bool:
     length_of_name = len(name)
     if name and length_of_name > 0 and name.find(" ") == -1:
        is_one_word = True
     else:
        is_one_word = False

     return is_one_word


def is_valid_name(name: str) -> bool:
    if is_valid_length(name) == True and is_valid_start(name) == True and is_one_word(name) == True:
        is_valid_name = True
    else:
        is_valid_name = False
    
    return is_valid_name
