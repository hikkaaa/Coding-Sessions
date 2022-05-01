# The game program consists in the computer randomly choosing a word that we have to guess. 
# We need to import random for the computer randomly pick a word
# We need a long list of words
import random
from words import words 
import string
from visual import lives_visual

# First step: make the computer start playing (choosing the word we have to guess)

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    # suppose the user has lives (a max number of mistakes)
    lives = 7

    # get user input
    # iterate while the length of the word is greater than 0 and lives greater than 0:
    while len(word_letters) > 0 and lives > 0:
        # There are several things that we can add for the user 
        # We can retun letters used and the lives left so that the user can keep track of them
        # use .join() to turn the list of used words into a string (with space between each letter)
        print('You have', lives ,' lives left. You have used these letters: ', ' '.join(used_letters))

        # the user also has to visualize the current state of the word ( - for non-guessed letters and guessed letters)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        # if user input is a valid alphabet letter and the user didn't type it before
        if user_letter in alphabet - used_letters:
            # add user letter to used letters of alphabet (letters already typed bu users)
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else: 
                # user's lives diminish 
                lives -= 1
                print('Ops! Letter is not in word.')

        elif user_letter in used_letters:
            print('You already used that character. Try again: ')
        else:
            print('You typed an invalid character! Try again: ')
    
    if lives == 0: 
        print('Oh no! You died! :( The correct word was ', word)
    else:
        # as soon as the user guesses the word or numer of lives left is 0, it exists the while loop
        print('WOW! You guessed the word ', word , ' correctly! :)')


if __name__ == '__main__':
    hangman()

