# With this code we are going to implement a game in which the computer has a secret number and the user is trying to guess that secret number.

# First step: the computer has to generate a secret number that the user has to guess. 
import random 

def guess(x):
    # This generates a random number between 1 and x
    random_number = random.randint(1, x)

    # Second step: the user makes its guess in the terminal, then the computer will tell if the guess is too high, too low, or correct. 
    # It is necessary a loop until the user guesses the right number.
    # As we don't have a predefined universe to iterate over, we can use a While Loop. 
    # The loop has to stop when the user guesses the right number.
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Try again. Your guess is too low :( ")
        elif guess > random_number:
            print("Try again. Your guess is too high :( ")
        
        # In this if-statement it is not necessary to code also the case when guess == random_number because the while loop would never start for that value of guess. 

    print(f"YAS!!! CONGRATS!!! You have guessed the number {random_number} correctly :) ")
       

# Ok, you did it!! Now, call the function setting as parameter an upper bound for the random generator.

guess(10)
        

