import numpy as np
import pandas as pd
import os
from src.processing import ALL_PATTERNS

CSV_PATH = os.path.join('data', 'scores.csv')

# calculate probabilities and turn them into an 8x8 array
def calc_probability(csv_file:str = CSV_PATH):
    """
    csv_file: it is the file which will be used to calculate probabilities.

    The purpose of this function is to calculate the probability of winning.
    It returns the probability in order for it to be used later in visualizations.
    """

    df = pd.read_csv(CSV_PATH,
                     dtype={'p1pattern': str, 'p2pattern': str})

    # creates 8x8 zero array to be filled in 
    card_prob_array = np.zeros((8,8))
    trick_prob_array = np.zeros((8,8))
    draw_cards_prob_array = np.zeros((8,8))
    draw_tricks_prob_array = np.zeros((8,8))

    # Loops through all possible pattern combinations
    for i, p1 in enumerate(ALL_PATTERNS):
        for j, p2 in enumerate(ALL_PATTERNS):
            if p1 == p2:
                continue # This is to account for when p1 and p2 are equal

            # Code for filtering rows
            df_subset = df[(df['p1pattern'] == p1) & (df['p2pattern'] == p2)]

            
            # Count Player 1 wins based on cards or tricks
            p2_card_wins = (df_subset['p2cards'] > df_subset['p1cards']).sum()
            p2_tricks_wins = (df_subset['p2tricks'] > df_subset['p1tricks']).sum()
            draw_cards = df_subset['draw_cards'].sum()
            draw_tricks = df_subset['draw_tricks'].sum()
                
            # Computes probability
            card_prob_array[i, j] = round((p2_card_wins / len(df_subset)),2)*100
            trick_prob_array[i, j] = round((p2_tricks_wins/ len(df_subset)),2)*100
            draw_cards_prob_array[i, j] = round((draw_cards / len(df_subset)))*100
            draw_tricks_prob_array[i, j] = round((draw_tricks / len(df_subset)))*100

    return card_prob_array, trick_prob_array, draw_cards_prob_array, draw_tricks_prob_array