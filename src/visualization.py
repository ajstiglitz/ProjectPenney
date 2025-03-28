import src.processing
import pandas as pd
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt
import os

from src.computing import calc_probability
ALL_PATTERNS = ['RRR', 'RBR', 'BRR', 'BBR', 'RRB', 'RBB', 'BRB', 'BBB']


# creates a heatmap that that uses the stored decks and scores, rather than doing any kind of simulation itself
def decks_heatmap(prob_matrix: pd.DataFrame,
                  n_decks:int):
    """
    prob_matrix: takes the 8x8 probability matrix that was calculated 
    by calc_probability in computing.py
    n_decks: the n_decks number that was used for generating the decks. Used in the heatmap title.
    
    Creates a heatmap for visualizing the probability results calculated by calc_probability
    """

    # sets up the path for Heatmaps to be loaded into figures folder 
    figure_dir = "figures"  
    os.makedirs(figure_dir, exist_ok=True)
    
    # n is based on the n_decks from the datagen.py file
    title = f"My Chance of Win(Draw) by ___ When n_decks = {n_decks}"

    # creates the heatmap
    plt = sns.heatmap(prob_matrix, cmap="crest", annot=True, linewidths = 0.5, xticklabels=ALL_PATTERNS, yticklabels=ALL_PATTERNS)
    plt.set_title(title)

    plot_title = f"Heatmap for the {title}"
    
    # saves the heatmap into the figures folder
    figure_path = os.path.join(figure_dir,plot_title)
    fig = plt.get_figure()
    fig.savefig(figure_path,bbox_inches = 'tight', facecolor = 'white')

    return plt