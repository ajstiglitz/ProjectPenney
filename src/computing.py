import numpy as np
import pandas as pd
import os
from src.processing import ALL_PATTERNS

CSV_PATH = os.path.join('data', 'scores.csv')

def get_df(csv_file:str = CSV_PATH) -> pd.DataFrame:
    """
    csv_file: str: it is the file which will be processed 
    to get into a format that can be used by calc_probability

    The purpose of this function is to 
    """
    df = pd.read_csv(CSV_PATH)
    # Gets rid of the '(', ')' and ' ' within the indexes of the pattern to get it ready to be split
    df['Unnamed: 0'] = df['Unnamed: 0'].str.replace('(','')
    df['Unnamed: 0'] = df['Unnamed: 0'].str.replace(')','')
    df['Unnamed: 0'] = df['Unnamed: 0'].str.replace(' ','')
    # creating two columns for p1pattern and p2pattern
    df[['p1pattern','p2pattern']] = df['Unnamed: 0'].str.split(',', expand=True)
    df = df.drop('Unnamed: 0', axis=1)
    
    return df

# Calculates probabilities and turns them into an 8x8 array
def calc_probability(n_decks:int):
    """
    n_decks: the number of decks that was created. The same number should 
    be entered that was used in the datagen.

    The purpose of this function is to calculate the probability of winning.
    It returns the probability in order for it to be used later in visualizations.
    """
    # Calls the get_df() function in order to get the cleaned data with the correct columns
    df = get_df()
    
    if 'p1pattern' not in df.columns or 'p2pattern' not in df.columns:
        df.reset_index(inplace=True)
    
    # Creates 8x8 zero array to be filled in 
    cards_prob_array = np.zeros((8,8))
    tricks_prob_array = np.zeros((8,8))
    draw_cards_prob_array = np.zeros((8,8))
    draw_tricks_prob_array = np.zeros((8,8))

    # Loops through all possible pattern combinations
    for i, p1 in enumerate(ALL_PATTERNS):
        for j, p2 in enumerate(ALL_PATTERNS):
            if p1 == p2:
                continue # This is to account for when p1 and p2 are equal

            # Code for filtering rows
            df_subset = df[(df['p1pattern'] == p1) & (df['p2pattern'] == p2)]
            # A check to prevent errors
            if len(df_subset) == 0:
                cards_prob_array[i, j] = 0
                tricks_prob_array[i, j] = 0
                draw_cards_prob_array[i, j] = 0
                draw_tricks_prob_array[i, j] = 0

                #debugging
                #if these show that means it flags and the .csv is not being read
                #print(f"card prob array: {cards_prob_array}")
                #print(f"tricks prob array: {tricks_prob_array}")
                #print(f"draw cards prob array: {draw_cards_prob_array}")
                #print(f"draw tricks prob array: {draw_tricks_prob_array}")
            
            else:
                # Count Player 2 wins based on cards or tricks
                p2_card_wins = df_subset["p2wincards"].sum()
                p2_tricks_wins = df_subset["p2wintricks"].sum()
                draw_cards = df_subset["draw_cards"].sum()
                draw_tricks =  df_subset["draw_tricks"].sum()
                                    
                # Computes probability and rounds it to fit within the heatmap boxes for later
                cards_prob_array[i, j] = round((p2_card_wins / n_decks)*100,2)
                tricks_prob_array[i, j] = round((p2_tricks_wins / n_decks)*100,2)
                draw_cards_prob_array[i, j] = round((draw_cards / n_decks)*100)
                draw_tricks_prob_array[i, j] = round((draw_tricks / n_decks)*100)

    #debugging
    #print(f"n_decks: {n_decks}")

    #debug
    #print(f"card probability\n {cards_prob_array}")
    #print(f"tricks probability\n{tricks_prob_array}")
    #print(f"draw card probability\n{draw_cards_prob_array}")
    #print(f"draw tricks probability\n{draw_tricks_prob_array}")
    
    return cards_prob_array, tricks_prob_array, draw_cards_prob_array, draw_tricks_prob_array