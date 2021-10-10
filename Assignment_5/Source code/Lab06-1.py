########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


import string


def character_value(char : str) -> int:
    number = [ord(letter) - 96 for letter in char]
    return number
    

def get_check_digit(idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    x = 0
    id_sum = 0
    while x < 11:
        id_sum = id_sum + (idnumber[x] * (x + 1))
    check_digit = id_sum % 10
    return check_digit
        

def is_valid(idnumber : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''
    error1 = ' '
    error2 = ' '
    error3 = ' '
    error4 = ' '
    error5 = ' '
    if len(idnumber) != 10:
        result1 = False
        error1 = 'Must be 10 characters long '
    else:
        result1 = True
        test = idnumber[0 : 4]
        result2 = test.isalpha()
        if test.isalpha == False:
            error2 = 'First 5 characters must be letters '
        x = idnumber[5]
        x = int(x)
        if x > 3 or x < 1:
            result3 = False
            error3 = '6th character must be 1-3 '
        else:
            result3 = True
        y = idnumber[6]
        y = int(y)
        if y > 4 or y < 1:
            result4 = False
            error4 = '7th character must be 1-4 '
        else:
            result4 = True
        test2 = idnumber[7 : 9]
        result5 = test2.isnumeric()
        if result5 == False:
            error5 = 'Last 3 characters must be numbers'
    if result1 == False or result2 == False or result3 == False or result4 == False or result5 == False:
        result = False
    else:
        result = True
    error = ''.join((error1, error2, error3, error4, error5))
    return result, error

def get_school(idnumber : str) -> str:
    z1 = idnumber[5]
    z1 = int(z1)
    if z1 == 1:
        return 'School of Computing and Engineering SCE'
    elif z1 == 2:
        return 'School of Law'
    elif z1 == 3:
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'
  

def get_grade(idnumber : str) -> str:
    z2 = idnumber[6]
    z2 = int(z2)
    if z2 == 1:
        return 'Freshman'
    elif z2 == 2:
        return 'Sophmore'
    elif z2 == 3:
        return 'Junior'
    elif z2 == 4:
        return 'Senior'
    else:
        return 'Invalid Grade'
   

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = is_valid(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        