#!/usr/bin/env python3
################################################################################
# This file contains a function used to test the LN_1_examples file.             #
################################################################################

# imports all the variables from LN_1_examples
from LN_1_examples import *

def run_tests():
    """ Prints the results of checking the examples from LN_examples.py

    tests(None) -> None
    """
    sub_test()
    <test sub-functions>


#----------------------------------- Tests ------------------------------------#

def sub_test():
    ''' Testing sub thing. '''
    
    print('Sub thing test: sub thing specific')
    invalid_int = 'Please define an integer called "my_int".'
    #Relevant comments
    <test code>
    print()


#------------------------------ Helper Functions ------------------------------#

def helper(var):
    ''' Returns something useful. '''
    <code>
    return useful_value


#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    # Aspect 1 Test

    <predefined example variables and code 1>

    # Solution
    <solution code 1>
    

    # Aspect 2 Test

    <predefined example variables and code 2>

    # Solution
    <solution code 2>


    ...

    
    # Aspect N Test

    <predefined example variables and code N>

    # Solution
    <solution code N>


    # Run tests

    run_tests()
