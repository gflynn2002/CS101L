########################################################################
##
## CS 101 Lab
## Program #6
## Gabriel Flynn
## gflynn2002@gmail.com
##
## PROBLEM : The Caesar Cipher is an encryption/decryption method that shifts the alphabet.  
##           For instance, if you have a cipher that shifts by 1, A would become B, B would become C, Z would wrap and become A.  
##           To decrypt that cipher you simply shift by -1.  It is a very simple cipher that is easily broken.
##
## ALGORITHM : 
##      First set the encryption function. It shifts uppercase and lower case letters by the key entered it does this for respective cases
##      Second set the decription function. It does the same as the encryption function just in reverse.
##      Then make the menu option that runs on a while loop till the user enters Q or q(by setting this option to the run value)
##      Option 1 prompts the user to enter text and a key for encryption and 2 does the same for decryption.
## 
## ERROR HANDLING:
##      No error handling needed
##
## OTHER COMMENTS:
##      None
##
########################################################################

#Encrypt
def encrypt(plain_text, key):
    encrypted = ''
    for c in plain_text:
        #Works for upper and lower simply shifts them in their proper case
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower():
            c_index = ord(c) - ord('a') 
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
    return encrypted

#Decrypt
def decrypt(ciphertext, key):
    decrypted = ''
    for c in ciphertext:
        #works for upper or lower simply shifts them in their proper case
        if c.isupper(): 
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower(): 
            c_index = ord(c) - ord('a') 
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
    return decrypted
#Simplified version of code written by Mokhtar Ebrahim


#Starts program
run = 'y'

#The user interface so long as they don't enter Q or q it won't stop
while run != 'q':
    option = input('\nPlease pick an option or press Q to quit\n1) Encode a message\n2) Decode a message: \n')
    if option == '1':
        #This is encryption
        text = input('\nPlease enter what you would like to encrypt: ')
        num = int(input('\nPlease enter a key: '))
        #Makes sure that the key is valid
        while num > 25 or num < 1:
            num = int(input('\nPlease enter a valid key(must be between 1 and 25: '))
        print(encrypt(text, num))
        optopn = 'out'
    #This is decryption
    elif option == '2':
        text2 = input('\nPlease enter what you would like to decrypt: ')
        num2 = int(input('\nPlease enter the key: '))
        #Makes sure that the key is valid
        while num2 > 25 or num2 < 1:
            num2 = int(input('\nPlease enter a valid key(must be between 1 and 25): '))
        print(decrypt(text2, num2))
        option = 'out'
    #And this is the quit option
    elif option == 'q' or option == 'Q':
        run = 'q'