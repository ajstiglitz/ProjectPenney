from src.datagen import PATH_DATA
import numpy as np
from glob import glob
import pandas as pd
import os

PATH_TO_LOAD = os.path.join('data','to_load')
PATH_LOADED = os.path.join('data','loaded')
SCORES_FILE = os.path.join('data','scores.csv')
FILE_PATTERN = 'seed*.npy'

# All 8 of the possible patterns a player can choose
ALL_PATTERNS = ['000', '001', '010', '011', '100', '101', '110', '111']

def find_seq(deck,
             pattern: str,
             start=0):
    """
    deck: the representation of the 52 card deck
    pattern: a string representing the sequence that the player chose
    start: the intial position

    Looks for the first occurence of a player pattern and gets the index    
    """

    try:
        idx = deck.index(pattern, start)
    except:
        return -1
    return idx

def score_game(deck, 
               p1:str, 
               p2:str):
    """
    deck: a representation of a 52-card deck
    p1: the three card pattern picked by player 1
    p2: the three card pattern picked by player 2

    This function should score the game based on these patterns 
    and accounts for draws in cards and/or tricks
    """

    deck_str = ''.join(map(str, deck))

    idx1 = find_seq(deck_str, p1)
    idx2 = find_seq(deck_str, p2)
    
    # initializing the total cards and tricks for players 1 and 2
    p1cards = 0
    p1tricks = 0
    p2cards = 0
    p2tricks = 0

    #initializing the draws for cards and tricks
    draw_cards = 0
    draw_tricks = 0

    # initializing which player won based on their cards
    p1wincards = 0
    p2wincards = 0
    
    # initializing which player won based on their tricks
    p1wintricks = 0
    p2wintricks = 0
    
    # the position in the deck
    pos = 0
       
    while (idx1 != -1) and (idx2 != -1):
        if idx1 < idx2:
            # Player 1 found first, so their cards and tricks score updates
            p1cards += idx1+3-pos
            p1tricks += 1
            pos = idx1+3
        elif idx2 < idx1:
            # Player 2 found first, so their cards and tricks score updates
            p2cards += idx2+3-pos
            p2tricks += 1
            pos = idx2+3

        # finding the first occurrence of p1 pattern
        idx1 = find_seq(deck_str, p1, pos)
        #finding the first occurence of p2 pattern
        idx2 = find_seq(deck_str, p2, pos)
        
    # tracking draws for cards and tricks
    if p1cards == p2cards:
        draw_cards += 1
    if p1tricks == p2tricks:
        draw_tricks += 1

    # tracking the actual card wins of the players
    if p1cards > p2cards:
        p1wincards += 1
    elif p2cards > p1cards:
        p2wincards += 1

    # tracking the actual trick wins of the players
    if p1tricks > p2tricks:
        p1wintricks += 1
    elif p2tricks > p1tricks:
        p2wintricks += 1


    return p1, p2, draw_cards, draw_tricks, p1wincards, p2wincards, p1wintricks, p2wintricks

# this is the problem. Shouldnt append scores, only update to keep it as the 56 probabilities
def score_decks(decks_file:str):
    """
    decks_file: A file containing many decks

    The Function loops over all possible combinations of player choices as well as 
    all the decks in the decks_file and computes the scores.
    """

    #loads in the decks_file
    decks = np.load(decks_file)

    scores_dict = {f"({p1}, {p2})": [0,0,0,0,0,0] for p1 in ALL_PATTERNS for p2 in ALL_PATTERNS if p1 != p2}
  
    # goes through all of the possible patterns and scores the probabilities for them    
    for deck in decks:
        for p1 in ALL_PATTERNS:
            for p2 in ALL_PATTERNS:
                if p1 != p2:
                    _, _, draw_cards, draw_tricks, p1wincards, p2wincards, p1wintricks, p2wintricks = score_game(deck, p1, p2)

                    # string index, as prof said
                    idx = f"({p1}, {p2})"
                    
                    #saves the scores to their corresponding places
                    #keeps the .csv file a reasonable size to push to Git
                    scores_dict[idx][0] += draw_cards
                    scores_dict[idx][1] += draw_tricks
                    scores_dict[idx][2] += p1wincards
                    scores_dict[idx][3] += p2wincards
                    scores_dict[idx][4] += p1wintricks
                    scores_dict[idx][5] += p2wintricks

    
    # puts the scores into a pandas dataframe
    df_scores = pd.DataFrame.from_dict(scores_dict, orient = 'index',
                             columns=["draw_cards", "draw_tricks","p1wincards","p2wincards", "p1wintricks", "p2wintricks"])
    df_scores.index.name = "p1p2pattern"
    df_scores.reset_index(inplace=True)

    #Debugging
    #print(df_scores.head())
    return df_scores


def update_score():
    """
    Saving the scores from the scoring_decks function. Looks at the to_load folder to determine
    what needs to have its score updated, and once finished, moves the scored file
    """

    files = glob(os.path.join(PATH_TO_LOAD, FILE_PATTERN))

    #if there are no files in the to_load folder, returns "loaded" message for user
    if not files:
        print("loaded")
        return
    
    if os.path.exists(SCORES_FILE):
        df_scores = pd.read_csv(SCORES_FILE, index_col=0)

    else:
        idx_lab = [f"({p1}, {p2})" for p1 in ALL_PATTERNS for p2 in ALL_PATTERNS if p1 != p2]
        #df scores has the patterns as the indexes
        df_scores = pd.DataFrame(0, index=idx_lab, 
                                 columns=["draw_cards", "draw_tricks","p1wincards","p2wincards", "p1wintricks", "p2wintricks"])

    for file in files:
        # tells you which file is being loaded
        print(f'Loading {file}')
        try:
            new_scores = score_decks(file)

            new_scores.index = df_scores.index 
            
            for idx in new_scores["p1p2pattern"]:

                #try splitting this up
                try:
                    df_scores.loc[idx, ["draw_cards", "draw_tricks","p1wincards","p2wincards", "p1wintricks", "p2wintricks"]] += new_scores.loc[idx, ["draw_cards", "draw_tricks","p1wincards","p2wincards", "p1wintricks", "p2wintricks"]].values

                except KeyError:
                    print(f"KeyError for idx: {idx}")
                    continue  # Skip if pattern doesn't match            

            df_scores.to_csv(SCORES_FILE)

            # after loading, moves the location to the loaded folder and tells the user
            os.rename(file, file.replace(PATH_TO_LOAD, PATH_LOADED))
            print(f'File: {file} moved to: {PATH_LOADED}')
        except Exception as e:
            raise type(e)(f'Problem loading file: {file}: {str(e)}')

    #debugging
    #print("DF Scores:")
    #print(df_scores.index.to_list())
    #print("New Scores:")
    #print(new_scores["p1p2pattern"].tolist())
    
    return