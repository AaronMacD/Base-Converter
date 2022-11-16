# -*- coding: utf-8 -*-
"""
Base Conversion
MTH 225
Aaron MacDougall
version 9/29/22
"""

    
#I could just convert it using built in features, but doing the math demonstrates my knowledge...
#Has to be able to convert numbers over the base to the letter. Works fine as is for binary, but doesn't work for bases above 10 since we need letters to fill in after 0-9.

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def convertFromDecimalBelowBase10(base, num):
    result = ""
    while num != 0:
        result = str((num%base)) + result
        num = num//base
    return result

def convertFromDecimalAboveBase10(base, num):
    result = ""

    while num != 0:
        extraDigit = num%base
        if extraDigit > 9:
            extraDigit = LETTERS[extraDigit-10]
        result = str(extraDigit) + result
        num = num//base
    return result

    
#def convertToDecimal(base, num):
    
    

def main():
    quit = False
    while quit == False:
        #Positive only for now, but once you learn 2's complement, do negatives as well!  
        number = input("Please enter your positive decimal integer to be converted: ")
        newBase = input("Please input the new base of this number: ")
        try:
            newBase = int(newBase)
            number = int(number)
        except:
            print("Invalid entry. Please only enter a number.")
            continue
        if number < 0 or newBase < 2:
            print("Invalid entry. You must enter a positive integers.")
            continue
        
        if newBase < 10:
            result = convertFromDecimalBelowBase10(newBase, number)
        if newBase > 10:
            result = convertFromDecimalAboveBase10(newBase, number)
        print("Here are the results of your conversion!")
        print(str(number) + " in base 10 is equal to " + result + " in base " + str(newBase) + ".")
        
        endResult = input("Do you wish to play again? (y/n)")
        if endResult == "n" or endResult == "N":
            quit = True
            
        
        

    
    
    
if __name__=='__main__':
    main()