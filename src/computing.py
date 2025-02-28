import numpy as np
import pandas as pd
import os

CSV_PATH = os.path.join('data', 'scores.csv')

# The sole purpose of this module is to read in the already computed scores
# and turn them into an 8x8 array of probabilities

def calc_probability(csv_file:str = CSV_PATH):
    df = pd.read_csv(CSV_PATH,dtype={'p1pattern': str, 'p2pattern': str})
    df = df.drop(columns = ['p1_pattern','p2_pattern'])




    return np.ndarray


