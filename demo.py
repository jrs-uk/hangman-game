import random

def import_word():
    global randomword
    randomword = random.choice(open("./words.txt").read().split())

def guess_word():
    """
    PythonForBeginners, "Python Hangman Game", https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman, assessed 7/12/2020
    """
    guesses = '' #Creates empty variable 'guesses'
    attempts = 10 #Sets the amount of attempts a player has to guess

    while attempts > 0: #Creates a while loop that will run if the variable attempts is greater than 0.
        remaining_letters = 0 #Creates a variable 'remaining_letters' with value 0 for counting the remaining letters not guessed.
        display_text = '' #Creates empty variable 'guesses'
        print("\n") # Enter down a new line for spacing
        
        for char in randomword: #Creates for loop, for every character in the random word.
            if char in guesses: #If the character the player has guessed is in the word
                display_text += char + " " #Adds the current character from the random word and a space to the variable display_text
            else:
                display_text += "_" + " " #Adds an underscore and a space to the variable display_text
                remaining_letters += 1 #Add 1 to the variable 'remaining_letters' for an remaining_letters letter guess
        print(display_text) #Output the variable 'display_text' - contains current correctly guessed letters in the word and underscores

        if remaining_letters == 0: #if all letters have been guessed correctly.
            print("\nWord Guessed, you got it! The word was,", randomword,"- Going back to main menu")
            attempts = 0 #Set remaining attempts to 0 to end while loop
            return #Leave game

        """Player Menu - Asks player if they want to continue or need a hint"""
        correct_input = 0 #Creates variable 'continue_game' with the value 0

        """
        While loops to ensure input is correct, ends if correct value 1 to 4 is input,
        and does not run when the attempts variable is at 10 so the menu does not appear when first calling this function,
        and also when the attempts variable is at 0 as the game will be over.
        """
        while correct_input == 0 and (not attempts == 10) and (not attempts == 0): 
            continue_game = input("\nWhat would you like to do?\n1. Guess again\n2. Reveal hint\n3. Reveal word\n4. Quit\n\n")
            if continue_game == "1": #If continue_game has the value 1, continue program
                correct_input = 1 #Set correct_input to 1 to end player menu loop
            if continue_game == "2": #If continue_game has the value 2, reveal a hint
                #Function for hint reveal here
                print("Hint")
                correct_input = 1
            elif continue_game == "3": #If continue_game has the value 3, reveal the word
                print("The word was,",randomword,", better luck next time!")
                attempts = 0 #Set attempts to 0 to end round
                correct_input = 1
            elif continue_game == "4": #If continue_game has the value 4, End game
                print("Thanks for playing!")
                attempts = 0
                quit() #Quit script
                correct_input = 1
        """End of player menu"""

        player_guess = input("\nPlease enter a character:") #Ask player to guess a letter

        guesses += player_guess #Add players guess to the variable 'guesses'
        if player_guess not in randomword: #If players guess is not in the random word
            attempts -= 1  #remove 1 from the variable attempts
            print("\nThat letter is not part of the word, you have,",attempts,"attempts remaining.")
            
        if attempts == 0: #If the variable 'attempts' has the value 0, end loop
            print("\nUnlucky, you ran out of attempts.")




        

play = 1
while play == 1:
    option = input("Welcome to Hangman, are you ready? Select an option to begin.\n\n1: Play\n2: Quit\n")
    if option == "1":
        import_word()
        guess_word()
    elif option == "2":
        play = 0
        quit()
