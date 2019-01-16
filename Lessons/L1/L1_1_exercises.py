#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following exercises below the appropriate   #
# comment, and click run when complete, using either the menu-bar at the top,  #
# or the F5 key on your keyboard.                                              #
################################################################################

# Set a variable 'my_int' to an integer value


# Now asign a random decimal value to a variable 'my_float'


# Create a list, "my_list", using my_int and my_float, as well as a boolean
# value of your choice, in any order you'd like.
# NOTE: lists can be created using <name = [item1, item2, 'item3', etc.]>


# Lists and tuples can contain any objects, including other lists and tuples.
# Redefine "my_tuple" (below) to contain my_list, and an additional item of a
# type of your choosing.
my_tuple = ()


# Finally, uncomment and fill out the dictionary "my_dict" below with the
# variables you've just created.
"""
my_dict = {
    'integer':
    'float':
    'list':
    'tuple':
    }
#"""


'''
    When you're done, click Run or F5 to check that you've followed the
    instructions. Example solutions can be found at the bottom of the example
    checker file.

    The code below isn't for editing, it's used to run the test file when this
    program is run.
'''

if __name__ == '__main__':
    from L1_2_exercise_checker import L1Tests
    L1Tests = L1Tests()
    # run the tests (with feedback)
    L1Tests.run_tests(verbose=True)
