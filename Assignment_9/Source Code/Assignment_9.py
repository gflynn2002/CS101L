########################################################################
##
## CS 101 Lab
## Program #9
## Gabriel Flynn
## gflynn2002@gmail.com
##
## Create a program to search and specify crime in the crime database csv files.
##
## ALGORITHM : 
##      Define all of the functions first(Number to month, convert file to list, and then the appropriate search functions. Then ask user for file name, date, offense, and zipcode to print out respective data.)
## 
## ERROR HANDLING:
##      Sometimes functions don't get called properly, can't find what causes it to skip.
##
## OTHER COMMENTS:
##      None
##
########################################################################

def month_from_number(num):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    num -= 1
    return months[num]

def read_in_file(file):
    #From AMC on stackoverflow.com
    import csv
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

def create_reported_date_dic(date, file):
    with open(file, 'r') as f:
        import csv
        reader = csv.reader(f)
    # skip header row
        l1 =[]
        for row in reader:
            if str(row[1]) == date:
                l1.append(row)
    return l1
                

def create_reported_month_dic(date, file):
    with open(file, 'r') as f:
        import csv
        reader = csv.reader(f)
        date = date + '/'
    # skip header row
        l1 =[]
        for row in reader:
            if str(row[1]) == any(row.startswith(date)):
                l1.append(row)
    return l1

def create_offense_dic(offense, file):
    with open(file, 'r') as f:
        import csv
        reader = csv.reader(f)
    # skip header row
        l1 =[]
        for row in reader:
            if str(row[6]) == offense:
                l1.append(row)
    return l1

def create_offense_by_zip(offense, zip, file):
    with open(file, 'r') as f:
        import csv
        reader = csv.reader(f)
    # skip header row
        l1 =[]
        for row in reader:
            if str(row[6]) == offense and str(row[12]) == zip:
                l1.append(row)
    return l1

flag1 = True

while flag1 == True:
    file = input('\nPlease enter the exact file name ==> ')
    #Try function from linuxize.com
    try:
        f = open(file)
    except IOError:
        print('File not found')
    finally:
        flag1 = False
        f.close()
date = input('\nPlease enter the date to search ==>  ')
print(create_reported_date_dic(date, file))
offense = input('\nPlease enter an offense ==>  ')
zip = input('\nPlease enter a zip code ==>  ')
offense = 'Embezzlement'
zip = '64112'
file = 'CrimeDataSmall.csv'

print(create_offense_by_zip(offense, zip, file))