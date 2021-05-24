from itertools import product

def main():
    numberOfDice = int(input("To play the game, Please enter x number of dice(s) you desire to have but is below the number of 10. \nEnter the value of how many dice you want to toss here : "))
    if (numberOfDice > 10) :
        print("ERROR! The value you have typed is higher than 10")
        return ValueError
    else :
        print("You have", numberOfDice, "dices in your hand.")
        facesOfDice = int(input("Please enter the number of faces you want on your dices, please enter a value below or equal to 6 here : "))
        if facesOfDice <= 6:
            print("You have", facesOfDice, "faces on your dice(s).")
            possibilities = facesOfDice ** numberOfDice
            print("For the number of dice you have and faces you gace, there are ", possibilities)
            wantedValue = int(input("Please enter the number you want to calculate the numbber of possibilities you have for x amount of dice and faces here : "))
            listeOfAllFaces = []
            for i in range(1,facesOfDice+1):
                listeOfAllFaces.append(i)

            numberOfPossibilities = 0

            if wantedValue >= numberOfDice*facesOfDice:
                return False, print("False")

            for i in product(listeOfAllFaces,repeat=numberOfDice):
                if sum(i) == wantedValue:
                    numberOfPossibilities+=1

            print ("The number of possibilities are : ", numberOfPossibilities)
        else: 
            print("ERROR! The value you have typed is higher than 6")
            return ValueError

main()

    