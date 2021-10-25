########################################################################
##
## CS 101 Lab
## Program #6
## Gabriel Flynn
## gflynn2002@gmail.com
##
## PROBLEM : In this lab we’ll write a program to read through a file containing information about fuel economy and output the results to a file above a threshold that the user gives.
##  If the user wants to see all vehicles with a combined mpg greater than 50, then yourprogram will output that information to the file of their choosing.
##  The information is tab-delimited.  When you read a line from the file, the values are separated by the tab character \t.  
##
## ALGORITHM : 
##      First setup input to ask for file, then open that in 'w' mode. Then create open = 0, set to 0 for every loop(it is used on year, and the mpgs) ask for all sections of
##      the spread sheet. Then use f.write with {} formatting so you can use all variables at once. Then close it.
## 
## ERROR HANDLING:
##      Must use exact text file name.
##
## OTHER COMMENTS:
##      None
##
########################################################################

wrkfile = input('What file would you like to open?')
f = open(wrkfile, 'a')
open = 0
while open == 0:
    year = int(input('What year is the car?'))
    if 1886 <= year:
        open = 1
    else:
        print('Invalid input')
open = 0
make = input('What is the make?')
model = input('What is the model')
cylinders = input('How many cylinders in the vehical?')
tran = input('What type of transmission?')
vclass = input('What is the vehical class?')
displ = input('What is the displacement in liters?')
while open == 0:
    cmpg = int(input('Enter combined MPG\n'))
    if 0 < cmpg < 101:
        open = 1
    else:
        print('Invalid input')
open = 0
while open == 0:
    cimpg = int(input('Enter city MPG\n'))
    if 0 < cimpg < 101:
        open = 1
    else:
        print('Invalid input')
open = 0
while open == 0:
    hmpg = int(input('Enter highway MPG\n'))
    if 0 < hmpg < 101:
        open = 1
    else:
        print('Invalid input')
f.write('\n{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(year, make, model, cylinders, tran, vclass, displ, cmpg, cimpg, hmpg))
f.close()
