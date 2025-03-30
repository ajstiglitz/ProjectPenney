import pandas as pd
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt
import os
import numpy as np


ALL_PATTERNS = ['RRR', 'RBR', 'BRR', 'BBR', 'RRB', 'RBB', 'BRB', 'BBB']

# code from professor's example
def make_annotation(arr1, arr2) -> np.ndarray:
    '''
    creates an Annotation for the heatmap.
    When in use, it should have the numbers from arr1 and arr2
    in the form of: number(number)
    '''

    # Verify both arrays have the same shape
    if arr1.shape != arr2.shape:
        raise ValueError(f'Arrays must be of the same shape, but have shapes {arr1.shape} and {arr2.shape}.')
    else:
       # Initialize annot with empty strings
        arr_shape = arr1.shape
        annot = np.empty(shape=arr_shape, dtype="<U9")

    for i in range(arr_shape[0]):
        for j in range(arr_shape[1]):
            # Ensure arr2 (draw values) are rounded to integers
            annot[i, j] = f'{arr1[i,j]}({int(arr2[i,j])})'  # Ensure draw value is an integer
    return annot


# creates a heatmap that that uses the stored decks and scores, 
# rather than doing any kind of simulation itself
def card_heatmap(card_prob_matrix: np.ndarray,
                 draw_cards_prob_array: np.ndarray,
                 n_decks:int,
                 gray_diagonal: bool = False
                ):
    """
    card_prob_matrix: takes the 8x8 probability matrix for p2 cards that was calculated 
    by calc_probability in computing.py
    draw_cards_prob_array: the 8x8 probability matrix that calculated the draws between p1 and p2's cards
    n_decks: the n_decks number that was used for generating the decks. Used in the heatmap title.
    gray_diagonal: a boolean that is used to either choose to (or not choose to) gray out the 
    diagonal on the heatmap
    
    Creates a heatmap for visualizing the probability results calculated by calc_probability
    """

    # sets up the path for Heatmaps to be loaded into figures folder 
    figure_dir = "figures"  
    os.makedirs(figure_dir, exist_ok=True)
 
    card_annot = make_annotation(card_prob_matrix, draw_cards_prob_array)

    # If gray_diagonal is enabled, mask diagonal values
    if gray_diagonal:
        card_prob_array = card_prob_matrix.astype(float)
        np.fill_diagonal(card_prob_matrix, np.nan)

    fig, ax = plt.subplots(figsize=(10, 8))
    
    # creates the heatmap
    sns.heatmap(card_prob_matrix,
                      cmap="crest", 
                      vmin=0, 
                      vmax=100, 
                      annot=card_annot,
                      fmt = '',
                      linewidths = 1,
                      cbar=False,
                      xticklabels=ALL_PATTERNS,
                      yticklabels=ALL_PATTERNS,
                      ax=ax
                      )
    ax.set_title(f"My Chance to Win(Draw) by Cards \n N = {n_decks}")

    plot_title = f"Heatmap for the cards {n_decks}"


    ax.set_xlabel('My Choice')
    ax.set_ylabel('Opponent Choice')
    
    # saves the heatmap into the figures folder
    figure_path = os.path.join(figure_dir,plot_title)
    fig.savefig(figure_path,bbox_inches = 'tight', facecolor = 'white')

    return


def tricks_heatmap(trick_prob_matrix: np.ndarray,
                   draw_tricks_prob_array: np.ndarray,
                   n_decks:int,
                   gray_diagonal: bool = False
                  ):
    """
    trick_prob_matrix: takes the 8x8 probability matrix for p2 trickss that was calculated 
    by calc_probability in computing.py
    draw_tricks_prob_array: the 8x8 probability matrix that calculated the draws between p1 and p2's tricks
    n_decks: the n_decks number that was used for generating the decks. Used in the heatmap title.
    gray_diagonal: a boolean that is used to either choose to (or not choose to) gray out the 
    diagonal on the heatmap
    
    Creates a heatmap for visualizing the probability results calculated by calc_probability
    """

    # sets up the path for Heatmaps to be loaded into figures folder 
    figure_dir = "figures"  
    os.makedirs(figure_dir, exist_ok=True)
 
    card_annot = make_annotation(np.ceil(trick_prob_matrix), draw_tricks_prob_array)

    # If gray_diagonal is enabled, mask diagonal values
    if gray_diagonal:
        card_prob_array = trick_prob_matrix.astype(float)
        np.fill_diagonal(trick_prob_matrix, np.nan)

    fig, ax = plt.subplots(figsize=(10, 8))
    
    # creates the heatmap
    sns.heatmap(trick_prob_matrix,
                      cmap="Blues", 
                      vmin=0, 
                      vmax=100, 
                      annot=card_annot,
                      fmt = '',
                      linewidths = 1,
                      cbar=False,
                      xticklabels=ALL_PATTERNS,
                      yticklabels=ALL_PATTERNS,
                      ax=ax
                      )

   
    ax.set_title(f"My Chance to Win(Draw) by Tricks \n N = {n_decks}")

    ax.set_xlabel('My Choice')
    ax.set_ylabel('Opponent Choice')
    
    plot_title = f"Heatmap for the tricks {n_decks}"
    
    # saves the heatmap into the figures folder
    figure_path = os.path.join(figure_dir,plot_title)
    fig.savefig(figure_path,bbox_inches = 'tight', facecolor = 'white')

    return