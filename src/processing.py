from src.datagen import PATH_DATA
import numpy as np
from glob import glob
import pandas as pd
import os

PATH_TO_LOAD = os.path.join('data','to_load')
PATH_LOADED = os.path.join('data','loaded')
SCORES_FILE = os.path.join('data','scores.csv')
FILE_PATTERN = 'seed*.npy'

# all 8 of the possible patterns a player can choose
ALL_PATTERNS = ['111', '101', '011', '001', '110', '100', '010', '000']

# Sole purpose of this module is to comute scores for any files that have not yet been scored


def find_seq(deck,
             pattern,
             start=0):
    """
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
    """

    deck_str = ''.join(map(str, deck))

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

    return p1, p2, p1cards, p1tricks, p2cards, p2tricks


def score_decks(decks_file:str):
    """
    decks_file: A file containing many decks

    The Function loops over all possible combinations of player choices as well as 
    all the decks in the decks_file and computes the scores
    """

    decks = np.load(decks_file)

    scores = []
    
    for deck in decks:
        for p1 in ALL_PATTERNS:
            for p2 in ALL_PATTERNS:
                if p1 != p2:
                    p1, p2, p1cards, p1tricks, p2cards, p2tricks = score_game(deck, p1, p2)
                    scores.append([p1, p2, p1cards, p1tricks, p2cards, p2tricks])

    df_scores = pd.DataFrame(scores, columns=["p1pattern","p2pattern","p1cards","p1tricks","p2cards","p2tricks"])
    return df_scores


def update_score():
    """
    Saving the scores from the scoring_decks function
    """

    files = glob(os.path.join(PATH_TO_LOAD, FILE_PATTERN))

    #if there are no files in the to_load folder, returns "loaded" message for user
    if not files:
        print("loaded")
        return
    
    if os.path.exists(SCORES_FILE):
        df_scores = pd.read_csv(SCORES_FILE)

    else:
        df_scores = pd.DataFrame(columns=["p1_pattern", "p2_pattern", "p1cards", "p1tricks", "p2cards", "p2tricks"])

    for file in files:
        # tells you which file is being loaded
        print(f'Loading {file}')
        try:
            new_scores = score_decks(file)

            df_scores = pd.concat([df_scores, new_scores], ignore_index=True)
            df_scores.to_csv(SCORES_FILE, index=False)

            # after loading, moves the location to the loaded folder and tells the user
            os.rename(file, file.replace(PATH_TO_LOAD, PATH_LOADED))
            print(f'File: {file} moved to: {PATH_LOADED}')
        except Exception as e:
            raise type(e)(f'Problem loading file: {file}')

    return