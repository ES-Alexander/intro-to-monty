#!/usr/bin/env python3
################################################################################
# This file contains tests for the L4_1_exercises.py file.                     #
################################################################################

import sys; sys.path.append('..')
from TestRun import TestRun, Redirect

from random import randint
import os # for unnecessary file removal

class L4Tests(TestRun):
    def __init__(self, num_trials=100):
        ''' Initialise this test suite. '''
        super().__init__()
        self._num_trials = num_trials

        # correct implementations for tested functionality
        self._flatten = lambda *lists : sum(lists, [])
        
        # generalised recursive solutions to exclusion and match extraction
        #   (principles of recursion are covered in L8)
        self._excl = lambda a, *ls : a if not ls or not a else \
                     self._excl([c for c in a if c not in ls[0]], *ls[1:])
        self._common = lambda *ls : ls[0] if len(ls) == 1 or not ls[0] else \
                       self._common([c for c in ls[0] if c in ls[1]], *ls[2:])
        # paired exclusion and matches
        self._bd = lambda a, b : (self._excl(a,b), self._common(a,b),
                                  self._excl(b,a))

    # helper functions
    @staticmethod
    def gen_a_b():
        ''' Generates and returns two random lists. '''
        a = []; b = []
        for i in range(randint(0,20)):
            a += [randint(0,15)]; b += [randint(0,15)]
        return (a,b)

    @staticmethod
    def is_lambda(func):
        ''' Raises AssertionError if func is not a lambda function. '''
        assert callable(func) and func.__name__ == (lambda: None).__name__, \
               'Should be a lambda function.'

    # test functions
    def test_light_switch(self):
        ''' Tests the 'light_switch' function. '''
        out_file = 'temp.txt'
        try:
            with Redirect(sys.stdout, open(out_file,'w'), maintain=False):
                light_switch()
                a = [False]; light_switch(a)
                assert a[0], 'a = [False]; light_switch(a) should mean ' +\
                       'a = [True] afterwards.'
                light_switch(a)
                assert not a[0], 'a = [True]; light_switch(a) should mean ' +\
                       'a = [False] afterwards.'
                try:
                    light_switch(False)
                    light_switch(True)
                except TypeError:
                    assert False, 'Should detect when a boolean is passed ' +\
                           'in and respond appropriately.'
                try:
                    light_switch((False,))
                    light_switch((True,))
                except TypeError:
                    assert False, 'Should detect when a tuple is passed in ' +\
                           'and respond appropriately.'

            with open(out_file) as out:
                calls = ['', '[False]', '[True]', 'False', 'True',
                         '(False,)', '(True,)']
                expecteds = ['turned off the light',
                             'turned on the light', 'turned off the light',
                             'light is stuck off', 'light is stuck on']
                
                for i, expected in enumerate(expecteds):
                    line = out.readline()[:-1]
                    assert line == expected, \
                           'light_switch({})'.format(calls[i]) +\
                           'should print {!r}, not \n    {!r}'.format(expected,
                                                                      line)
        finally:
            os.remove(out_file) # unnecessary file
    
    def test_flatten(self, f2=''):
        ''' Tests the 'flatten' function, or 'flatten2' if f2 == 2 or '2'. '''
        for i in range(self._num_trials):
            lists = []
            if i == 0:
                lists += [[1,2,3,4],[5,6,7],[8,9]] # easy to see
            else:
                for j in range(randint(1,10)):
                    lists += list(self.gen_a_b())  # general random tests
            correct = self._flatten(*lists)
            if f2:
                result = flatten2(*lists)
            else:
                result = flatten(*lists)
            assert result == correct, 'flatten{} should return '.format(f2) +\
                   'a list of all elements in the inputted lists\n' +\
                   '(e.g. flatten{}({}) == {}, not {})'.format(f2,
                        ','.join(['{}']*len(lists)).format(*lists),
                        correct, result)
                    
    def test_flatten2(self):
        ''' Tests the 'flatten2' function. '''
        self.test_flatten(2)
    
    def test_a_only(self):
        ''' Tests the 'a_only' function. '''
        self.is_lambda(a_only)
        for i in range(self._num_trials):
            if i == 0:
                a,b = [1,2,3,1],[1,4,5] # easy to see
            else:
                a,b = self.gen_a_b()    # general random tests
            correct = self._excl(a,b)
            result = a_only(a,b)
            assert result == correct, 'a_only should return ' +\
                   "a list of elements exclusive to 'a'\n" +\
                   "(e.g. a_only({}) == {}, not {})".format('{},{}'.format(a,b),
                                                           correct, result)

    def test_overlap(self):
        ''' Tests the 'overlap' function. '''
        self.is_lambda(overlap)
        for i in range(self._num_trials):
            if i == 0:
                a,b = [1,2,3,1],[1,4,5] # easy to see
            else:
                a,b = self.gen_a_b()    # general random tests
            correct = self._common(a,b)
            result = overlap(a,b)
            assert result == correct, 'overlap should return ' +\
                   "a list of elements in both 'a' and 'b'\n" +\
                   "(e.g. overlap({}) == {}, not {})".format(
                       '{},{}'.format(a,b), correct, result)

    def test_breakdown(self):
        ''' Tests the 'breakdown' function. '''
        self.is_lambda(breakdown)
        for i in range(self._num_trials):
            if i == 0:
                a,b = [1,2,3,1],[1,4,5] # easy to see
            else:
                a,b = self.gen_a_b()    # general random tests
            correct = self._bd(a,b)
            result = breakdown(a,b)
            assert result == correct, 'breakdown should return ' +\
                   "a tuple of (elements exclusive to 'a', elements shared" +\
                   "by both 'a' and 'b', elements exclusive to 'b')\n" +\
                   "(e.g. breakdown({}) == {}, not {})".format(
                       '{},{}'.format(a,b), correct, result)


