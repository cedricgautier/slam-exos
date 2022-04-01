from itertools import product

def main():
    # Asking the user to input the number of dices they want to have.
    numberOfDice = int(input("To play the game, Please enter x number of dice(s) you desire to have but is below the number of 10. \nEnter the value of how many dice you want to toss here : "))
    # This is checking if the number of dices the user wants to have is higher than 10. If it is, it
    # will print an error message and return a value error.
    if (numberOfDice > 10) :
        print("ERROR! The value you have typed is higher than 10")
        return ValueError
    else :
        # This is asking the user to input the number of faces they want on their dices.
        print("You have", numberOfDice, "dices in your hand.")
        facesOfDice = int(input("Please enter the number of faces you want on your dices, please enter a value below or equal to 6 here : "))
        if facesOfDice <= 6:
            print("You have", facesOfDice, "faces on your dice(s).")
            possibilities = facesOfDice ** numberOfDice # Doing the calculation of how many possibilities there are for the number of dices and faces the user has.
            print("For the number of dice you have and faces you gace, there are ", possibilities)
            wantedValue = int(input("Please enter the number you want to calculate the numbber of possibilities you have for x amount of dice and faces here : ")) # This is asking the user to input the number they want to calculate the number of possibilities for.
            listeOfAllFaces = []
            for i in range(1,facesOfDice+1):
                listeOfAllFaces.append(i) # This is creating a list of all the possible faces that can be on the dices.

            numberOfPossibilities = 0

            # This is checking if the number the user wants to calculate the number of possibilities
            # for is higher than the number of dices and faces the user has. If it is, it will return
            # a value error.
            if wantedValue >= numberOfDice*facesOfDice:
                return False, print("False")

            # This is creating a list of all the possible combinations of the faces on the dices.
            for i in product(listeOfAllFaces,repeat=numberOfDice):
                if sum(i) == wantedValue:
                    # This is adding 1 to the numberOfPossibilities everytime the sum of the dices is
                    # equal to the number the user wants to calculate the number of possibilities for.
                    numberOfPossibilities+=1

            print ("The number of possibilities are : ", numberOfPossibilities)
        else: 
            print("ERROR! The value you have typed is higher than 6")
            return ValueError

main()

    