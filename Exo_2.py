def valide (characters):
    characters = input("Enter any alphabetical character here :")
    for c in characters:
        if (not(c in charactersAccepted)): 
            return False
    return True

def saisie ():
    characters = input("Enter any alphabetical character here :")
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
    print(valide())

elif entry == 'Saisie':
    print(saisie())
    
elif entry == 'Proportion':
    proportion()
