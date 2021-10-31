########################################################################
##
## CS 101 Lab
## Program #8
## Gabriel Flynn
## gflynn2002@gmail.com
##
## We’re going to work on something that is important to all students, grade weighting.  Our program will allow the user to enter 2 types of grades; Tests and Programs.  
## Each of our scores is assumed to be out of 100, so we only need the users score.  The tests are 60% of a student’sgrade, while the assignments are 40%.  In order to calculate the final score,
## we multiply the mean score of the tests by 0.6 and add it to the mean of assignments multiplied by 0.4.When we display scores we will also show them the low, high, mean, and standard deviation 
## of their tests and assignments.The mean is the average.  To calculate the mean you would sum all the values and divide by the number of values.  If the values we want a mean for are 5, 8, 4, 9 
## then the mean is𝑚𝑒𝑎𝑛=(5+8+4+ 9) / 4In this case our mean is 6.5The standard deviation is calculated by taking each value and subtracting the mean, and squaring the value.  Divide the sum of
## those values by the numbers of values, and take the square root of that result.  Using the example above
##
## ALGORITHM : 
##      First import math and statistcs, then setup all lists flags and variables, set a loop to work while run = True, that keeps everything going. Print the menu. For 1 append tests and mtests with the imput,
##      do the same for 4 but with assignments. For 2 remove a specific number from tests and mtests, same for 5 but with assignments. For 3 clear tests and mtests as well as reseting variables, for 6 do the same but for assignments.
##      For D print out the table displaying tests with the amount, min, max, average, and standard deviation, do the same for assignments, and the weighted score below it.
## 
## ERROR HANDLING:
##      No known Errors
##
## OTHER COMMENTS:
##      None
##
########################################################################

#math and statistics for standard deviation
import math
import statistics


#Keeps menu looped and running
run = True
run2 = True

tests = []
mtests = []
assignments = []
massignments = []

#Tests to make sure list as something
flag1 = 0
flag2 = 0

#Initial Flags
wscore = 'n/a'
amin = 'n/a'
amax = 'n/a'
aavg = 'n/a'
anum = 0
tmin = 'n/a'
tmax = 'n/a'
tavg = 'n/a'
tstd = 'n/a'
astd = 'n/a'
tnum = 0


while run == True:
    run2 = True
    opt = input('\tGrade Menu\n1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit\n\n==> ')
    if opt == '1':
        run2 == True
        while run2 == True:
            add = int(input('\nEnter the new test score 0-100 ==> '))
            add2 = str(add)
            if 0 <= add <= 100:
                print('\nAccepted')
                tests.append(add)
                mtests.append(add2)
                run2 = False
                flag1 = 1
                tnum += 1
            else:
                print('\nPlease enter a number between 0 and 100', add, 'is not a valid grade.')
    elif opt == '2':
        run2 == True
        while run2 == True:
            add = int(input('\nEnter the score to remove 0-100 ==> '))
            add2 = str(add)
            if 0 <= add <= 100:
                print('\nAccepted')
                tests.remove(add)
                mtests.remove(add2)
                run2 = False
            else:
                print('\nPlease enter a number between 0 and 100', add, 'is not a valid grade.')
    elif opt == '3':
        run2 == True
        while run2 == True:
            confirm = input('\nAre you sure you wish to delete all tests? (Y/N) ==> ')
            if confirm == 'y' or confirm == 'Y':
                flag1 = 0
                tests = []
                mtests =[]
                wscore = 'n/a'
                tmin = 'n/a'
                tmax = 'n/a'
                tavg = 'n/a'
                tstd = 'n/a'
                astd = 'n/a'
                tnum = 0
                print('\nAll tests deleted')
                run2 = False
            elif input == 'n' or input == 'N':
                print('\nNot deleted')
                run2 = False
            else:
                print('\nInvalid input please use y or n only.')
    elif opt == '4':
        run2 == True
        while run2 == True:
            add = int(input('\nEnter the new assignment score 0-100 ==> '))
            add2 = str(add)
            if 0 <= add <= 100:
                print('\nAccepted')
                assignments.append(add)
                massignments.append(add2)
                run2 = False
                flag2 = 1
                anum += 1
            else:
                print('\nPlease enter a number between 0 and 100', add, 'is not a valid grade.')
    elif opt == '5':
        run2 == True
        while run2 == True:
            add = int(input('\nEnter the score to remove 0-100 ==> '))
            add2 = str(add)
            if 0 <= add <= 100:
                print('\nAccepted')
                assignments.remove(add)
                massignments.remove(add2)
                run2 = False
            else:
                print('\nPlease enter a number between 0 and 100', add, 'is not a valid grade.')
    elif opt == '6':
        run2 == True
        while run2 == True:
            confirm = input('\nAre you sure you wish to delete all assignments? (Y/N) ==> ')
            if confirm == 'y' or confirm == 'Y':
                flag2 = 0
                assignments = []
                massignments = []
                wscore = 'n/a'
                amin = 'n/a'
                amax = 'n/a'
                aavg = 'n/a'
                anum = 0
                print('\nAll assignments deleted')
                run2 = False
            elif input == 'n' or input == 'N':
                print('\nNot deleted')
                run2 = False
            else:
                print('\nInvalid input please use y or n only.')
    elif opt == 'D' or opt == 'd':
        if flag1 == 1 and flag2 == 1:
            wscore = (((tnum /len(mtests) * 0.6)) + ((anum /len(massignments) *0.4)))
        if flag1 == 1:    
            tmin = min(tests)
            tmax = max(tests)
            tavg = (tnum /len(mtests))
            tstd = statistics.pstdev(tests)
        if flag2 == 1:
            amin = min(assignments)
            amax = max(assignments)
            aavg = (anum /len(massignments))
            astd = statistics.pstdev(assignments)

        print('\nType\t\t#\tmin\tmax\tavg\tstd')
        print('============================================================================')
        print('Tests\t\t{}\t{}\t{}\t{}\t{}'.format(tnum,tmin,tmax,tavg,tstd))
        print('Assignments\t{}\t{}\t{}\t{}\t{}'.format(anum,amin,amax,aavg,astd))
        print('\nThe weighted scores is', wscore)
    elif opt == 'Q' or opt == 'q':
        print('Goodbye')
        break