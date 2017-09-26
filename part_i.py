# pylint: disable=c
# Problem Set 2, Part I
# Name: Lozano,Jolene
# Collaborators:
import math


def is_divisible(x, y):
    if x != 0 and y == 0:
        return False
    elif x == 0 and y == 0:
        return True
    elif x % y == 0:
        return True
    elif x % y != 0:
        return False


#
# is_divisible(0,0)
# is_divisible(1,0)
# is_divisible(4,2)
# is_divisible(2,4)
def main():
    user_input1 = input('Please enter your first number: ')
    user_input2 = input('Please enter your second number: ')
    if is_divisible(user_input1, user_input2) == True:
        if abs(user_input1) == abs(user_input2):
            print 'Both numbers are divisible by each other.'
        else:
            print 'The first number is divisible by the first one.'
    elif is_divisible(user_input2, user_input1) == True:
        print 'The second number is divisible by the second one.'
    elif is_divisible(user_input1, user_input2) == False:
        print 'Neither number is divisible by each other.'


main()
