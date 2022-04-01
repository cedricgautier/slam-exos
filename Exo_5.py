#Recursive

def main():
    # Asking the user to input the number of dice they want to play with.
    numberOfDice = int(input("To play the game, Please enter x number of dice(s) you desire to have but is below the number of 10. \nEnter the value of how many dice you want to toss here : "))
    # Checking if the user has inputted a number of dice that is higher than 10. If the user has inputted a number higher than 10, it will print an error message and return a ValueError.
    if (numberOfDice > 10) :
        print("ERROR! The value you have typed is higher than 10")
        return ValueError
    else :
        print("You have", numberOfDice, "dices in your hand.")
        facesOfDice = int(input("Please enter the number of faces you want on your dices, please enter a value below or equal to 6 here : "))
        # Asking the user to input the number of faces they want on their dice. If the user inputs a number higher than 6, it will print an error message and return a ValueError.
        if facesOfDice <= 6:
            print("You have", facesOfDice, "faces on your dice(s).")
            possibilities = facesOfDice ** numberOfDice
            print("For the number of dice you have and faces you gace, there are ", possibilities)
            wantedValue = int(input("Please enter the number you want to calculate the numbber of possibilities you have for x amount of dice and faces here : "))
            
            def Resolution(facesOfDice,numberOfDice, wantedValue):
                # Initializing a table with the number of rows equal to the number of dice and the
                # number of columns equal to the wanted value.
                table=[[0]*(wantedValue+1) for i in range(numberOfDice+1)] #Initialize all entries as 0
            
                # This is a for loop that is going through the range of the number of faces of the
                # dice and the wanted value.
                for j in range(1,min(facesOfDice+1,wantedValue+1)): #Table entries for only one dice
                    table[1][j]=1
                        
                # Looping through the range of the number of dice and the wanted value.
                for i in range(2,numberOfDice+1):
                    for j in range(1,wantedValue+1):
                        for k in range(1,min(facesOfDice+1,j)):
                            table[i][j]+=table[i-1][j-k]
                    
                # Returning the last value of the table.
                return table[-1][-1]
            # Printing the number of possibilities for the number of dice and faces the user has inputted.
            print(Resolution(facesOfDice,numberOfDice,wantedValue))

main()