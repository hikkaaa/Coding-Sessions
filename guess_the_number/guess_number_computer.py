# This version of the game sees the computer guessing user's number.

import random

def computer_guess(x):
    # Set lower and upper bound for the set of numbers the computers has to choose from
    low = 1
    high = x

    # initialize a feedback variable
    feedback = " "

    while feedback != "c" :

        # This time we don't want as parameters 1 and x because we want the computer to change these bounds depending on the user's feedback. 
        # if user feedback is "too high" -->  the computer has to stop considering anything above that.
        # if user feedback is "too low" --> the computer has to stop considering anything below that.

        if low != high :   
            guess = random.randint(low, high)
        else: 
            # it is the as same setting guess = high because low = high
            guess = low 

        # The computer asks for user feedbacks
        # Add lower() method at the end to lowecase that the string frokm input.
        # THEORY: If you try to compare a capital letter to its lowercase letter, they come out not to be equal. 

        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        
    # Exit the while loop when the the computer guesses the user's number, that is, when feedback == 'c'
    print(f"YAS! THE COMPUTER GUESSED THE NUMBER {guess} CORRECTLY!!! :)")


computer_guess(10)