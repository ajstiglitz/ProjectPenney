import numpy as np
import pandas as pd
import os
from src.processing import ALL_PATTERNS

CSV_PATH = os.path.join('data', 'scores.csv')

# and turn them into an 8x8 array of probabilities
def calc_probability(csv_file:str = CSV_PATH):
    """
    csv_file: it is the file which will be used to calculate probabilities.

    The purpose of this function is to calculate the probability of winning.
    Returns that probability in order for it to be used later in visualizations.
    """

    df = pd.read_csv(CSV_PATH,dtype={'p1pattern': str, 'p2pattern': str})
    df = df.drop(columns = ['p1_pattern','p2_pattern'])

    # creates 8x8 zero array to be filled in 
    prob_array = np.zeros((8,8))

    # Loop through all possible pattern combos
    for i, p1 in enumerate(ALL_PATTERNS):
        for j, p2 in enumerate(ALL_PATTERNS):
            if p1 == p2:
                continue # dont need to bother if p1 and p2 equal (because that's not possible for the game)

            # Filtering rows
            df_subset = df[(df['p1pattern'] == p1) & (df['p2pattern'] == p2)]

            # Count Player 1 wins based on cards or tricks
            p1_wins = ((df_subset['p1cards'] > df_subset['p2cards']) | 
                       (df_subset['p1tricks'] > df_subset['p2tricks'])).sum()

            # Compute probability
            prob_array[i, j] = p1_wins / len(df_subset)

    return prob_array


