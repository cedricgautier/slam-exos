
def main ():
    
    """
    The function takes an integer as an input and returns a list of all prime numbers between 0 and the
    inputted number.
    """
    entry = int(input("Enter the number you want here : "))
    prime = False #prime is defined as false and will change if entry number is a prime number. 
    
    if entry > 1 : 
        for numbers in range(2, entry):
            if (entry % numbers) == 0: # Check if entry number has a factor
                prime = True
                break

    if prime :
        print(entry, 'is not prime number!')
    else : 
        print(entry, 'is a prime number')
        start = 0
        finish = entry

        print("All prime numbers between the 0 and the enterded value are : ")
        for entry in range(start, finish + 1):
            # all prime numbers are greater than 1
            if entry > 1:
                for numbers in range(2, entry):
                    if (entry % numbers) == 0:
                        break
                else:
                    print(entry)

main()
