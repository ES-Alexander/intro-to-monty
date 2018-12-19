#!/usr/bin/env python3

import traceback # controlled printing of tracebacks (from caught Exceptions)

class TestRun(object):
    ''' A class for running tests. '''

    PASS = 1
    FAIL = 0
    ERROR = -1
    
    def __init__(self):
        ''' A class for running tests and printing relevant output.

        Tests should be in a class which inherits from TestRun, and can be run
            by instantiating that class and running run_tests(), or run_test().
            Both running methods take a boolean for verbosity, which defaults to
            False for multiple tests and True for single tests. 'run_tests'
            has an argument 'methods' which allows specifying a set of desired
            test methods to run (defaults to all).

        Test methods should be instancemethods of the class, and should begin
            with 'test_'. The test component should be an assert statement,
            preferably with failure reasoning provided as the second argument,
            e.g.:
                    assert 1 == 2, '1 is not equal to 2'
            
        Constructor: TestRun()

        '''
        self._TP = TestPrint()

    def run_tests(self, methods=[], section='', verbose=False):
        ''' Runs the specified methods at the given verbosity.

        'methods' is a list of the test methods to run. If left empty all the
            tests in the class are run.

        'section' is the name of the section currently being tested. If left
            empty defaults to the name of the testing class.

        'verbose' is a boolean specifying verbosity. If True, any tests which
            fail will print their failure reason (the string provided as the
            second argument of the assert statement (assert bool, str)), and
            any tests which raise exceptions will print their traceback.

        TestRun.run_tests(*list, *str, *bool) -> None
        
        '''
        if not section:
            section = type(self).__name__
        self._TP.print_section(section)
        
        if not methods:
            # default to run all methods
            methods = [m for m in dir(self) if m.startswith('test_')]
        
        # initialise counts
        num_tests = len(methods)
        passes = 0; failures = 0; errors = 0

        # run the specified methods
        for method in methods:
            result = self.run_test(method, verbose) # run the test
            # increment the relevant count
            if result == TestRun.PASS:
                passes += 1
            elif result == TestRun.FAIL:
                failures += 1
            elif result == TestRun.ERROR:
                errors += 1

        # print an output specifying results and the end of the section
        self._TP.section_end(num_tests, passes, failures, errors)

    def run_test(self, test_name, verbose=True):
        ''' Returns the success state of running test_name.

        Return values are within the set [TestRun.PASS, TestRun.FAIL,
            TestRun.ERROR].

        'test_name' should be an instance method of the running class.

        'verbose' is a boolean specifying verbosity. If True, a failing test
            will print its failure reason (the string provided as the
            second argument of the assert statement (assert bool, str)), and
            a test which raises an exception will print its traceback.

        TestRun.run_test(str, *bool) -> int

        '''
        try:
            exec('ss=self.{}()'.format(test_name))
            self._TP.test_success(test_name)
            return TestRun.PASS
        except AssertionError as e:
            self._TP.test_failure(test_name)
            if verbose:
                print('    Test failed because:', str(e))
            return TestRun.FAIL
        except Exception as e:
            self._TP.test_error(test_name)
            if verbose:
                traceback.print_tb(e.__traceback__)
                print('    {}: {}'.format(type(e).__name__, str(e)))
            return TestRun.ERROR
                

class TestPrint(object):
    ''' A class for printing test success states. '''
    # Terminal/IDLE colour specifier
    ColourMap = {'TERM':
                 {'ERROR':33, 'PASS':32, 'FAIL':31, 'STD':0},
                 'IDLE':
                 {'ERROR':'KEYWORD', 'PASS':'STRING', 'FAIL':'COMMENT',
                  'STD':'stdout'}
                }
    
    def __init__(self):
        ''' A class for printing coloured, formatted test success states.

        Implements behaviour for both IDLE and a standard terminal.

        Constructor: TestPrint()

        '''
        try:
            # assume the user is using IDLE
            import sys
            self._color = sys.stdout.shell
            self._mode = 'IDLE'
        except AttributeError:
            # using a standard terminal, not IDLE
            self._mode = 'TERM'

    def test_success(self, test_name):
        ''' Prints test_name with a coloured PASS qualifier.

        TestPrint.test_success(str) -> None

        '''
        self.test_eval(test_name, 'PASS')

    def test_failure(self, test_name):
        ''' Prints test_name with a coloured FAIL qualifier.

        TestPrint.test_failure(str) -> None

        '''
        self.test_eval(test_name, 'FAIL')

    def test_error(self, test_name):
        ''' Prints test_name with a coloured ERROR qualifier.

        TestPrint.test_error(str) -> None

        '''
        self.test_eval(test_name, 'ERROR')

    def test_eval(self, test_name, success_state):
        ''' Prints test_name and success state in a standardised format.

        success_state 

        '''
        ss = TestPrint.ColourMap[self._mode][success_state]
        if self._mode == 'TERM':
            # use ANSI escape codes to print desired colour
            print('  {0:<45}\033[0;{1};40m{2}\033[0;32;0m'.format(test_name, ss,
                    success_state))
        else:
            # mode must be IDLE, use sys.stdout.shell to write standard colours
            a = self._color.write('  {0:<45}'.format(test_name), 'stdout')
            a = self._color.write(success_state+'\n', ss)

    @staticmethod
    def print_section(section):
        ''' Prints a section heading for the specified section.

        Heading is an 80-character line of #---- section ----#

        TestPrint.print_section(str) -> None

        '''
        section = ' ' + section + ' '
        symbols = 78 - len(section)
        if symbols % 2:
            before = '-' * ((symbols // 2) + 1)
            after = '-' * (symbols // 2)
        else:
            before = after = '-' * (symbols // 2)
        print('#' + before + section + after + '#\n')

    @staticmethod
    def section_end(num_tests, passes, failures, errors):
        ''' Prints a section summary and ending for the given results.

        TestPrint.section_end(int, int, int, int) -> None

        '''
        # correct print output for single cases
        if passes == 1: ps = 'pass'
        else: ps = 'passes'
        if failures == 1: fs = 'failure'
        else: fs = 'failures'
        if errors == 1: es = 'error'
        else: es = 'errors'

        print('\nRan {} tests, with {} {}, {} {}, and {} {}.'.format(
            num_tests, passes, ps, failures, fs, errors, es))
        print('#' + '-'*78 + '#')

                
if __name__ == '__main__':
    # test running tests
    class TestRun2(TestRun):
        def test_1(self):
            assert 1 == 1, "1 != 1" # should PASS
        def test_2(self):
            assert 1 == 2, "1 != 2" # should FAIL
        def test_3(self):
            assert 1/0 == 1, "1/0 != 1" # should ERROR (ZeroDivisionError)

    TestRun2().run_tests(verbose=True)
    
