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