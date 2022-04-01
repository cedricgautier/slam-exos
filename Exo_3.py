def int_to_rome(x):
    """
    This function converts a decimal number to a roman number
    
    :param x: the number you want to convert to roman numerals
    :return: the roman number.
    """
    # Creating a list of numbers that will be used to convert the decimal number to roman number.
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    # Creating a list of roman numbers.
    roman = ['I','IV','V','IX', 'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
    # Making sure that the loop will stop when the value of i is less than 0.
    i = 12 
    roman_numeral = ''
    if x > 3999:
            return False
    # Checking if the value of the number is less than or equal to the value of x.
    while x != 0:
        # Checking if the value of the number is less than or equal to the value of x.
        if numbers[i] <= x:    
            # Adding the roman number to the roman_numeral variable.
            roman_numeral += roman[i] 
            # Subtracting the value of the number from the value of x.
            x = x - numbers[i]
        # Making sure that the loop will stop when the value of i is less than 0.
        else:
            i -= 1 # i = i - 1
    return roman_numeral 

print("Your decimal in Roman : ", int_to_rome(int(input("Enter the value you want to convert here : "))))