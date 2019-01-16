#!/usr/bin/env python3
################################################################################
# This file contains tests for the L3_1_exercises.py file.                     #
################################################################################

import sys; sys.path.append('..')
from TestRun import TestRun, Redirect

import os
if not os.path.exists('test_files'):
    os.mkdir('test_files')

from random import randint

class L3Tests(TestRun):
    def __init__(self, out_file):
        ''' Initialise this test suite '''
        super().__init__()

        self._print_log = []
        prefixes = ['NE:','A:','B:']
        with open(out_file) as out:
            prev = ''
            for line in out:
                for index, prefix in enumerate(prefixes):
                    if line.startswith(prefix):
                        if index == 1 and ':' not in prev:
                            self._print_log += [prev]
                        self._print_log += [line]
                        break # no need to check other prefixes
                prev = line

    def run_tests(self, *args, **kwargs):
        ''' Overwrite run_tests to display a message if cannot run. '''
        if len(self._print_log) == 4:
            print(self._print_log)
            super().run_tests(*args, **kwargs)
            return
        print('#' + '-'*35, 'L3Tests', '-'*34 + '#\n')
        print('    Testing could not be completed because of invalid printed',
              'output.', file=sys.stderr)
        print('\n#' + '-'*78 + '#\n')

    def test_creation(self):
        ''' Testing that generated 'a' and num_elements are valid. '''
        num_els, a = self._print_log[0].split(' A: ')
        num_els = int(num_els[4:])
        a = eval(a)
        
        assert 1 <= num_els <= 50, "'num_elements' should be a random number" +\
               'between 1 and 50, which {} is not.'.format(num_els)

        assert len(a) == num_els, "'a' should contain 'num_elements' elements"+\
               'which is {}, not {}.'.format(num_els, len(a))

        for val in a:
            assert -100 <= val <= 100, "Values in 'a' should be between -100" +\
                   'and 100, which {} is not.'.format(val)

    def test_maximum(self):
        ''' Testing that the determined maximum value is correct. '''
        a = eval(self._print_log[0].split(' A: ')[1])
        max_val = int(self._print_log[1])

        assert max_val == max(a), 'The print maximum ({}) '.format(max_val) +\
               "is not equal to the maximum value of 'a' ({})".format(max(a))

        a2 = eval(self._print_log[2][3:])
        assert a2 == a, "'a' should not have changed in determining the " +\
               'maximum, but was {} and became {}.'.format(a, a2)

    def test_subset(self):
        ''' Testing that the determined subset of 'a' is correct. '''
        a = eval(self._print_log[0].split(' A: ')[1])
        b = eval(self._print_log[3][3:])
        b_cor = [c for c in a if abs(c) < len(a)]

        assert b == b_cor, "'b' should be a subset of 'a', containing all" +\
               "elements with a magnitude less than the length of 'a'.\n"  +\
               'b={} is invalid (should be {})'.format(b, b_cor)
        


#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    out_file = 'test_files/outX.txt'
    with Redirect(sys.stdout, open(out_file,'w'), maintain=False):
        a = []

        # Creating something random
        '''
            The imported 'randint' function is a random integer generator, which
            can be used as 'randint(a,b)' to return a random integer between a
            and b (inclusive) (a must be less than b). For example, randint(0,5)
            returns a random integer between 0 and 5.

            Change the variable 'num_elements' to be a random number between 1
            and 50.

            Next modify the empty list 'a' by adding in 'num_elements' elements.
            Each element should be a random integer between -100 and 100, and no
            element should be repeated. If a new value is generated as a repeat
            of an existing element, generate more values repeatedly until a
            unique value has been found, then continue to the next element.
        '''
    
        num_elements = randint(1,50)

        # modify a to have 'num_elements' elements
        for i in range(num_elements):
            new = randint(-100, 100)
            while new in a:
                new = randint(-100, 100)
            a += [new]

        print('NE:', num_elements, 'A:', a)
        
        # The largest of them all
        '''
            Now that 'a' has been generated, write some code to determine and
            print the largest value in 'a'. You should not modify the variable
            'a', and should use loops, not the builtin 'max' function. You can
            use print statements to help you understand what your code is doing,
            but you will need to remove them before the automatic testing works.
        '''

        # determine and print the maximum value in 'a'
        max_val = a[0]
        for value in a:
            if value > max_val:
                max_val = value
        print(max_val)

        print('A:', a)

        # A subset (of 'a')
        '''
            Create a list 'b', and to it all elements of 'a' that have a
            magnitude less than the length of 'a'. The builtin 'abs' function
            returns the absolute value of a number, which is its magnitude
            (e.g. abs(-1) = 1).
        '''

        # b = ...?
        b = []
        a_len = len(a) # only calculate this once (not every iteration)
        for value in a:
            if abs(value) < a_len:
                b += [value]

        print('B:', b)


    # run the automatic tests
    Tests = L3Tests(out_file)
    Tests.run_tests(verbose=True)

    with open(out_file) as out:
        print(out.read())
    
