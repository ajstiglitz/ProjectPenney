### ProjectPenney Overview
---

### Description
The purpose of this code is to simulate Penney's Game and find the probability of a player winning based on the pattern of 3 that they chose. Those probabilities are then put in a heatmap to visualize. 

Penney's Game is a two player sequence game where players choose a binary sequence with a length of three or more. These binaries can include something like heads or tails for a coin, or the colors red or black for a card deck. The combinations that the players choose are then scored based on their number of occurences. In the case of players using a card deck, they are scored based on the number of cards they end up with at the end, and the number of tricks that they have (where "tricks" refers to when their pattern comes up and a new round of the game starts).

There are certain combinations that a player can choose that will increase their pobability of winning. Player 2 will always have a better chance of winning than Player 1 simply for the fact that they pick their sequence second. The method for them to win would be to choose their sequence based on the idea of (~2-1-2). Where Player 2 chooses the inverse of Player 1's second choice for their first pick, and so on. 

For a game with a sequnce of 3, there are 8 possible combinations.

Link to Penney's Game Wiki: https://en.wikipedia.org/wiki/Penney%27s_game 

---

### How to use the Project
This project contains a .ipynb file called "WorkingCode" which walks you through the process of creating your decks, scoring them, and getting the probabilities.
- You can delete "settings", "scores", and the data in the "loaded" and "to load" folders if you want to start all of the tests over.
- You can also simply run the decks and new tests will be added into the settings, which you then can re-run for updated results.
- Make sure that when you are running the code for the visualization that you change the integer for n_decks to match the one you used to generate the decks so the title is correct.

----

### Quickstart: how to use UV
This repository uses version 3.12 of Python, 3.10.0 of Matplotlib, 2.2.2 of Numpy, and 2.2.3 of Pandas
- And it was set up using a virtual environment

Here is a link to the UV website to learn how to install for yourself: https://docs.astral.sh/uv/

----

### Files of ProjectPenney Repository
- data/
    - Contains the folders for loaded and to_load
    - It is also where the scores.csv and settings.json files will be saved to when the code is run

- figures/
    - Where the heatmaps of the probability of winning will be saved to

- src/
    - Contains the code for:
        - A debugging wrapper
        - Generating the decks
        - Saving the decks
        - Scoring the decks 
        - Saving the scores
        - And visualizing the probabilities with heatmap

---

### Breakdown of the Different .py Files in src
1. Computing
2. Datagen
3. Helpers
4. Processing
5. Visualization

### 1) Computing
The purpose of this file is to calculate the probability of the scores.

### 2) Datagen
The purpose of this file is to generate decks and save them to the disk.

### 3) Helpers
The purpose of this code is for debugging. This file contains a wrapper function.

### 4) Processing
This file is for scoring the decks based on the player sequences. 

### 5) Visualization
This file has a function for showing a heatmap based on the probability of a player winning depending on their sequence choice. Later on, a second heatmap based on the probability of a choice resulting in a draw will be added.