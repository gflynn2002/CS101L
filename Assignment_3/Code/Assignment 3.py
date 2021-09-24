########################################################################
##
## CS 101 Lab
## Program #3
## Gabriel Flynn
## gflynn2002@gmail.com
##
## Find number when given remainder when divided by 3, 5, and 7
##
## ALGORITHM : 
##      First print intro, set playagain to y, while playagain is y repeat all of this. Get rem3 as an integer input, and test to make sure it is between 0 and 2. Get rem5 and rem7, and check to make sure they aren't the same
##      Then test for everything between 1 to 101 if their modulo(%) or remainder is equal to rem3, rem5, and rem7 respectively. Once it finds a number that satisfies all equations print it to tell user their number was found.
##      Then ask if the user wants to play again putting in y or Y repeats code, n or N ends it.
## 
## ERROR HANDLING:
##      No known Errors
##
## OTHER COMMENTS:
##      None
##
########################################################################

#Intro and set play
print(
    '~Welcome User! To The GREAT Flarsheim Number Guesser!!!\n'
    'Please choose a number from 1 to 100 in your head\n'
    'Once you have your number I\'m going to need you to answer a few simple questions\n')
playagain = 'y'
while playagain == 'y' or playagain == 'Y':
    rem3 = int(input('What is the remainder of your number when divided by 3?\n'))
    #Test if remainder of 3 is valid(must be 0, 1, 2)
    while rem3 != 0 and rem3 != 1 and rem3 !=2:
        if rem3 < 0:
            print('Enter value greater than 0')
        elif rem3 >= 3:
            print('Enter value less than 3')
        else:
            print('Error:  Unexpected Value')
        print('\nPlease enter a valid number')
        rem3 = int(input('What is the remainder of your number divided by 3?\n'))
    rem5 = int(input('What is the remainder of your number when divided by 5?\n'))
    rem7 = int(input('What is the remainder of your number when divided by 7?\n'))
    #Test to make sure remainder of 5 and 7 are different
    while rem5 == rem7:
        print('\nError remainder of 5 and remainder of 7 must be different.')
        rem5 = int(input('Please re-enter remainder when divided by 5.'))
        rem7 = int(input('Please re-enter remainder when divided by 7.'))
    #Tests for all numbers 1-100
    for i in range (1, 101):
        r3 = False
        r5 = False
        r7 = False
        if i % 3 == rem3:
            r3 = True
        if i % 5 == rem5:
            r5 = True
        if i % 7 == rem7:
            r7 = True
        while r3 and r5 and r7:
            print('Your number is', i)
            print('Pretty cool right?')
            break
    while 1 > 0:
        #Restarts or ends game
        playagain = input('Do you wish to play again?(y/n)')
        if playagain == 'y' or playagain == 'Y' or playagain == 'n' or playagain == 'N':
            break