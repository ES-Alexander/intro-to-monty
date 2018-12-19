#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following examples below the appropriate    #
# comment, and click run when complete, using either the menu-bar at the top,  #
# or the F5 key on your keyboard.                                              #
################################################################################

# Write an if block to check which of the two specified values is larger, and
# set variable 'larger' to the larger value, and 'smaller' to the smaller value.
# Assume that the values are not equal.

# NOTE: different variable types, including strings, have < and > defined

val_1 = 'text'
val_2 = 'text2'
larger = ''
smaller = ''

# <your code here>


# The following import statement allows for the generation of random integers.
# Using an if block, sort the values below into lists 'even' and 'odd'.

# NOTE: there are multiple methods for determining if a number is even or odd,
#   one of which is facilitated using the type function described in L1.

# NOTE 2: variables can be added to a list by using the += operator, as
# list_name += [variable]

from random import randint

rand_1 = randint(1, 101)
rand_2 = randint(1, 101)
even = []
odd = []

# <your code here>


# The final example involves determining a number of properties of another
# random value. Set the following parameters to their relevant truth values
# based on the value rand_3.

# NOTE: separate conditionals can be denoted by brackets [e.g. (a and b) or c]

rand_3 = randint(-100, 100)

divisible_by_3 = False
divisible_by_7 = False
positive = False
negative = False
between_0_and_15_inclusive = False

# <your code here>



'''
    When you're done, click Run or F5 to check that you've followed the
    instructions. It is suggested to run the tests a few times to ensure
    passing all tests wasn't by luck. Example solutions can be found at the
    bottom of the example checker file.

    The code below isn't for editing, it's used to run the test file when this
    program is run.
'''

if __name__ == '__main__':
    from L2_example_checker import run_tests
    run_tests()
