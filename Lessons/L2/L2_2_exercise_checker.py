#!/usr/bin/env python3
################################################################################
# This file contains tests for the L2_1_exercises file.                        #
################################################################################

from L2_1_exercises import *
import sys; sys.path.append('..')
from TestRun import TestRun

class L2Tests(TestRun):
    def test_bigger(self):
        ''' Testing the 'which one is bigger?' exercise. '''
        vals = [val_1, val_2]; vals.sort
        small, big = vals
        assert larger == big, "'larger' should be set to the larger value.\n" +\
               '    {} > {}'.format(big, small)
        assert smaller == small, "'smaller' should be set to the smaller " +\
               'value.\n    {} < {}'.format(small, big)

    def test_even_odd(self):
        ''' Testing even/odd categorisation of rand_1 and rand_2. '''
        for i in range(2):
            val_name = 'rand_{}'.format(i+1)
            val = eval(val_name)
            if val % 2 == 0:
                assert val in even, "{} = {}, should be in 'even' list.".format(
                    val_name, val)
            else:
                assert val in odd, "{} = {}, should be in 'odd' list.".format(
                    val_name, val)

    def test_diagnosis(self):
        ''' Testing rand_3 categorisation. '''
        assert multiple_of_3 == (rand_3 % 3 == 0), "'rand_3' = {}".format(
            rand_3) + ', which is a multiple of 3.'
        assert multiple_of_7 == (rand_3 % 7 == 0), "'rand_3' = {}".format(
            rand_3) + ', which is a multiple of 7.'
        assert positive == (rand_3 >= 0), "'rand_3' = {}".format(rand_3) +\
               ', which is positive.'
        assert negative == (rand_3 < 0), "'rand_3' = {}".format(rand_3)  +\
               ', which is negative.'
        assert between_0_and_15_inclusive == (0 <= rand_3 <= 15), \
               "'rand_3' = {}, which is between 0 and 15 (inclusive).".format(
                   rand_3)

#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    # Which one is bigger?
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



    # Programmer's Diagnosis
    rand_3 = randint(-100, 100)

    equals_0 = (rand_3 == 0)
    # Solution
    multiple_of_3 = (rand_3 % 3 == 0)
    multiple_of_7 = (rand_3 % 7 == 0)
    positive = (rand_3 >= 0)
    negative = (rand_3 < 0)
    between_0_and_15_inclusive = (0 <= rand_3 <= 15)



    # run the tests
    Tests = L2Tests()
    Tests.run_tests(verbose=True)
