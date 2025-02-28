### ProjectPenney Overview
---

### Description
The purpose of this code is to simulate Penney's Game and find the probability of a player winning based on the pattern of 3 that they chose. Those probabilities are then put in a heat map for an easier visualization. 

----

### Quickstart: how to use UV
This repository uses version 3.12 of Python, 3.10.0 of Matplotlib, 2.2.2 of Numpy, and 2.2.3 of Pandas
- it was set up using a virtual environment

Here is a link to the UV website to learn how to install for yourself: https://docs.astral.sh/uv/

----

### Breakdown of the Different .py Files
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
Used for debugging. This file contains a wrapper function.

### 4) Processing
This file is for scoring the decks based on the player sequences. 

### 5) Visualization
This file has a function for showing a heatmap based on the probability of a player winning depending on their sequence choice. Later on, a second heatmap based on the probability of a choice resulting in a draw will be added.

----

### How to use the Project
This project contains a .ipynb file called "WorkingCode" which walks you through the process of creating your decks, scoring them, and getting the probabilities.
- you can delete "settings", "scores", and the data in the "loaded" folder if you want to start all of the tests over.
- you can also just run the decks some more and the new tests will be added into the settings, and you can re-run the scoring and other functions for updated results.