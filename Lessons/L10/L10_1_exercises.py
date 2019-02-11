#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following exercises below the appropriate   #
# comment. A sample solution for the code testing exercise is provided in the  #
# file L10_example_solution.py.                                                #
################################################################################

# import the TestRun module
import sys; sys.path.append('..')
from TestRun import TestRun

from random import randint

# Code Testing
'''
    Develop a set of black box and white box test-cases for the following
    function, then implement a suitable test suite underneath. For numbers with
    no restrictions, it is suggested to test with them as 0, positive, and
    negative for every determined test case.

    The implementation of this function has intentionally been done badly, both
    to increase the complexity of understanding the functionality, and to add
    implementation features which require testing. You should also find that the
    function does not fully implement its specification. Before moving on to the
    white box test cases, implement your black box test cases to see if they
    pick up on the issue. From there, try to identify and fix the bug that has
    been left (only one line of code should actually NEED to be modified to meet
    the specification).

    Once you've found and fixed the bug (only edit the required line), determine
    the relevant white box test cases and add any additional ones to your test
    suite.

    Finally, try to implement the full function correctly in a single line, and
    test that with your tests as well.
'''

def func_to_test(a,b,c,n):
    ''' Returns (n * a) - min(b,c) if 0 <= a and a <= c, else returns
    (n * a) + max(b,c).

    func_to_test(int, int, int, int) -> int

    '''
    temp_val = n * (a - 1)
    if c < 0 or a < 0:
        if b > c:
            return temp_val + b + n
        else:
            return temp_val + c + n

    sign = -1 if n < 0 else 1
    
    output_val = 0
    for i in range(sign * 2 * n):
        output_val += sign * (a - b)
        
    return output_val/2 + (n * b) - min(b,c)

# black box test-cases
'''
    
'''

class FunctionTestsBB(TestRun):
    ''' '''
    # setup/tests


# run the black-box tests on the original (incorrect) func to test
Tests = FunctionTestsBB()
Tests.run_tests(verbose=True) # display reasoning for any failed tests




#####----- EDIT THIS ONE -----#####
def func_to_test(a,b,c,n):
    ''' Returns (n * a) - min(b,c) if 0 <= a and a <= c, else returns
    (n * a) + max(b,c).

    func_to_test(int, int, int, int) -> int

    '''
    temp_val = n * (a - 1)
    if c < 0 or a < 0:
        if b > c:
            return temp_val + b + n
        else:
            return temp_val + c + n

    sign = -1 if n < 0 else 1
    
    output_val = 0
    for i in range(sign * 2 * n):
        output_val += sign * (a - b)
        
    return output_val/2 + (n * b) - min(b,c)

# white box test-cases
'''
    
'''

# implementation of test suite

class FunctionTestsWB(FunctionTestsBB):
    ''' A test suite of white-box tests for func_to_test.

    Adds to the black-box tests in FunctionTestsBB, since the black-box tests
        are already implemented.

    '''
    # setup/tests


# run the new tests on the corrected func_to_test
Tests2 = FunctionTestsWB()
Tests2.run_tests(verbose=True) # display reasoning for any failed tests



# single-line definition
func_to_test = None

#Tests2.run_tests() # run the tests on the new definition (once defined)


# Repositories
'''
    Set up a GitHub or BitBucket account and your own Git or Mercurial
    repository (both platforms support both types).

    With an account set up and a repository made, create a basic README file
    including the author (you), the last modified date, and what the repository
    is for.

    Next download your chosen repository system and get your repo cloned onto
    your computer. Try creating and adding a file, then changing it, committing
    those changes with a meaningful message, and pushing the commit to the
    master repo. Try cloning the repo into two separate folders on your
    computer, and use a terminal to commit and push some changes in one, then
    navigate into the other and pull the latest changes so that both copies are
    up to date.

    If you have any personal programming projects you'd like to do, dedicate
    this repo to one of them, and post some information about the project in the
    GitHub Projects tab, or using the Boards option in BitBucket. It's often
    useful to have columns/boards for Todo, In Progress, and Done as a minimum.
'''
