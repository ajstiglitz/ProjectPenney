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
    prob_array = np.zeros((8,8))

    # Loops through all possible pattern combinations
    for i, p1 in enumerate(ALL_PATTERNS):
        for j, p2 in enumerate(ALL_PATTERNS):
            if p1 == p2:
                continue # This is to account for when p1 and p2 are equal

            # Code for filtering rows
            df_subset = df[(df['p1pattern'] == p1) & (df['p2pattern'] == p2)]

            # Code to set to NaN when the patterns are the same.
            if len(df_subset) == 0:
                prob_array[i, j] = np.nan
            else:
                # Count Player 1 wins based on cards or tricks
                p1_wins = ((df_subset['p1cards'] > df_subset['p2cards']) | 
                           (df_subset['p1tricks'] > df_subset['p2tricks'])).sum()                
                
                # Computes probability
                prob_array[i, j] = p1_wins / len(df_subset)

    return prob_array