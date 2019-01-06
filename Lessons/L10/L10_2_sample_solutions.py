#!/usr/bin/env python3
# L10_1_examples SAMPLE SOLUTION (code testing)

# import the TestRun module
import sys
sys.path.append('..')
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

    Once you've found and fixed the bug (only edit the required line in the copy
    of the function definition below the black box tests), determine the
    relevant white box test cases and implement a new complete test suite, with
    all the relevant tests.
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
    No input type requirements are presented, but the docstring running code
    suggests all inputs should be integers. As such, other input types have
    undefined output, and cannot be validly tested against the specification.

    To get the first return output type, 'a' must be between 0 and 'c'
    inclusive, with non-negative 'c'. This provides edge cases of a = 0, a = c,
    and a = c = 0.

    The second return output type requires a < 0 or a > c. As such, a = -1 and
    a = c + 1 are edge cases, checking for c as a general integer (as below).

    Since the output depends on b relative to c, b should be tested in each
    test as less than and greater than c. When they are equal, max=min=b=c.

    No restriction is placed on n, so it is assumed it is equally valid
    anywhere within the set of integers. Without tighter specification, we test
    for positive and negative for each other test.
    
    A      C       EXPECTED OUTPUT     REASON FOR TEST
     0      0       -min(b,c)           Edge case (opt1, min a, min c, [a=c=0])
     0      +ve     -min(b,c)           Edge case (opt1, min a, general c [a=0])
     c      +ve     (n*a)-min(b,c)      Edge case (opt1, max a, general c [a=c])
     0<a<c  >=2     (n*a)-min(b,c)      General case (opt1, [0<a<c, c>1])
     -1     int     (n*a)+max(b,c)      Edge case (opt2, max a < 0, [a=-1])
     c+1    int     (n*a)+max(b,c)      Edge case (opt2, min a > c, [a=c+1])
     -ve    int     (n*a)+max(b,c)      General case (opt2, general c, [a<0])
     int    -ve     (n*a)+max(b,c)      General case (opt2, general a, [c<0])

    While there are overlaps in several of the inputs required here, the test-
    cases are each given their own test to display how each test-case is being
    tested.
