import random
from Words import words
import string

# We have to keep choosing a word until we get a valid word that we can guess in hangman.
def get_valid_word(words):
    word = random.choice(words) # will randomly choose a word from the list.

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    # to keep the track of what is valid letter.
    word = get_valid_word(words)
    word_letter = set(word) # will save all the letters in a word as a set.
    alphabet = set(string.ascii_uppercase)
    used_letter = set() # to keep track of what the user has guessed.
    
    # getting user input
    while len(word_letter) > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letter))

        # what current word is (i.e. W - R D)
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('\nGuess a letter: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

        elif user_letter in used_letter:
            print("You have already used that character. Please Try Again.")

        else:
            print("Invalid character.TRY AGAIN")  

# user_input = input("Type something: ")
# print(user_input)

hangman()
