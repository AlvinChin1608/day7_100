#Challenge 1 
#Step 1 
import random 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print the word Right for matches and wrong 

"""
The enumerate function in Python is a built-in function that adds a counter (index) to an iterable object (like a list, string, or tuple) and returns it as an enumerate object. This enumerate object is essentially an iterator that produces a sequence of tuples, where each tuple contains two elements:

fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
  print(f"Index: {i}, Fruit: {fruit}")

"""
#My solution using enumerate and append 
"""
matching_indices = [] #create empty index

for i, letter in enumerate(chosen_word):
  if letter == guess:
    matching_indices.append(i) #the numeric index whereabout
  is_match = i in matching_indices #now we put the matched indices here
  if is_match == False:
    print("Wrong")
  else:
    print("Right")
"""
# Solution 2 for Todo 3 challenge.. ^^^ just realised the above code was unnecessarily complicated 

for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("wrong")

