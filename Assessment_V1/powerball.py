from random import sample, choice
from collections import Counter, OrderedDict
from string import capwords
import sys

def main():
    '''Execute the code from here'''
    
    
    while True:
        try:
            numPlayers = int(input("Enter number of Players: "))
            break
        except KeyboardInterrupt:
            print("Exiting the program...")
            sys.exit(0)
        except:
            print("Enter a valid number")
    
    if numPlayers is 1:
        name = playerName()
        num = chooseNumbers()
        
        print("{} {}, Powerball: {}".format(name, num[:5], num[-1]), end='\n\n')
       
        print("Powerball Winning Number")
        print("{}, Powerball: {}".format(winningNumbers()[0], winningNumbers()[1]))
       
    else:
        names, numbers = [], []
        
        for _ in range(numPlayers):
            names.append(playerName()) 
            numbers.append(chooseNumbers())
        
        pBallFinal = getPballFinal(numbers)
        
        for name, number in zip(names, numbers):
            print("{} {}, Powerball: {}".format(
                  name, number[:5], number[-1]), end = '\n\n')

        print("Powerball Winning Number")
        print("{}, Powerball: {}".format(pBallFinal[0], pBallFinal[1]))


def playerName():
    '''Enter each player name'''
    
    
    while True:
        fName = input("Enter First Name: ")
        lName = input("Enter Last Name: ")
        
        if fName is '' or (not fName.isalpha()) or lName is '' or (not lName.isalpha()):
            print("Enter correct details", end = '\n\n')
            continue
        else:
            break
        
    return capwords(fName) + ' ' + capwords(lName)


def chooseNumbers():
    '''Player Chooses numbers and Powerball number'''
    
    
    numbers, i = [], 1
    
    #validate the entries being entered into the numbers list
    while i < 6:
        try:
            num = int(input("From 1 to 69, enter number {}: ".format(i)))
            if num not in numbers and num < 70 and num > 0:
                numbers.append(num)
                i += 1
            else:
                print("Enter a unique number and less than 70")
        except KeyboardInterrupt:
            print("Exiting the program...")
            sys.exit(0)
        except:
            print("Enter correct details")
            continue
            
    numbers.sort()   
    
    while True:
        pballNumber = int(input("Enter PowerBall number: "))
        if pballNumber in numbers or pballNumber > 26:
            print("Enter unique powerball number and less than 27..")
            continue
        else:
            break
            
    numbers.append(pballNumber)
    print()
    
    return numbers     

    
def getPballFinal(numbers):
    '''Choose the winning number of Powerball from given unique numbers'''

    
    temp = []
    for i in numbers:
        temp.extend(i)
    
    #keeping the count of each element in descending order in a dictionary        
    maxCommon = OrderedDict(Counter(map(str, temp)).most_common(6))
    
    tempKeysList = list(maxCommon.keys())
    tempValuesList = list(maxCommon.values())
    
    fList = getBall(tempKeysList, tempValuesList)
    
    return fList


def getBall(Keys, Values):
    '''Get the final values of Powerball numbers'''
    
        
    if Values.count(Values[0]) > 1:
        ctr = Values.count(Values[0])
        pBall = choice(Keys[:ctr])        

    elif Values.count(Values[0]) == 1:
        pBall = Keys[0]
    
    Keys.remove(pBall)
    final = sorted(list(map(int, Keys)))
    
    return final, int(pBall)
    

def winningNumbers():
    '''Randomly select the winning numbers and Powerball numbers'''
    
    
    while True:
        regBalls = sorted(sample(range(1, 70), 5))
        powerBall = choice(range(1, 27))
        
        if powerBall in regBalls:
            continue
        else:
            break
            
    return regBalls, powerBall
        
        
if __name__ == "__main__":
    main()
    