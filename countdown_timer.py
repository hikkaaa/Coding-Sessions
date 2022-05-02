# main concept: loops + use python library time
# for the countdown, the computer asks the user to enter the time in seconds
# The computer is going to countdown starting from the user's time 

#time is the library that deals with everything related to time in Python
import time

def countdown(t):
    while t:
        # use divmod: 
        # divmod() performs division on two numbers and returns both quotient and remainder
        #in this case: quotient= minutes, remainder= seconds
        mins, secs = divmod(t, 60)
        # 02d formats an integer (d) to a field of minimum width 2
        timer= "{:02d}:{:02d}".format(mins, secs)
        # Use the syntax print(string, end = "\r") to make the next stdout line begin at the beginning of the current line. 
        # As a result, string is overwritten by the following print() statement.
        print(timer, end="\r")
        # the time must stop when the time= 1.
        time.sleep(1)
        t-= 1
    print("Time is over!")

# ask user for time input
t= int(input("Enter the time in seconds: "))

countdown(t)