from src.datagen import PATH_DATA
from src.datagen import get_decks
from glob import glob
import os

PATH_TO_LOAD = os.path.join('data','to_load')
PATH_LOADED = os.path.join('data','loaded')
FILE_PATTERN = 'seed*.npy'

# from binary to decimal
def bin2dec(b: str):
    return int(b,2)


# from decimal to binary
def dec2bin(n:int):
    return f'{n:b}'


#computing all the scores and all the modules are people with specific jobs

#check if user inputted 1s and 0s (just for purpose of checking the player input)
# URL
# https://stackoverflow.com/questions/37578628/python-checking-if-string-consists-only-of-1s-and-0s
def binary_check(pattern:str):
    for character in pattern:
        if character != '0' and character != '1':
            print("not 0 or 1")
            break
    return

# this function should be for patterns like RRR and RBR etc
def player_patterns():
    """
    get the two patterns to be used for scoring the decks
    """

    #set false
    flag = False

    while not flag:
        pattern1 = input("Player 1's Pattern")
        # check if only 3 characters
        # if you want to make the pattern length possible for 4 cards, 3 changes to n
        if len(pattern1) > 3:
            print("Error: p1 pattern exceeds length")
            break
        # check if pattern is only made up of 1s or 0s
        binary_check(pattern1)

        
        pattern2 = input("Player 2's Pattern")
        #checking
        if len(pattern2) > 3:
            print("Error: p2 pattern exceeds length")
            break
        # check if pattern is only made up of 1s or 0s
        binary_check(pattern2)
        flag = True

    return pattern1, pattern2

# from office hours notebook
def find_seq(deck, pattern, start=0):
    try:
        idx = deck.index(pattern, start)
    except:
        return -1
    return idx


# use 'wa' or 'a' for append if you want to add to json file
#you use timestamp though so its fine (i think)

#scoring by tricks and total cards
# using loops to score
def scoring_decks(n_decks: int,
                  seed:int,
                  path_data: PATH_DATA
                  ):

                 
    #open the json file that has the deck you want to score
    json_path = os.path.join(path_data,)
    
    decks = get_decks(n_decks,seed)




    deck_str = ''.join(map(str, decks[0]))

    # the patterns that the players inputted
    p1,p2 = player_patterns()

    idx1 = find_seq(deck_str, p1)
    idx2 = find_seq(deck_str, p2)
    
    # initializing total cards and tricks for players 1 and 2
    p1cards = 0
    p1tricks = 0
    p2cards = 0
    p2tricks = 0

    # position in the deck
    pos = 0


    idx1 = find_seq(deck_str, p1)
    idx2 = find_seq(deck_str, p2)

    while (idx1 != -1) and (idx2 != -1):
        if idx1 < idx2:
            # Player 1 found first
            p1cards += idx1+3-pos
            p1tricks += 1
            pos = idx1+3
        elif idx2 < idx1:
            p2cards += idx2+3-pos
            p2tricks += 1
            pos = idx2+3
        
        idx1 = find_seq(deck_str, p1, pos)
        idx2 = find_seq(deck_str, p2, pos)


    return p1cards, p1tricks, p2cards, p2tricks

def load_data(self)-> None:
    files = glob(os.path.join(PATH_TO_LOAD, FILE_PATTERN))

    for file in files:
        print(f'Loading {file}')
        try:
            # code to load the npy file
            #if successful move to loaded folder
            self.something()

            os.rename(file, file.replace(PATH_TO_LOAD, PATH_LOADED))
        except Exception as e:
            raise type(e)(f'Problem loading file: {file}')

    return

def save_deck_score(path_data: PATH_DATA,
                    path_,
                    p1Pattern:str,
                    p2Pattern:str

                    
                    ):
    """
    Saving the scores from the scoring_decks function
    """

    npy_files = glob(os.path.join(PATH_TO_LOAD, FILE_PATTERN)) 
    npy_path = os.path.join(path_data, npy_file)

    with open(npy_path, 'a') as f:


    #split the data folder into processed and unprocessed. So when adding the pattern and scoring it moves when done.

    # save the pattern of p1 and p2 and the cards and tricks for each on the json file





        return