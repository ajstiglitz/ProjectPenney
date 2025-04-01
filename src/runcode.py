import importlib
from src.datagen import get_decks, store_decks
from src.processing import update_score
from src.computing import calc_probability
from src.visualization import card_heatmap, tricks_heatmap
import numpy as np

def run_code(n_decks:int,
             total_decks:int,
             seed:int)-> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    n_decks: number of 52-card decks that will be generated
    total_decks: if .npy files are already loaded, the n_decks wont be correct 
    for calculating probability if you add more generated decks. This is used for 
    calc_probaility; you need to add the n_decks to the n seen in the file names for already loaded filed
    to get the right scores.
    seed: the random seed that can be set for reproducibility

    Runs the code itself to create, store, score, and calculate the probability for the generated decks
    """

    # calls the get_decks() function and stores as deck to be used later
    deck = get_decks(n_decks, seed)

    #calls the store_deck() function
    store_decks(n_decks, seed, deck)

    # calls the update_score() function
    update_score()

    card_prob_matrix, trick_prob_array, draw_cards_prob_array, draw_tricks_prob_array = calc_probability(total_decks)

    return card_prob_matrix, trick_prob_array, draw_cards_prob_array, draw_tricks_prob_array


def get_visualizations(card_prob_matrix: np.ndarray,
                       trick_prob_array: np.ndarray,
                       draw_cards_prob_array: np.ndarray,
                       draw_tricks_prob_array: np.ndarray,
                       total_decks: int,
                       seed:int
                       ) -> None:
    """
    card_prob_matrix: the probability array that was calculated for player 2's chances of winning by cards
    trick_prob_array: the probability array that was calculated for player 2's chances of winning by tricks
    draw_cards_prob_array: the probability array that was calculated for the times p1 and p2 had a draw 
    based on cards in a game 
    draw_tricks_prob_array: the probability array that was calculated for the times p1 and p2 had a draw 
    based on tricks in a game 
    total_decks: If .npy files are already loaded, the n_decks wont be correct.

    Takes the results from run_code and creates the two heatmaps for cards and tricks
    """

    card_heatmap(card_prob_matrix, draw_cards_prob_array, total_decks,seed, gray_diagonal=True)

    tricks_heatmap(trick_prob_array, draw_tricks_prob_array, total_decks,seed, gray_diagonal=True)

    return None