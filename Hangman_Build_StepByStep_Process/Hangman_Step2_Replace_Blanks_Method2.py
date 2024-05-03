#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

"""
we use the range and count how many letters and 
filled the display list with "_"
"""
#because we are not using any variable, and just looping. We can use blank it with underscore
display = []
word_length = len(chosen_word) #the length of the word eg, 4, 5, 8

for _ in range(word_length): #0 - 'X' length we replaced it with _
    display += "_"

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
"""
The 'position' is used to iterate through each letter of chosen_word and check if it matches the user's guess.

For example, 'Camel' was the chosen_word. So, the range from 0 to word length 5 

for position in range(0,5):

if we type in 'a', and check each letter if c = a. Since it is False, it goes back to the for loop.

next letter = 'camel'[1] a = a, since it is true, it get into the list 'display' and replace the second char that is matching.. 

and this loop continues until it finished scanning through all the characters

"""

for position in range(word_length): 
    letter = chosen_word[position] 
    if letter == guess:
        display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)