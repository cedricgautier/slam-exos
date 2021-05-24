#Recursive

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
            
            def Resolution(facesOfDice,numberOfDice, wantedValue):
                table=[[0]*(wantedValue+1) for i in range(numberOfDice+1)] #Initialize all entries as 0
            
                for j in range(1,min(facesOfDice+1,wantedValue+1)): #Table entries for only one dice
                    table[1][j]=1
                        
                    # Fill rest of the entries in table using recursive relation
                    # i: number of dice, j: sum
                for i in range(2,numberOfDice+1):
                    for j in range(1,wantedValue+1):
                        for k in range(1,min(facesOfDice+1,j)):
                            table[i][j]+=table[i-1][j-k]
                    
                return table[-1][-1]
            print(Resolution(facesOfDice,numberOfDice,wantedValue))

main()