"""___info___"""

d = dict({'file' : 'passGen.py',
          'creator' : 'Matthew McLaren',
          'published' : '01/09/2021',
          'status' : 'public',
          'language' : 'python',
        })

for key in d.keys():
    print(key, ':', d[key])

print('')

"""___package___"""

# random.py
import random

"""___body___"""

def printLine(phrase, width):
    """
        This formats print statements to make everything flow easier on the console.
    """
    # this will be the new string
    fixed = ''

    # checks if the phrase needs to be changed
    if len(phrase.rsplit(' ')) > width - 1:
        # this is to help merge the new phrase
        wcount = 0
        line = 1
        
        # this begins inserting the newline characters
        for word in phrase.rsplit(' '):
            # if the word is the very first thing in the phrase
            if wcount == 0 and line == 1:
                # starts the string off with one word
                fixed += word

                # adds an itteration for count
                wcount += 1    
            # if the word fits in the segment
            elif wcount <= width - 1:
                # adds the word to the string
                fixed += ' ' + word

                # adds an itteration for count
                wcount += 1
                
            # if the word doesn't fit
            else:
                # adds newline character
                fixed += '\n' + word

                # resets count
                wcount = 1

                # adds a line
                line += 1

        # this returns the new string
        return print(fixed)
    # if the phrase does not need to be fixed
    else:
        # returns the stated phrase
        return print(phrase)

def checkCriteria(criteria, failed = False):
    """
        This function is an input exclusive function that returns a True or False
    """
    if failed == False:
        # gathers the input from the user
        resp = input('Would you like ' + criteria + ' to be enabled: ').lower()

        # returns the necessary end result until specifications are met
        if resp == 'yes' or resp == 'y':
            return True
        elif resp == 'no' or resp == 'n':
            return False
        else:
            return checkCriteria(criteria, True)
    else:
        # gathers the input from the user
        resp = input('Please put only yes/y or no/n: ').lower()

        # returns the necessary end result until specifications are met
        if resp == 'yes' or resp == 'y':
            return True
        elif resp == 'no' or resp == 'n':
            return False
        else:
            return checkCriteria(criteria, True)

def makePass(length = None):
    """
        This function actually makes the password.
    """
    # these grab t/f for the criteria
    lc = checkCriteria('lowercase characters')
    uc = checkCriteria('uppercase characters')
    nc = checkCriteria('number Characters')
    sc = checkCriteria('special characters')

    # this makes sure the password has something to be built with
    if lc == uc == nc == sc == False:
        print('\nMake sure your password includes characters, try again.\n')
        return makePass(length)
    
    # these are the building blocks for the password
    blocks = ''

    # this runs through what the person wants
    if lc == True:
        blocks += 'abcdefghijklmnopqrstuvwxyz'
    if uc == True:
        blocks += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if nc == True:
        blocks += '0123456789'
    if sc == True:
        blocks += '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

    # tracks the length of the password
    track = 0
    while track < length:
        print()
    
makePass()


def main():
    """
        This is the function used for putting everything together
    """
    # introduction to the code for the user
    printLine('\nHello, you are using this because you need a new password. Good choice! Please answer these questions and a password will be provided.\n', 14)
    
    # code starts here

"""___initiate___"""

# for the final process don't mess with this
#main()
