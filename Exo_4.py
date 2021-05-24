
def main():
    numberOfDice = int(input("To play the game, Please enter x number of dice(s) you desire to have but is below the number of 10. \nEnter the value of how many dice you want to toss here : "))
    if (numberOfDice > 10) :
        print("ERROR! The value you have typed is higher than 10")
        return ValueError
    else :
        print("You have", numberOfDice, "dices in your hand.")
        facesOfDice = int(input("Please enter the number of faces you want on your dice, please enter a value below or equal to 6 here : "))
        if facesOfDice <= 6:
            print("You have", facesOfDice, "faces on your dice(s).")
            possibilities = facesOfDice ** numberOfDice
            print("For the number of dice you have and faces you gace, there are ", possibilities)
            int(input("Please enter the number you want to calculate the numbber of possibilities you have for x amount of dice and faces here : "))
            '''waysToGetValue = (numberOfDice + possibilities - 1) / (numberOfDice * (possibilities - 1))
            print(waysToGetValue) Not the right equation'''
        else: 
            print("ERROR! The value you have typed is higher than 6")
            return ValueError

main()