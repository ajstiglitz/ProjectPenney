import src.processing
import pandas as pd
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt

from src.computing import calc_probability
ALL_PATTERNS = ['RRR', 'RBR', 'BRR', 'BBR', 'RRB', 'RBB', 'BRB', 'BBB']


# create a heatmap that that uses the stored decks and scores rather than doing any kind of simulation itself
def decks_heatmap():
    """
    Creates a heatmap for visualizing the probabilities of winning based on the scored decks
    """
    prob_matrix = calc_probability()
    plt = sns.heatmap(prob_matrix, cmap="crest", 
                      annot=True, linewidths = 0.5, 
                      xticklabels=ALL_PATTERNS, yticklabels=ALL_PATTERNS,)

    return plt