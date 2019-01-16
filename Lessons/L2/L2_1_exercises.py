#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following exercises below the appropriate   #
# comment, and click run when complete, using either the menu-bar at the top,  #
# or the F5 key on your keyboard.                                              #
################################################################################

# Which one is bigger?
'''
    Write an 'if-else' block to check which of the two specified values is
    larger, and set the variable 'larger' to the larger value, and 'smaller' to
    the smaller value. You may assume that the values are not equal.

    NOTE: different variable types, including strings, have the 'less than' (<)
    and 'greater than' (>) operators defined.
'''

# setup code
val_1 = 'text'
val_2 = 'text2'
larger = ''
smaller = ''

# <your code here>




# Well that's odd...
'''
    The following import statement allows for the generation of random integers.
    Using a couple of if-else blocks, place 'rand_1' and 'rand_2' into the
    appropriate list(s).

    NOTE: variables can be added to a list using the += operator, as:
        list_name += [variable]
'''
# setup code
from random import randint

rand_1 = randint(1, 101)
rand_2 = randint(1, 101)
even = []
odd = []

# <your code here>




# Programmer's Diagnosis
'''
    The final example involves determining several properties of a new random
    value. Set the following variables to conditional values which determine
    if 'rand_3' has their namesake properties. The first one has been done for
    you as an example.

    Consider positive as 0 or above, and negative as below 0.
'''

rand_3 = randint(-100, 100)

equals_0 = (rand_3 == 0) # this one is done
# change these ones to conditional statements
multiple_of_3 = False
multiple_of_7 = False
positive = False
negative = False
between_0_and_15_inclusive = False




'''
    When you're done, click Run or F5 to check that you've followed the
    instructions. It is suggested to run the tests a few times to ensure
    passing all tests wasn't by luck. Example solutions can be found at the
    bottom of the exercise checker file.

    The code below isn't for editing, it's used to run the test file when this
    program is run.
'''

if __name__ == '__main__':
    from L2_2_exercise_checker import L2Tests
    L2Tests = L2Tests()
    # run the tests (with feedback)
    L2Tests.run_tests(verbose=True)
