import random

def play():
    # we must have two inputs: the user's choice and the computer's choice
    # ask for user input to know user's choice
    # used lower() because we want the input to be ok as long as the user types one of the accepted letters (doesn't matter if in upper or lower cases)
    user = (input(" Hello to Rock, Paper, Scissors! Game. \nType 'r' for rock, 'p' for paper or 's' for scissors.\n")).lower()
    # computer's input comes from the random choice between r, p and s 
    # GAME THEORY: The best strategy for this game is nonetheless a random strategy. 
    # This is the strategy the human player use, hence we recreate the same for the computer through random.choice()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It\'s a tie!"
    
    # make a function that states when a player wins (line 24)
    if is_win(user, computer):
        return "YEY! CONGRATS!!! YOU WON."
    
    # default case, returns automatically if the previous if statements are not satisfied
    return "OH NO! YOU LOST :( "



def is_win(player, opponent):
    # this function returns true when the player wins against the opponent
    if (player == 'r') and (opponent == 's') or (player == 's') and (opponent == 'p') \
        or (player == 'p') and (opponent == 'r'):
        return True

print(play())

