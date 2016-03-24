#Juan Marcos Mendez
import random
sticks = 21

def playGame():
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        if subtractSticks( userChoice ):
            print('You lost!')
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(computerChoice) )
        if subtractSticks( computerChoice ):
            print('Computer lost!')
            break
#################################################        
def askUserChoice():                            #
    numbers = [1,2,3,4]                         # list of number only allowed
    user = ''                                   # user pick
    while user not in numbers:                  # Saying user can only pick from these numbers
        print('Pick a number. Only 1-4')        # Display
        user = int(input())                     # Asking user to pick
        if user not in numbers:                 # If user didnt pick right then
            print('OOPS try again. 1-4 only')   # Display
        else:                                   # if worked then
            return int(user)                    # do this
def subtractSticks( number ):                   #
    global sticks                               #
    sticks = sticks - number                    # what was asked for
    if sticks <= 0:                             # if sticks is zero
        return True                             # then ture you win
    else:                                       # or 
        return False                            # lose
def determineComputerChoice():                  #
    computerChoice = random.randint(1,4)        # computer random number picking
    return computerChoice                       # return the number to your code part
#For the the computer random number i had to look online didnt know it.
#Also i got some advice from people that know this better then i do.
