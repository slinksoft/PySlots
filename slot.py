import random
from os import system
from time import sleep
print('''Welcome to PySlots!
You'll start with $50.
Answer with yes/no. you can also use y/n. Case sensitivity does not apply.
To win you must get one of the following combinations:
BAR\tBAR\tBAR\t\tpays\t* 10 of stake
BELL\tBELL\tBELL/BAR\tpays\t * 5 of stake
PLUM\tPLUM\tPLUM/BAR\tpays\t * 3.5 of stake
ORANGE\tORANGE\tORANGE/BAR\tpays\t * 3 of stake
CHERRY\tCHERRY\tCHERRY\t\tpays\t * 2.5 of stake
CHERRY\tCHERRY\t  -\t\tpays\t * 2 of stake
CHERRY\t  -\t  -\t\tpays\t * 1 of stake
''')

#Constants:
INIT_CREDITS = 50
ITEMS = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR"]
CONST_TIME = 120

def setGlobals():

    global stake, credit, firstWheel, secondWheel, thirdWheel
    firstWheel = None
    secondWheel = None
    thirdWheel = None

    credit = INIT_CREDITS

def play():
    global stake, credit, firstWheel, secondWheel, thirdWheel
    isPlaying = True
    while (isPlaying == True and credit > 0):

        print("You have $" + str(credit) + ".")
        answer = input("Play PySlots?: ")
        answer = answer.lower()
        if (answer.lower() in ["yes", "y"]):
            stake = int(input("How much do you want to bet? $"))
            spinWheel(CONST_TIME)
            processScore()
        elif (answer.lower() in ["no", "n"]):
            print("You ended the game with $" + str(credit) + " in your hand.")
            input()
            break
        else:
            print("wrong input!")
    if (credit <= 0):
        print("You are out of credits!")


def spinWheel(time):
    '''
    returns a random item from the wheel
    '''
    t = time
    s1 = False
    s2 = False
    s3 = False
    global firstWheel, secondWheel, thirdWheel
    while (t >= 0):
        if (s1 == False):
            firstWheel = ITEMS[random.randint(0, 5)]
        if (s2 == False):
            secondWheel = ITEMS[random.randint(0, 5)]
        if (s3 == False):
            thirdWheel = ITEMS[random.randint(0, 5)]

        print(firstWheel + '|' + secondWheel + '|' + thirdWheel)
        t -= 1;

        if (t == 80):
            s1 = True
        if (t == 40):
            s2 = True
        if (t <= 0):
            s3 = True
        sleep(.01)
        system('cls')

def processScore():
    '''
    prints the current score
    '''
    global stake, credit, firstWheel, secondWheel, thirdWheel
    if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
        win = stake
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
        win = stake*2
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "CHERRY")):
        win = stake*2.5
    elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and ((thirdWheel == "ORANGE") or (thirdWheel == "BAR"))):
        win = stake*3
    elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and ((thirdWheel == "PLUM") or (thirdWheel == "BAR"))):
        win = stake*3.5
    elif((firstWheel == "BELL") and (secondWheel == "BELL") and ((thirdWheel == "BELL") or (thirdWheel == "BAR"))):
        win = stake*5
    elif((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
        win = stake*10
    else:
        win = stake * -1

    credit += win
    print("Result: \n" + str(firstWheel) + "|" + str(secondWheel) + "|" + str(thirdWheel) )
    if(win > 0):
        print("You won! Profit: $" + str(win))
    else:
        print("You lost!")

setGlobals()
play()