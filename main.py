from src.runcode import run_code, get_visualizations

if __name__ == '__main__':
        
    print("Welcome to Project Penney Simulation!")
    menu_check = int(input("0. Run the Simulation to get Probabilities \n1. Cancel\n"))

    if menu_check == 0:
        # Ask user for n_decks
        n_decks = int(input("Enter number of decks to simulate: "))

        # Ask user for the seed
        seed = int(input("Seed for reproducibility: "))

        #line break
        print("")

        # total amount of decks. Can check the settings.json and add the n_decks there for correct amount
        total_decks = int(input("What is the total amount of decks used (for calculation purposes)\nNOTE: "
        "If you uploaded this from git, there were 1M files already loaded.\nAdd your n_decks number to get the correct value for an accurate calculation"
        "\nIf you deleted those loaded files and are starting from scratch, just use your n_decks number: "))

        #Runs the code
        card_prob_matrix, trick_prob_array, draw_cards_prob_array, draw_tricks_prob_array= run_code(n_decks,total_decks,seed)

        #asks if user wants to create the visualization
        pause = str(input("Would you like the visualization? (Y/N): "))

        if pause == "Y":
            #creates the heatmaps for cards and tricks
            get_visualizations(card_prob_matrix, trick_prob_array, draw_cards_prob_array, draw_tricks_prob_array, total_decks)

        else:
            ("The End.")

    elif menu_check == 1:
        print("The End.")
        