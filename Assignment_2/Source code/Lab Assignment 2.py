########################################################################
##
## CS 101 Lab
## Lab Grade Calculator
## Gabriel Flynn
## gflynn2002@gmail.com
##
## Create a program that takes grades from exams, labs, and attendance and weights them.
##  
## ERROR HANDLING:
##      No errors found.
##
## OTHER COMMENTS:
##      No other comments.
##
########################################################################


print('**** Welcome to the LAB grade calculator! ****')
name = input('Who are we calculating grades for? ==>')
lgrade = int(input('Enter the Labs grade? ==>'))

'''Testing if between 0 and 100 below each variable'''

if lgrade > 100:
    print('The lab value should have been 100 or less. It has been changed to 100')
    lgrade = 100
elif lgrade < 0:
    print('The lab value should have been zero or greater. It has been changed to zero.')
    lgrade = 0

egrade = int(input('Enter the EXAMS grade? ==>'))

if egrade > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
    egrade = 100
elif egrade < 0:
    print('The exam value should have been zero or greater. It has been changed to zero.')
    egrade = 0

agrade = int(input('Enter the Attendence grade? ==>'))

if agrade > 100:
    print('The attendence value should have been 100 or less. It has been changed to 100.')
    agrade = 100
elif agrade < 0:
    print('The attendence value should have been zero or greater. It has been changed to zero.')
    agrade = 0


'''This sets the weighted grade and tests to find what letter grade to set'''
wgrade = ((lgrade * 0.7) + (egrade * 0.2) + (agrade * 0.1))
if wgrade > 90:
    letter = 'A'
elif wgrade > 80:
    letter = 'B'
elif wgrade > 70:
    letter = 'C'
elif wgrade > 60:
    letter = 'D'
else:
    letter = 'F'

print('The weighted grade for', name, 'is', wgrade)
print(name, 'has a letter grade of', letter)
print('**** Thanks for using the Lab grade calculator ****')