'''

# implementation of test suite (black box tests)

class FunctionTestsBB(TestRun):
    ''' A test suite of black-box tests for func_to_test. '''
    def __init__(self):
        ''' Initialise relevant testing variables. '''
        super().__init__()
        self.range_mag = 10000 # magnitude of positive/negative integers
        self.num_trials = 100   # number of trials per test

    def _general_test(self, correct, a_range, b_range, c_range, n_range):
        ''' A generic test for func_to_test.

        Tests for the same function tend to require the same/similar format.

        Allows specification of the formula to use for the correct result, and
            ranges for the 'a', 'b', 'c', and 'n' inputs.

        'X_range' is a string of 'min,max' to allow for variable inputs. It also
            has special options of 'int' to test as a general integer, '+ve' and
            '-ve' to test as appropriate, and as a single value, to test one
            value instead of a range.

        FunctionTestsBB._general_test(str, str, str, str, str) -> None

        '''
        # shortcut inputs for full integer range or single value
        a_range = self._format_input_shortcut(a_range)
        b_range = self._format_input_shortcut(b_range)
        c_range = self._format_input_shortcut(c_range)
        n_range = self._format_input_shortcut(n_range)

        # run test trials
        for trial in range(self.num_trials):
            # func(*(a,b,c)) -> func(a,b,c)   [splits tuple/list into inputs]
            # eval('a,b,c') = (a,b,c)         [turns string into tuple]
            c = randint(*eval(c_range)) # others refer to c, so do c first
            a = randint(*eval(a_range))
            b = randint(*eval(b_range))
            n = randint(*eval(n_range))
            ret = func_to_test(a,b,c,n) # return value
            cor = eval(correct)         # correct value
            assert ret == cor, '(a,b,c,n)=({},{},{},{})'.format(a,b,c,n) +\
                   ' -> \n\t should result in {}, not {}'.format(cor, ret)

    def _format_input_shortcut(self, input_range_str):
        ''' Returns formatted input if input in a shortcut format.

        If no shortcut is specified, returns input_range_str.

        Valid shortcuts are 'int', '+ve', '-ve', a single value, or a tilde
            preceding a variable name to test around that variable.

        FunctionTestsBB._format_input_shortcut(str) -> str
    
        '''
        if input_range_str == 'int':
            # full integer range (+ve,0,-ve)
            return '-{0},{0}'.format(self.range_mag)
        elif input_range_str == '+ve':
            return '1,{}'.format(self.range_mag)    # positive integers
        elif input_range_str == '-ve':
            return '-{},-1'.format(self.range_mag)  # negative integers
        elif input_range_str.startswith('~'):
            # test about variable specified after tilde (~var)
            return '{0}-{1},{0}+{1}'.format(input_range_str[1:], self.range_mag)
        elif ',' not in input_range_str:
            return '{0},{0}'.format(input_range_str) # '-c' -> '-c,-c'
        else:
            return input_range_str

    # Option 1 -> (n*a) - min(b,c)
    def test_option1_1(self):
        ''' Testing edge case (opt1, min a, min c, [a=c=0]) -> 0. '''
        self._general_test('-min(b,c)','0','~c','0','int')

    def test_option1_2(self):
        ''' Testing edge case (opt1, min a, general c, [a=0]) -> -min(b,c). '''
        self._general_test('-min(b,c)','0','~c','+ve','int')

    def test_option1_3(self):
        ''' Testing edge case (opt1, max a, general c, [a=c]) -> opt1. '''
        self._general_test('(n*a)-min(b,c)','c','~c','+ve','int')

    def test_option1_4(self):
        ''' Testing general case (opt1, [0<a<c, c>1]) -> opt1. '''
        self._general_test('(n*a)-min(b,c)','1,c-1','~c',
                      '2,{}'.format(self.range_mag),'int')

    # Option 2 -> (n*a) + max(b,c)
    def test_option2_1(self):
        ''' Testing edge case (opt2, max a < 0, [a=-1]) -> opt2. '''
        self._general_test('(n*a)+max(b,c)','-1','~c','int','int')

    def test_option2_2(self):
        ''' Testing edge case (opt2, min a < c, [a=c+1]) -> opt2. '''
        # THIS TEST FAILS (func_to_test uses wrong equation)
        self._general_test('(n*a)+max(b,c)','c+1','~c','int','int')

    def test_option2_3(self):
        ''' Testing general case (opt2, general c, [a<0]) -> opt2. '''
        self._general_test('(n*a)+max(b,c)','-ve','~c','int','int')

    def test_option2_4(self):
        ''' Testing general case (opt2, general a, [c<0]) -> opt2. '''
        self._general_test('(n*a)+max(b,c)','int','~c','-ve','int')


# run the black-box tests on the original (incorrect) func to test
Tests = FunctionTestsBB()
Tests.run_tests(verbose=True) # display reasoning for any failed tests




#####----- EDITED THIS ONE -----#####
def func_to_test(a,b,c,n):
    ''' Returns (n * a) - min(b,c) if 0 <= a and a <= c, else returns
    (n * a) + max(b,c).

    func_to_test(int, int, int, int) -> int

    '''
    temp_val = n * (a - 1)
    if a < 0 or a > c: # changed from 'if c < 0 or a < 0:'
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
    The first branch here contains a separate if/else statement. This nested if-
    block can be flattened to have two branches, with branch 0 occurring if
    (a<0 or a>c) and b>c, and branch 1 occurring if (a<0 or a>c) and b<=c.

    For branch 0, this gives edge conditions at a=-1, a=c+1, and b=c+1. General
    cases are (a<-1, b>c+1) and (a>c+1, b>c+1).
    
    Branch 1 has edge conditions at a=-1, a=c+1, and b=c. General cases are
    (a<-1, b<c) and (a>c+1, b<c).

    Branch 2 is in the calculation of the sign of n. It has edge cases at n=-1
    and n=0, and general cases when n>0 and n<-1.

    Branch 3 is the for-loop, which effectively performs the operation
    2 * n * (a - b). Because n is an integer, only even numbers of iterations
    are possible. 0 iterations occurs when n=0, 2 iterations when n=+/-1,
    doubling for each extra n. When n=0, output_val is 0, and n*b is 0, so the
    result is -min(b,c), as expected. When n=+/-1, output_val is +/-(a-b) after
    the first iteration, then +/-2*(a-b) after the second. output_val is then
    halved, and +/-b is added, negating the -b in output_val, resulting in
    n*a - min(b,c), as desired. The loop continues with this pattern, so it is
    reasonable to assume that the result will also continue to be
    n*a - min(b,c). There is no upper limit to the value of n, so no upper limit
    can be tested for the loop.

    Where letters are left out in the test-cases below, they are general values,
    so should be tested at a negative, 0, and positive value in each test.

    BRANCH 0 (a<0 or a>c and b>c)
    A     B       EXPECTED OUTPUT   REASON FOR TEST
     -1    c+1     -n + b            Edge case (opt2, max a<0, min b>c)
     c+1   c+1     n*a + b           Edge case (opt2, min a>c, min b>c)
     <-1   >c+1    n*a + b           General case (opt2, a<0, general b>c)
     >c+1  >c+1    n*a + b           General case (opt2, a>c, general b>c)

    BRANCH 1 (a<0 or a>c and b<=c)
    A     B       EXPECTED OUTPUT   REASON FOR TEST
     -1    c       -n + c            Edge case (opt2, max a<0, max b<=c)
     c+1   c       n*a + c           Edge case (opt2, min a>c, max b<=c)
     <-1   <c      n*a + c           General case (opt2, a<0, general b<=c)
     >c+1  <c      n*a + c           General case (opt2, a>c, general b<=c)

    BRANCH 2 (sign(n))
    A         C     N      EXPECTED OUTPUT   REASON FOR TEST
     0<=a<=c   +ve   0      -min(b,c)         Edge case (opt1, min n>=0)
     0<=a<=c   +ve   -1     -a - min(b,c)     Edge case (opt1, max n<0)
     0<=a<=c   +ve   +ve    (n*a)-min(b,c)    General case (opt1, n>0)
     0<=a<=c   +ve   <-1    (n*a)-min(b,c)    General case (opt1, n<-1)

    BRANCH 3 (loop)
    A         C     N       EXPECTED OUTPUT   REASON FOR TEST
     0<=a<=c   +ve   0       -min(b,c)         Edge case (opt1, 0 iterations)
     0<=a<=c   +ve   +/-1    (n*a)-min(b,c)    Edge case (opt1, 2 iterations)
     0<=a<=c   +ve   |n|>1   (n*a)-min(b,c)    General case (opt1, n iterations)

    Looking at the test cases presented here, there are a number of overlaps
    between branch 0 and 1, and between branch 2 and 3. Overlaps are convenient
    because they allow you to test multiple cases simultaneously, or at least
    easily do so in the same test. The black-box test class was used to display
    how each test-case can be tested individually. The white-box class will
    instead be used to display how multiple test-cases can be integrated into
    a more general test, which only passes if all the covered test-cases pass.

    Unlike in the lesson notes testing example, many of the black box tests here
    are not immediately relatable to the white box tests. The first three tests
    in branch 0 and 1 cover the first three opt2 BB tests, but the remainder are
    hard to relate because of the different variables being considered.
'''