#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':

    # Default variables
    '''
        Write a function 'light_switch' which takes a variable 'is_on', set to a
        list containing 'True' by default (ie [True]). Calling light_switch
        should toggle the switch, so if is_on contains True it should be swapped
        out for False, with 'turned off the light' printed to the console. If
        is_on contains False, it should be swapped for True, and 'turned on the
        light' should be printed. If a tuple is passed in as is_on, or a boolean
        is passed in directly (can check with the 'isinstance' function), the
        light cannot be toggled, so do not attempt to replace the contents, and
        instead print 'light is stuck on' if is_on is True and 'light is stuck
        off' if is_on is False. No value should be returned.

        e.g.
            light_switch() # -> turned off the light
            a = [False]
            light_switch(a) # -> turned on the light
            print(a) # -> [True]
            b = False
            light_switch(b) # -> light is stuck off
            print(b) # -> False
            c = tuple([True])
            light_switch(c) # -> light is stuck on
            print(c) # -> (True,)
    '''
    
    def light_switch(is_on=[True]):
        ''' Attempts to toggle the light state in is_on[0].

        Prints a relevant message informing of the updated state.

        light_switch(*list[bool]/tuple(bool)/bool) -> None

        '''
        if isinstance(is_on, (bool, tuple)):
            # input is immutable - check if light is stuck on, else stuck off
            if (isinstance(is_on, tuple) and is_on[0]) or \
               (isinstance(is_on, bool) and is_on): 
                print('light is stuck on')
            else:
                print('light is stuck off')
            return # done now - no need to run the rest of the function

        if is_on[0]:
            is_on[0] = False
            print('turned off the light')
        else:
            is_on[0] = True
            print('turned on the light')
        

    # * Dereferencing (Unknown Number of Parameters)
    '''
        Implement the function 'flatten' below, which takes in an unknown number
        of lists and returns a single list of all the inputted lists joined
        together. You may find it helpful to use a builtin function to help
        achieve this, but you are not required to do so.

        Write a second method 'flatten2' beneath, which uses a different
        implementation to achieve the same result as 'flatten'.

        e.g.
        flatten([1,2,3,4],[5,6,7],[9,10,11]) -> [1,2,3,4,5,6,7,8,9,10,11]
    '''
    
    def flatten(*lists):
        ''' Returns a combined list of the inputted lists.

        e.g. flatten([1,2,3],[4,5,6]) -> [1,2,3,4,5,6]

        flatten(*list) -> list

        '''
        output = []
        for l in lists:
            output += l
        return output

    flatten2 = lambda *lists : sum(lists, []) # this is a bit unconventional
        
    
    # Lambdas and List Comprehension
    '''
        Write a lambda function 'a_only' which takes two lists (a,b) and returns
        a list of all elements that are in 'a' but not in 'b' (effectively a
        copy of 'a' without any element values shared by 'b').
        
        Write a lambda function 'overlap' which takes in two lists (a,b) and
        returns a list of all elements that are in both 'a' AND 'b'.

        Write a lambda function 'breakdown' which takes in two lists (a,b), and
        returns a tuple with its first element as a list of elements only in a,
        its second element as a list of elements in both a and b, and its third
        element as a list of elements only in b. You may use your 'overlap' and
        'a_only' functions to implement this.

        e.g.
        a = [1,2,3,4,1]
        b = [4,2,5,9]
        a_only(a,b)    # returns [1,3,1]
        overlap(a,b)   # returns [2,4]
        breakdown(a,b) # returns ([1,3,1],[2,4],[5,9])
    '''
    a_only = lambda a, b : [c for c in a if c not in b]
    overlap = lambda a, b : [c for c in a if c in b]
    breakdown = lambda a, b : (a_only(a,b), overlap(a,b), a_only(b,a))

    Tests = L4Tests()
    Tests.run_tests(verbose=True)
