########################################################################
##
## CS 101 Lab
## Program #5
## Gabriel Flynn
## gflynn2002@gmail.com
##
## PROBLEM : In this program you are going to simulate a slot machine in Pierson Hall.  
## The slot machine has 3 reels and each reel will have numbers ranging from 1 to 10. 
## The user can choose how many chips they start out with.  They are allowed to wager
## between 1 to the amount of bank they currently have on each spin.  If they match 3 numbers,
## they will win 10 times their wager.  If they match 2 numbers they will win 3 times their wager.
##
## ALGORITHM : 
##      First import random, then define the function play_again() which is a boolean function.
##      For that set the flag to 0, while it is 0 ask if player wants to play again. Set play input
##      to lowercase with .lower(). If their lowered input is yes or y return True, if it is n or no
##      return false. In both cases set flag to 1.
##      Next define get_wager which takes the variable bank into account. It also has the same flag
##      system as before. If they user enters a value greater than their bank or less than 0 ask them
##      to enter it again. If they pass that set the flag to 1 and return the wager.
##      Next define get_slot_results. This will use a tuple. Create a variable for 3 reels. Each reel will = random.randint(1, 10)
##      This returns a random number between 1-10. Then name the tuple and give it the 3 reels for values. Then return the values.
##      Next define get_matches, which uses 3 new variables that take the reels into account(but under different names.)
##      If they are all = return 3. If 2 are = return 2 if none are return 0.
##      Next define get_bank. Set bank to -1, then while bank is < 1 or > 100 ask what the user wants to start with. If they don't
##      enter a value between 1 and 100 then ask them to do so.
##      Next define get_payout. If matches are 3 return wager * 10, if it's 2 return wager * 3 and if it's 0 return wager * -1
##      Use if __name__ == "__main__": Set playing to True(for first loop). Then while playing is True set bank = get_bank()
##      orig_amnt = bank top = bank and spins = 0. These will set the output for when the user loses. The while bank > 0
##      Set wager to get_wager(bank), set reel1, reel2, and reel 3 to get_slot_results(). Set matches to get_matches(reel1, reel2, reel3)
##      and set payout to get_payout(wager, matches). That is the core of the game. Everytime it loops this set bank to bank + payout.
##      Next print 'Your spin' then the 3 reels. Print 'You matched' then matches, 'reels', then 'you won/lost' their payout amount here
##      Then print 'Current bank' and of course their bank value. And to space it nicely print a blank line.
##      Do spins = spins + 1 to set up that value for the lose state, and if bank > than top set top to bank, for the same reason as spins.
##      When they run out it will print 'You lost all', orig_amnt, 'in', spins, 'spins' Then print 'The most chips you had was', top.
##      This all uses the setup to give them their losing screen. Then set playing to call function play_again() and your done.
## 
## ERROR HANDLING:
##      No error handling needed if player enters invalid value then it just asks again.
##
## OTHER COMMENTS:
##      None
##
########################################################################

import random

def play_again() -> bool:
    flag = 0
    while flag == 0:
        playing = input('Do you want to play again?')
        playing = playing.lower()
        if playing == 'yes' or playing == 'y':
            flag = 1
            return True
        if playing == 'no' or playing == 'n':
            flag = 1
            return False
     
def get_wager(bank : int) -> int:
    flag = 0
    while flag == 0:
        wager = int(input('How much do you want to wager?'))
        if wager <= bank and bank > 0:
            flag == 1
            return wager
        else:
            print('Enter a valid amount')

def get_slot_results() -> tuple:
    reel1 = random.randint(1, 10)
    reel2 = random.randint(1, 10)
    reel3 = random.randint(1, 10)
    tuple = (reel1, reel2, reel3)

    return tuple

def get_matches(reela, reelb, reelc) -> int:
    if (reela and reelb == reelc):
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0

def get_bank() -> int:
    bank = -1
    while bank < 1 or bank > 100:
        bank = int(input('How many chips would you like to start with(must be between 1 and 100.)'))
        if bank < 1 or bank > 100:
            print('Please enter a valid balance.')
    return bank

def get_payout(wager, matches):
    if matches == 3:
        return int(wager) * 10
    elif matches == 2:
        return int(wager) * 3
    elif matches == 0:
        return int(wager) * -1     


if __name__ == "__main__":

    playing = True
    while playing == True:

        bank = get_bank()
        orig_amnt = bank
        top = bank
        spins = 0

        while bank > 0:
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spins = spins + 1
            if bank > top:
                top = bank
           
        print("You lost all", orig_amnt, "in", spins, "spins")
        print("The most chips you had was", top)
        playing = play_again()