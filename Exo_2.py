def valide (characters):
    """
    The function valide takes a string as an argument and returns True if the string contains only
    characters from the list charactersAccepted
    
    :param characters: a string of characters to be validated
    :return: a boolean value.
    """
    for c in characters:
        if (not(c in charactersAccepted)): 
            return False
    return True

def saisie (characters):
    """
    The function takes a string as an argument and returns the string if it is valid. Otherwise, it
    returns an error message
    
    :param characters: The string you want to test
    :return: The characters that the user entered.
    """
    if valide(characters):
        return characters
    return "Your characters invalid"

def proportion():
    chain = input("Enter the chain you want :")
    sequences =input('Set you the sequence you want here :')
    nbSeq =  chain.count(sequences)
    pourcentage = ((nbSeq *len(sequences)/ len(chain)) * 100)
    print("Chaîne : ", chain)
    print("Séquences :", sequences)
    print (f"Il y a", pourcentage,  "% de", '"',sequences,'"', "dans votre chaîne")
 
#MAIN 
charactersAccepted = "aAcCgGtT"
entry = input(
    "Enter 'Valide' or 'Saisie' or 'Proportion' to choose a function. \nWrite here : ")

if entry == 'Valide':
    characters = input("Enter any alphabetical character here :")
    print(valide(characters))

elif entry == 'Saisie':
    characters = input("Enter any alphabetical character here :")
    print(saisie(characters))
    
elif entry == 'Proportion':
    proportion()