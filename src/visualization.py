import src.processing
import pandas as pd
import seaborn as sns # type: ignore


# create a heatmap that that uses the stored decks and scores rather than doing any kind of simulation itself
#grey out patterns played against itself (like RRR and RRR for p1 and p2)
#can put NaNs in
#also can do % as whole number
# like 49% winning and 3% draw
#put in some indication of the sample size when the visualization pops up

#show everything (other than the diagonal)

def decks_heatmap(csv_path):
    """
    Creates a heatmap for visualizing the ideas on the Penney Game Wiki 
    (should have similar probability results)
    """
    data = pd.read_csv(csv_path,index_col=0)
    g = sns.heatmap(data)
    
    return

