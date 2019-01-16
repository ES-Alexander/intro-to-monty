#!/usr/bin/env python3
################################################################################
# This file contains a function used to test the L1_2_exercises file, checking #
# that the correct variables are defined, and as the correct types and values. #
################################################################################

# imports all the variables from L1_examples
from L1_1_exercises import *
import sys; sys.path.append('..')
from TestRun import TestRun

class L1Tests(TestRun):
    def test_my_int(self):
        ''' Testing 'my_int' correctness. '''
        assert isinstance(my_int, int), "'my_int' should be an integer, "    +\
               'not a {!r}'.format(type(my_int).__name__)

    def test_my_float(self):
        ''' Testing 'my_float' correctness. '''
        assert isinstance(my_float, float), "'my_float' should be a float, " +\
               'not a {!r}'.format(type(my_float).__name__)

    def test_my_list(self):
        ''' Testing 'my_list' correctness. '''
        assert isinstance(my_list, list), "'my_float' should be a list, "    +\
               'not a {!r}'.format(type(my_list).__name__)
        assert my_int in my_list, "'my_list' should contain 'my_int'."
        assert my_float in my_list, "'my_list' should contain 'my_float'."
        assert True in my_list or False in my_list, "'my_list' should "      +\
               'contain a boolean value.'

    def test_my_tuple(self):
        ''' Testing 'my_tuple' correctness. '''
        assert isinstance(my_tuple, tuple), "'my_tuple' should be a tuple, " +\
               'not a {!r}'.format(type(my_tuple).__name__)
        assert my_list in my_tuple, "'my_tuple' should contain 'my_list'."
        assert len(my_tuple) >= 2, "'my_tuple should contain 'my_list' and " +\
               'at least one other item.'

    def test_my_dict(self):
        ''' Testing 'my_dict' correctness. '''
        assert isinstance(my_dict, dict), "'my_dict' should be a dictionary" +\
               ', not a {!r}'.format(type(my_dict).__name__)
        assert my_dict['integer'] is my_int, "'my_dict' should have "        +\
               "'my_int' as its value for the 'integer' key."
        assert my_dict['float'] is my_float, "'my_dict' should have "        +\
               "'my_float' as its value for the 'float' key."
        assert my_dict['list'] is my_list, "'my_dict' should have 'my_list'" +\
               " as its value for the 'list' key."
        assert my_dict['tuple'] is my_tuple, "'my_dict' should have "        +\
               "'my_tuple' as its value for the 'tuple' key."




#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    # Integer 
    my_int = 5 # Note that any integer value could have been selected

    # Float 
    my_float = 2.0 # Note that any float value could have been selected

    # List 
    my_list = [my_int, my_float, True]

    # Tuple 
    my_tuple = (my_list, 'extra')

    # Dictionary 
    my_dict = {
        'integer': my_int,
        'float': my_float,
        'list': my_list,
        'tuple': my_tuple
        }


    # run the automatic tests
    Tests = L1Tests()
    Tests.run_tests(verbose=True)
