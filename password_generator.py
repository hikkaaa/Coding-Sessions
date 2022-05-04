#this program generates a password. The length of password is given by user input. 
# The computer also asks the user how many passwords she/he wants to generate. 

# import random as the computer generate passwords using random characters
import random 
import string

print('Welcome to your Password Generator!')

# this variable is an empty string that should contain all characters type (capital, lowercase letters, numbers, special characters, etc...)
def generate_password():
    number_password = int(input('Enter the amount passwords you want to generate: '))
    length = int(input('Enter the length of the password you want to generate: '))

    characters = string.ascii_letters + string.digits + string.punctuation

    while number_password > 0: 
        password = "".join(random.sample(characters, length))
        print(password)
        
        number_password -=1

generate_password()



