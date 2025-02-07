import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    print(np.random.random())
    return 42


#if you invoke this script from the command line, the top main has nothing to do with the main down here
# if you import it into a notebook it would be main but it wouldnt have the underscores
#what you are doing is that if this thing is supposed to be run from the command line
if __name__ == '__main__':
    main()