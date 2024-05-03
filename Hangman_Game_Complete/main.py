import random
import hangman_words
import hangman_art

def play_hangman():
    # Update the word list to use the 'word_list' from hangman_words.py
    # Delete this line: word_list = ["ardvark", "baboon", "camel"]
    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    # Testing code
    print(hangman_art.logo)
    print(f'Pssst, the solution is {chosen_word}.')

    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    guessed_letters = set() # Set to store guessed letters

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Letter has been guessed. Try another letter")
            continue  # Skip the rest of the loop and go back to asking for a guess

        guessed_letters.add(guess)  # Add the guess to the set of guessed letters

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            lives -= 1
            print("\n\nLetter not found. Please try again")
            print(f"Your remaining attempts :{lives}")
            if lives == 0:
                end_of_game = True
                print("\n\nYou lose!!!!!!!!!!!!!!!!")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(hangman_art.stages[lives])

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thank you for playing!")

# Start the game
play_hangman()
