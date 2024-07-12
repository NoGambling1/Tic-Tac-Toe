from functools import reduce
from time import sleep
from colorama import Fore

gameWon = False
gameArray = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
user = ""
personToGo = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# -----------------------------------------

def addMove(spot, user): 
    if spot in range(4): gameArray[spot-1] = user
    elif spot in range(4, 7): gameArray[spot-1] = user
    else: gameArray[spot-1] = user

# -----------------------------------------

def checkWin(user1, user2):
    # Check rows
    if (gameArray[0] == gameArray[1] == gameArray[2] == user1 or
        gameArray[3] == gameArray[4] == gameArray[5] == user1 or
        gameArray[6] == gameArray[7] == gameArray[8] == user1):
        return f"User 1 ({user1}) won the game!"
    if (gameArray[0] == gameArray[1] == gameArray[2] == user2 or
        gameArray[3] == gameArray[4] == gameArray[5] == user2 or
        gameArray[6] == gameArray[7] == gameArray[8] == user2):
        return f"User 2 ({user2}) won the game!"


    if (gameArray[0] == gameArray[3] == gameArray[6] == user1 or
        gameArray[1] == gameArray[4] == gameArray[7] == user1 or
        gameArray[2] == gameArray[5] == gameArray[8] == user1):
        return f"User 1 ({user1}) won the game!"
    if (gameArray[0] == gameArray[3] == gameArray[6] == user2 or
        gameArray[1] == gameArray[4] == gameArray[7] == user2 or
        gameArray[2] == gameArray[5] == gameArray[8] == user2):
        return f"User 2 ({user2}) won the game!"


    if (gameArray[0] == gameArray[4] == gameArray[8] == user1 or
        gameArray[2] == gameArray[4] == gameArray[6] == user1):
        return f"User 1 ({user1}) won the game!"
    if (gameArray[0] == gameArray[4] == gameArray[8] == user2 or
        gameArray[2] == gameArray[4] == gameArray[6] == user2):
        return f"User 2 ({user2}) won the game!"


    return "The game ended in a draw."

# -----------------------------------------

def checkArr(arr):
    counterAgain = 0
    checkArr = []
    checkArrTrue = []
    for val in arr:
        if val != " ": checkArr.append(counterAgain) # pos of taken spots starting from 0
        else: checkArrTrue.append(counterAgain)
        counterAgain += 1
    #print(checkArr)
    return checkArr

# -----------------------------------------

def checkArrTrue(arr):
    counterAgain = 0
    checkArrTrue = []
    checkArr = []
    for val in arr:
        if val != " ": checkArr.append(counterAgain+1) # pos of taken spots starting from 0
        else: checkArrTrue.append(counterAgain+1)
        counterAgain += 1
    #print(checkArrTrue)
    return checkArrTrue

# -----------------------------------------

def buildFullBoard(arr):
    counter = 0
    counter1 = 1
    checkARR = checkArr(gameArray)
    for z in range(3):
        for x in range(3):
            print (Fore.GREEN + "[" + str(gameArray[counter]).translate({39: None}) + "] ", end="")
                
            counter += 1
        print(Fore.BLUE + "| ",end="")
        
        for y in range(3):    
            if checkARR != []:
                if counter1 - 1 in checkARR: print (Fore.RED + "[" + str(" ").translate({39: None}) + "] ",end="")
                else: print (Fore.RED + "[" + str(counter1).translate({39: None}) + "] ",end="")
            else: print (Fore.RED + "[" + str(counter1).translate({39: None}) + "] ",end="")
            counter1 += 1
        print("\n")
# -----------------------------------------
print("Welcome to Tic-Tac-Toe, Shitty NoGambling addition!")
sleep(1)
while True:
    user1 = input("Is user 1 \"x\" or \"-\"?  ")
    if not (user1 == "x" or user1 == "-"): 
        print ("That is not a valid input, please try again.") 
        continue
    else: break

if (user1 == "x"): user2 = "-"
else: user2 = "x"
print ("User 1 is playing " + user1 + ", while User 2 is playing " + user2)
sleep(0.5)
turn = 0
while True:
    buildFullBoard(gameArray)
    print (Fore.CYAN + "--------------------------" + Fore.RESET)

    sleep(0.5)
    if (turn % 2 == 0): personToGo = 1 # Deciding who goes
    else: personToGo = 2
    while True:
        if personToGo == 1: 
            pos = input("Which spot would you like to go, User 1 (" + user1 + ")? ")
        else: 
            pos = input("Which spot would you like to go, User 2 (" + user2 + ")? ")
        pos = int(pos)

        if not (pos in checkArrTrue(gameArray)): 
            print("That is not a valid input, please try again")
            sleep(0.1)
            continue
        else: 
            break
    if (personToGo == 1): 
        addMove(pos, user1)
    else: 
        addMove(pos, user2)
    turn += 1
    sleep(0.3)
    
 
    result = checkWin(user1, user2)
    if result != "The game ended in a draw.":
        print(Fore.MAGENTA + result)
        break  