class FunctionTestsWB(FunctionTestsBB):
    ''' A test suite of white-box tests for func_to_test.

    Adds to the black-box tests in FunctionTestsBB, since the black-box tests
        are already implemented.

    '''
    # BRANCH 0/1 (option 2)
    def test_option2_wb_1(self):
        ''' Test option 2 edge-cases.

        (a,b) = (-1,c+1), (c+1,c+1), (-1,c), (c+1,c).

        '''
        # 'cor', 'a_range', and 'b_range' change across these test cases
        cor_a_b = [('-n+b','-1','c+1'), ('n*a+b','c+1','c+1'),
                   ('-n+c','-1','c'), ('n*a+c','c+1','c')]
        for inputs in cor_a_b:
            self._general_test(inputs[0],inputs[1],inputs[2],'int','int')

    def test_option2_wb_2(self):
        ''' Test option 2 general cases.

        (a,b) = (<-1,>c+1), (>c+1,>c+1), (<-1,<c), (>c+1,<c).

        '''
        # 'cor', 'a_range', and 'b_range' change across these test cases
        cor_a_b = [('(n*a)+b','-self.range_mag,-2','c+2,self.range_mag+2'),
                   ('(n*a)+b','c+2,self.range_mag+2','c+2,self.range_mag+2'),
                   ('(n*a)+c','-self.range_mag,-2','-self.range_mag-1,c-1'),
                   ('(n*a)+c','c+2,self.range_mag+2','-self.range_mag-1,c-1')]
        for inputs in cor_a_b:
            cor, a, b = inputs
            self._general_test(cor,a,b,'int','int')

    # BRANCH 2/3 (option 1)
    def test_option1_wb_1(self):
        ''' Test option 1 edge cases. [0<=a<=c, n=0,-1,1]. '''
        # 'cor' and 'n_range' change across these test cases
        cor_n = [('-min(b,c)','0'), ('-a-min(b,c)','-1'), ('a-min(b,c)','1')]
        for inputs in cor_n:
            cor, n = inputs
            self._general_test(cor,'0,c','int','+ve',n)

    def test_option1_wb_2(self):
        ''' Test option 1 general cases. [0<=a<=c, n=+ve,<-1]. '''
        # only 'n_range' changes across these test cases
        n_vals = ['+ve','-{},-1'.format(self.range_mag)]
        for n in n_vals:
            self._general_test('(n*a)-min(b,c)','0,c','int','+ve',n)


# run the new tests on the corrected func_to_test
Tests2 = FunctionTestsWB()
Tests2.run_tests(verbose=True) # display reasoning for any failed tests



