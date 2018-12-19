#!/usr/bin/env python3
################################################################################
# This file contains a function used to test the LN_1_examples file.             #
################################################################################

# imports all the variables from LN_1_examples
from LN_1_examples import *
from ...TestRun import TestRun

class LNTests(TestRun):
    def test_thing():
        ''' Testing a thing. '''
        a = 2
        assert a == 1, "a = {} != 1".format(a)

    def helper(var):
        ''' Returns something useful. '''
        # code acting on var
        return var


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
