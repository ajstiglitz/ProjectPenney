import numpy as np
import json
import os
from datetime import datetime as dt

from src.helpers import PATH_DATA

PATH_TO_LOAD = os.path.join('data','to_load')
HALF_DECK_SIZE = 26

def get_decks(n_decks: int,
              seed: int,
              half_deck_size: int = HALF_DECK_SIZE
             ) -> tuple[np.ndarray, np.ndarray]:
    """
    n_decks: number of decks that will be generated
    seed: the random seed that can be set for reproducibility
    half_deck_size: a global variable to set the size of half of the deck

    Efficiently generate `n_decks` shuffled decks using NumPy.
    
    Returns:
        decks (np.ndarray): 2D array of shape (n_decks, num_cards), 
        each row is a shuffled deck.

    """
    init_deck = [0]*half_deck_size + [1]*half_deck_size  # Base deck
    decks = np.tile(init_deck, (n_decks, 1))
    rng = np.random.default_rng(seed)
    rng.permuted(decks, axis=1, out=decks)
    
    return decks


def timestamp() -> str:
    """
    Creates a timestamp
    """
    t = str(dt.now())
    r = t.replace(' ', '-').replace(':', '-').replace('.', '-')
    return r


# Stores data generated by get_decks()
def store_decks(n_decks: int,
                seed: int, 
                result_decks: np.ndarray,
                path_data: str = PATH_DATA
               )-> dict:
    
    """
    n_decks: number of decks
    seed: random seed that can be set for reproducibility
    result_decks: the np.ndarray from get_decks()
    path_data: the path for where the data will go
    
    Stores the data generated by get_decks() function into
        .npy file and .json file
    Seed and num_decks stored separately from random decks
    """

    # Code to create a directory
    os.makedirs(PATH_TO_LOAD, exist_ok=True)

    # Creates a timestamp
    ts = timestamp()

    # Name of the file that will be saved
    npy_file = f"seed{seed}_decks{n_decks}_timestamp{ts}.npy"
    npy_path = os.path.join(PATH_TO_LOAD, npy_file)

    json_path = os.path.join(path_data, 'settings.json')
    
    # if file exists, then load it. If not, then create new one.
    if os.path.exists(json_path):
        with open(json_path,'r') as f:
            settings = json.load(f)
    else:
        settings = {}
            
    if npy_file in settings:
        return settings

    # Code to save the decks into the npy file
    np.save(npy_path, result_decks)

    # The information that gets saved into the .npy file
    settings[npy_file] = {}
    settings[npy_file]['seed'] = seed
    settings[npy_file]['n'] = n_decks


    with open(json_path, 'w') as f:
        json.dump(settings, f)
    
    return settings