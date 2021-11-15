########################################################################
##
## CS 101 Lab
## Top Ten Most Frequent Words
## Gabriel Flynn
## gflynn2002@gmail.com
##
## This program prints the ten most frequent words in a text document
##  
## ERROR HANDLING:
##      No errors found.
##
## OTHER COMMENTS:
##      No other comments.
##
########################################################################

from collections import Counter
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
user_file = open(file, 'r')
words = user_file.read()
user_file.close()
words = words.split(',')
str1 = ''.join(words)
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
for ele in str1:
    if ele in punc:
        str1 = str1.replace(ele, " ")
#punctiation remover from manjeet_04 on geeksforgeeks.org
words = str1.split('\n')
str1 = ''.join(words)
str1 = str1.lower()
words = str1.split(' ')
words2 = [x for x in words if len(x)>3]
c = Counter(words2)
c2 = c.most_common(10)
num = 1
print('# (\'Word\', Frequency)')
print('=======================')
for i in c2:
    print(num, i)
    num += 1
unique = []
for word in words2:
    if word not in unique:
        unique.append(word)
amnt_unique = len(unique)
print('There are {} words that only appear once'.format(amnt_unique))
#Instructions say to print number of unique words and number of words that only appear once. To me that means the same thing, it's to late to email so we're hoping this is an error.