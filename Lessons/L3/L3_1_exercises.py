#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following exercises below the appropriate   #
# comment, and click run when complete, using either the menu-bar at the top,  #
# or the F5 key on your keyboard.                                              #
################################################################################

# setup code for tests
if __name__ == '__main__':
    import sys; sys.path.append('..')
    from TestRun import Redirect
    from L3_2_exercise_checker import L3Tests
    out_file = 'test_files/out.txt'
    # start a logger for printed output
    Out = Redirect(sys.stdout, open(out_file,'w'), maintain=False)

# setup code for exercises
from random import randint
a = []

# Creating something random
'''
    The imported 'randint' function is a random integer generator, which can be
    used as 'randint(a,b)' to return a random integer between a and b
    (inclusive) (a must be less than b). For example, randint(0,5) returns
    a random integer between 0 and 5.

    Change the variable 'num_elements' to be a random number between 1 and 50.

    Next modify the empty list 'a' by adding in 'num_elements' elements. Each
    element should be a random integer between -100 and 100, and no element
    should be repeated. If a new value is generated as a repeat of an existing
    element, generate more values repeatedly until a unique value has been
    found, then continue to the next element.

    You can use print statements to help you understand what your code is doing,
    but make sure none of them start with 'NE:', 'A:', or 'B:'.
'''

num_elements = 0 # replace this

# modify a to have 'num_elements' elements




print('NE:', num_elements, 'A:', a) # keep this here - it's needed for testing

# The largest of them all
'''
    Now that 'a' has been generated, write some code to determine and print
    the largest value in 'a'. You should not modify the variable 'a', and should
    use loops, not the builtin 'max' function. 
'''

# determine and print the maximum value in 'a'





print('A:', a) # keep this here - it's needed for testing

# A subset (of 'a')
'''
    Create a list 'b', and to it all elements of 'a' that have a magnitude less
    than the length of 'a'. The builtin 'abs' function returns the absolute
    value of a number, which is its magnitude (e.g. abs(-1) = 1).
'''

# b = ...?
b = 0 # replace this




print('B:', b) # keep this here - it's needed for testing

'''
    When you're done, click Run or F5 to check that you've followed the
    instructions. Example solutions can be found at the bottom of the exercise
    checker file.

    Because the results here change every time, it's suggested you run the file
    multiple times to see if you consistently pass the tests.
    
    The code below isn't for editing, it's used to run the test file when this
    program is run.
'''

if __name__ == '__main__':
    Out.close()
    L3Tests = L3Tests(out_file)
    # run the tests (with feedback)
    L3Tests.run_tests(verbose=True)

    # print the previously hidden output (after the test output)
    with open(out_file) as out:
        print(out.read())
