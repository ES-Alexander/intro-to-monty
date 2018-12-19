#!/usr/bin/env python3
################################################################################
# This file contains a function used to test the L2_1_examples file.           #
################################################################################

# imports all the variables from L2_1_examples
from L2_1_examples import *

def run_tests():
    """ Prints the results of checking the examples from LN_examples.py

    tests(None) -> None
    """
    larger_smaller_test()
    even_odd_test()
    property_check_test()


#----------------------------------- Tests ------------------------------------#

def larger_smaller_test():
    ''' Performing larger smaller test on val_1 and val_2 '''
    
    print('Larger-Smaller Test: val_1, val_2')

    # Check if the predefined variables exist
    if are_defined(['val_1', 'val_2','smaller','larger']):
        # Check if val_1 and val_2 are the initial values
        if val_1 == 'text' and val_2 == 'text2':
            passed = True
            # Check if smaller is correctly defined
            if smaller == min(val_1, val_2):
                print("Pass: 'smaller' is correctly defined.")
            else:
                passed = False
                print("Fail: 'smaller' is incorrectly defined.")
                
            # Check if larger is correctly defined
            if larger == max(val_1, val_2):
                print("Pass: 'larger' is correctly defined.")
            else:
                passed = False
                print("Fail: 'larger' is incorrectly defined.")

            # Print success state
            if passed:
                print("SUCCESS: both 'smaller' and 'larger' are correctly" +
                      "defined.")
            else:
                print("FAILED: either 'smaller' or 'larger' are " +
                      "incorrectly defined.")
        else:
            print("FAILED: one or more of val_1 and val_2 have been " +
                  "redefined.")
    else:
        print("FAILED: one or more of the initial variables is undefined.")
    print()


def even_odd_test():
    ''' Performing even-odd test on rand_1 and rand_2. '''

    print("Even-Odd Test: rand_1, rand_2")

    # Check definition of initial variables
    if are_defined(['rand_1','rand_2','even','odd']):
        passed = True
        # Check Even correctly defined
        for var in [rand_1, rand_2]:
            if var%2 == 0:
                if var not in even:
                    passed = False
                    print("Fail: " + str(var) + " not in Even list.")
                else:
                    print("Pass: " + str(var) + " in even list, as expected.")
            else:
                if var not in odd:
                    passed = False
                    print("Fail: " + str(var) + "not in odd list.")
                else:
                    print("Pass: " + str(var) + " in odd list, as expected.")

        # print success state
        if passed:
            print("SUCCESS: variables correctly sorted into even and odd " +
                  "lists.")
        else:
            print("FAILED: variables incorrectly sorted. Please review your " +
                  "conditional statements.")
    else:
        print("FAILED: one or more of the initial variables is undefined.")
    print()

def property_check_test():
    ''' Performing property-check test on rand_3. '''

    print("Property Check Test: rand_3")

    # Check definition of initial variables
    if are_defined(['rand_3','divisible_by_3','divisible_by_7','positive',
                    'negative','between_0_and_15_inclusive']):
        passed = True
        # Check divisible by 3
        if (rand_3 % 3 == 0 and divisible_by_3) or \
           (rand_3 % 3 != 0 and not divisible_by_3):
            print('Pass: divisible_by_3 correctly defined.')
        else:
            passed = False
            print("Fail: divisible_by_3 incorrectly defined.")
        # Check divisible by 7
        if (rand_3 % 7 == 0 and divisible_by_7) or \
           (rand_3 % 7 != 0 and not divisible_by_7):
            print('Pass: divisible_by_7 correctly defined.')
        else:
            passed = False
            print("Fail: divisible_by_7 incorrectly defined.")
        # Check positive
        if (rand_3 > 0 and positive) or (rand_3 < 0 and not positive) \
           or rand_3 == 0:
            print("Pass: positive correctly defined.")
        else:
            passed = False
            print("Fail: positive incorrectly defined.", rand_3,
                  "is not positive.")
        # Check negative
        if (rand_3 < 0 and negative) or (rand_3 > 0 and not negative) \
           or rand_3 == 0:
            print("Pass: negative correctly defined.")
        else:
            passed = False
            print("Fail: negative incorrectly defined.", rand_3,
                  "is not negative")
        # Check between 0 and 15
        if (rand_3 >= 0 and rand_3 <= 15 and between_0_and_15_inclusive) \
           or (not between_0_and_15_inclusive and (rand_3 < 0 or rand_3 > 15)):
            print("Pass: between_0_and_15_inclusive correctly defined.")
        else:
            passed = False
            print("Fail: between_0_and_15_inclusive incorrectly defined.")

        # print success state
        if passed:
            print("SUCCESS: all properties are defined as expected.")
        else:
            print("FAILURE: some or all properties are incorrectly defined.")
            
    else:
        print("FAILED: one or more of the initial variables is undefined.")


#------------------------------ Helper Functions ------------------------------#

from .. import helpers
from helpers import is_defined, are_defined


#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    # Larger-Smaller Test

    val_1 = 'text'
    val_2 = 'text2'
    larger = ''
    smaller = ''

    # Solution:
    if val_1 > val_2:
        larger = val_1
        smaller = val_2
    else:
        smaller = val_1
        larger = val_2
        

    # Even-Odd Test

    from random import randint

    rand_1 = randint(1, 101)
    rand_2 = randint(1, 101)
    even = []
    odd = []

    # Solution
    if rand_1 % 2 == 0:
        even += [rand_1]
    else:
        odd += [rand_1]

    if rand_2 %2 == 0:
        even += [rand_2]
    else:
        odd += [rand_2]


    # Property Separation Test

    rand_3 = randint(-100, 100)

    divisible_by_3 = False
    divisible_by_7 = False
    positive = False
    negative = False
    between_0_and_15_inclusive = False

    # Solution
    if rand_3 % 3 == 0:
        divisible_by_3 = True

    if rand_3 % 7 == 0:
        divisible_by_7 = True

    if rand_3 >= 0: # Note that zero can be defined as either positive, negative
                    # or both, since it was left unspecified.
        positive = True
    else:
        negative = True

    if 0 <= rand_3 and rand_3 <= 15:
        between_0_and_15_inclusive = True


    # Run tests

    run_tests()
