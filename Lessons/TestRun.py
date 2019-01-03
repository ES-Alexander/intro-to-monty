#!/usr/bin/env python3

################################################################################
#                                                                              #
#                               Testing Module                                 #
#                                                                              #
###--------------------------------------------------------------------------###
#                                                                              #
# Author: ES Alexander                                                         #
# Released: 2018-12-26                                                         #
#                                                                              #
# Feel free to use and modify as you wish, but keep this header and add a note #
#   specifying how it has been modified from the original, the last date it    #
#   was modified, and who modified it.                                         #
#                                                                              #
# Do not attempt to sell this testing module. If planning to use commercially, #
#   or sell tests derived from the module, please contact the original author  #
#   at 'sandman.esalexander@gmail.com'.                                        #
#                                                                              #
###--------------------------------------------------------------------------###
#                                                                              #
# Modified: 2019-03-01                                                         #
# Author: ES Alexander                                                         #
#                                                                              #
# Added stream redirection (and logging) functionality for filestreams.        #
#                                                                              #
################################################################################

import traceback # controlled printing of tracebacks (from caught Exceptions)
import multiprocessing # used for automatic timeouts (not available in IDLE)
import time # used for measuring test times and user-generated timeouts
import sys # used for shell io functionality

class TestRun(object):
    ''' A class for running tests. '''

    PASS = 1
    FAIL = 0
    ERROR = -1
    TIMEOUT = -2
    
    def __init__(self, timeout=5, log_func=None):
        ''' A class for running tests and printing relevant output.

        Tests should be in a class which inherits from TestRun, and can be run
            by instantiating that class and running run_tests(), or run_test().
            Both running methods take a boolean for verbosity, which defaults to
            False for multiple tests and True for single tests. 'run_tests'
            has an argument 'methods' which allows specifying a set of desired
            test methods to run (defaults to all).

        Test methods should be instance methods of the class, and should begin
            with 'test_'. The test component should be an assert statement,
            preferably with failure reasoning provided as the second argument,
            e.g.:
                    assert 1 == 2, '1 is not equal to 2'

        'timeout' is the default number of seconds after which a test is
            terminated as 'timed out'. Due to processing issues with interactive
            debuggers, AUTOMATIC TIMEOUTS CANNOT BE IMPLEMENTED IN IDLE. If a
            test stalls while running from IDLE (or more generally), pressing
            CTRL+C to trigger a KeyboardInterrupt is treated as a TIMEOUT of
            that test, and the remaining tests are run.

        'log_func' is a logging function used as an override for shell.write
            when running in IDLE. Leave as None if not running in IDLE.
            
        Constructor: TestRun(*int)

        '''
        # initialise instance variables
        self._TP = TestPrint(log_func)
        self._timeout = timeout
        self._last_failed = []

        # update test method docstrings with run information
        for method_name in self.get_test_methods():
            method = eval('self.' + method_name)
            method.__func__.__doc__ += \
                    '\n\nself.run_test({!r}) -> None\n\n'.format(method_name)

    def get_test_methods(self):
        ''' Returns the available test methods in this class.

        Test methods should begin with 'test_', and return None.

        self.get_test_methods() -> list[str]

        '''
        return [m for m in dir(self) if m.startswith('test_')]

    def run_tests(self, methods=[], section='', verbose=False, timeout=None):
        ''' Runs the specified methods at the given verbosity.

        'methods' is a list of the test methods to run. If left empty all the
            tests in the class are run (in sorted order, not defining order).

        'section' is the name of the section currently being tested. If left
            empty defaults to the name of the testing class.

        'verbose' is a boolean specifying verbosity. If True, any tests which
            fail will print their failure reason (the string provided as the
            second argument of the assert statement (assert bool, str)), and
            any tests which raise exceptions will print their traceback.

        'timeout' is the number of seconds after which a test is terminated as
            'timed out'. If left as None, it is set to the instance default
            timeout value. AUTOMATIC TIMEOUTS CANNOT BE IMPLEMENTED IN IDLE
            (see __init__ docs).

        self.run_tests(*list, *str, *bool, *int) -> None
        
        '''
        if not section:
            section = type(self).__name__
        self._TP.print_section(section)
        self._print_IDLE_warning() # timeout warning for IDLE users
            
        self._last_failed = []
        
        if not methods:
            # default to run all methods
            methods = self.get_test_methods()
        
        # initialise counts
        num_tests = len(methods)
        passes = 0; failures = 0; errors = 0; timeouts = 0

        start = time.time()

        # run the specified methods
        for method in methods:
            result = self.run_test(method, verbose, timeout) # run the test
            # increment the relevant count
            if result == TestRun.PASS:
                passes += 1
            elif result == TestRun.FAIL:
                self._last_failed += [method]
                failures += 1
            elif result == TestRun.ERROR:
                self._last_failed += [method]
                errors += 1
            elif result == TestRun.TIMEOUT:
                self._last_failed += [method]
                timeouts += 1

        duration = time.time() - start
        # print an output specifying results and the end of the section
        self._TP.section_end(num_tests, duration, passes, failures, errors,
                             timeouts)

    def run_failed_tests(self, timeout=None):
        ''' Runs all tests from the last test run which did not pass.

        Tests are run in verbose mode to display reasoning.

        If no tests were failed in the last run, or there have been no previous
            runs, all tests are run.

        'timeout' is the number of seconds after which a test is terminated as
            'timed out'. If left as None, it is set to the instance default
            timeout value. AUTOMATIC TIMEOUTS CANNOT BE IMPLEMENTED IN IDLE
            (see __init__ docs).

        self.run_failed_tests(*int) -> None

        '''
        self.run_tests(self._last_failed, 'Last Failed Tests', True, timeout)

    def run_test(self, test_name, verbose=True, timeout=None):
        ''' Returns the success state of running test_name.

        Return values are within the set [TestRun.PASS, TestRun.FAIL,
            TestRun.ERROR].

        'test_name' should be an instance method of the running class.

        'verbose' is a boolean specifying verbosity. If True, a failing test
            will print its failure reason (the string provided as the
            second argument of the assert statement (assert bool, str)), and
            a test which raises an exception will print its traceback.

        'timeout' is the number of seconds after which a test is terminated as
            'timed out'. If left as None, it is set to the instance default
            timeout value. AUTOMATIC TIMEOUTS CANNOT BE IMPLEMENTED IN IDLE
            (see __init__ docs).

        self.run_test(str, *bool, *int) -> int

        '''
        if not timeout:
            timeout = self._timeout

        start = time.time()
        try:
            if self._TP.mode == 'TERM':
                # only auto-check for timeout if not in IDLE
                p = multiprocessing.Process(name = test_name,
                    target = self.timeout_check, args=(test_name,))
                p.start(); p.join(timeout)  # check for timeout
                if p.is_alive():
                    p.terminate(); p.join() # automatic timeout has occurred
                    self._TP.test_timeout(test_name)
                    if verbose:
                        print('    Automatic timeout after {}'.format(timeout),
                              'seconds\n')
                    return TestRun.TIMEOUT
            exec('self.{}()'.format(test_name)) # run the function normally
            self._TP.test_success(test_name)    # test succeeded if no errors
            #if verbose: print()                 # add a line between tests
            return TestRun.PASS
        except AssertionError as e:
            self._TP.test_failure(test_name)    # test failed
            if verbose:
                print('    ' + str(e) + '\n')
            return TestRun.FAIL
        except KeyboardInterrupt:
            # User-specified timeout of test occurred
            duration = time.time() - start
            self._TP.test_timeout(test_name)
            if verbose:
                print('    User-generated timeout after',
                      '{:.2f} seconds\n'.format(duration))
            return TestRun.TIMEOUT
        except Exception as e:
            self._TP.test_error(test_name)      # unknown error occurred
            if verbose:
                traceback.print_tb(e.__traceback__)
                print('    {}: {}'.format(type(e).__name__, str(e)) + '\n')
            return TestRun.ERROR
        
    def timeout_check(self, test_name):
        ''' Run the given method without no consequences, for runtime testing.

        self.timeout_check(str) -> None

        '''
        try:
            exec('self.{}()'.format(test_name))
        except (Exception, KeyboardInterrupt):
            return

    def _print_IDLE_warning(self):
        ''' Prints a warning about disabled timeouts to IDLE users.

        self._print_IDLE_warning() -> None

        '''
        if self._TP.mode == 'IDLE':
            c_print = self._TP._colour.write # colour write function for IDLE
            c_print('Tests running in IDLE:\n', 'ERROR')
            c_print('  ->', 'stdout')
            c_print(' Automatic timeouts DISABLED\n', 'DEFINITION')
            c_print('  -> Use ', 'stdout')
            c_print('CTRL+C', 'BUILTIN')
            c_print(' to cause user-generated timeouts when tests are taking '+\
                    'too long.\n\n', 'stdout')
                

class TestPrint(object):
    ''' A class for printing test success states. '''
    # Terminal/IDLE colour specifier
    ColourMap = {'TERM':
                 {'ERROR':35, 'TIMEOUT':34, 'PASS':32, 'FAIL':31, 'STD':0},
                 'IDLE':
                 {'ERROR':'BUILTIN', 'TIMEOUT':'DEFINITION', 'PASS':'STRING',
                  'FAIL':'COMMENT', 'STD':'stdout'}
                }
    
    def __init__(self, cprint=None):
        ''' A class for printing coloured, formatted test success states.

        Implements behaviour for both IDLE and a standard terminal.

        'cprint' is an override function for shell.write in IDLE. Can be used
            for logging purposes.

        Constructor: TestPrint(func)

        '''
        if cprint is not None:
            class Colour(object):
                def __init__(self, func):
                    self.write = func
            
            self._colour = Colour(cprint)
            self.mode = 'IDLE'
            return
        
        try:
            # assume the user is using IDLE
            self._colour = sys.stdout.shell
            self.mode = 'IDLE'
        except AttributeError:
            # using a standard terminal, not IDLE
            self.mode = 'TERM'

    def test_success(self, test_name):
        ''' Prints test_name with a coloured PASS qualifier.

        self.test_success(str) -> None

        '''
        self.test_eval(test_name, 'PASS')

    def test_failure(self, test_name):
        ''' Prints test_name with a coloured FAIL qualifier.

        self.test_failure(str) -> None

        '''
        self.test_eval(test_name, 'FAIL')

    def test_error(self, test_name):
        ''' Prints test_name with a coloured ERROR qualifier.

        self.test_error(str) -> None

        '''
        self.test_eval(test_name, 'ERROR')

    def test_timeout(self, test_name):
        ''' Prints test_name with a coloured TIMEOUT qualifier.

        self.test_timeout(str) -> None

        '''
        self.test_eval(test_name, 'TIMEOUT')

    def test_eval(self, test_name, success_state):
        ''' Prints test_name and success state in a standardised format.

        success_state 

        '''
        ss = TestPrint.ColourMap[self.mode][success_state]
        if self.mode == 'TERM':
            # use ANSI escape codes to print desired colour
            print('  {0:<45}\033[0;{1};40m{2}\033[0;32;0m'.format(test_name, ss,
                    success_state))
        else:
            # mode must be IDLE, use sys.stdout.shell to write standard colours
            a = self._colour.write('  {0:<45}'.format(test_name), 'stdout')
            a = self._colour.write(success_state+'\n', ss)

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
        print('\n#' + before + section + after + '#\n')

    @staticmethod
    def section_end(num_tests, duration, passes, failures, errors, timeouts):
        ''' Prints a section summary and ending for the given results.

        TestPrint.section_end(int, float, int, int, int, int) -> None

        '''
        # correct print output for single cases
        if passes == 1: ps = 'pass'
        else: ps = 'passes'
        if failures == 1: fs = 'failure'
        else: fs = 'failures'
        if errors == 1: es = 'error'
        else: es = 'errors'
        if timeouts == 1: ts = 'timeout'
        else: ts = 'timeouts'

        print('\nRan {} tests, with {} {}, {} {}, {} {}, and {} {}.'.format(
            num_tests, passes, ps, failures, fs, errors, es, timeouts, ts))
        print('Testing took {:.3f}s'.format(duration))
        print('#' + '-'*78 + '#\n')
        

class Redirect(object):
    ''' Redirect a stream to one or more places. '''
    # Inspiration: https://stackoverflow.com/q/616645
    def __init__(self, in_stream, *out_streams, maintain=True):
        ''' Mimic the functionality of the Unix 'Tee' command.

        Reads data from in_stream and writes it to all streams in out_streams.
            By default, out_streams includes in_stream unless 'maintain' is
            set to False.

        Constructor: Redirect(stream, *streams, **bool)

        '''
        # store 'maintain' state internally
        self._maintain = maintain
        
        self.in_stream = in_stream
        self.__dict__.update(in_stream.__dict__)

        # determine appropriate state
        self.state = None
        if in_stream is sys.stdout:
            sys.stdout = self
            self.state = 'stdout'
        elif in_stream is sys.stderr:
            sys.stderr = self
            self.state = 'stderr'

        # attempt to redirect IDLE direct shell writes
        try:
            self._shell_write = self.in_stream.shell.write
            self.in_stream.write = self.shell_write
        except AttributeError:
            # not using IDLE
            self._shell_write = self.shell_write = None

        # determine the lists of output streams
        self._out_streams = list(out_streams)
        self.ext_streams = len(self._out_streams)
        if maintain:
            self._out_streams += [self.in_stream]
            if self.state is None:
                self.ext_streams += 1

    def __del__(self):
        ''' Clean up the streams in use. '''
        self.close()

    def __enter__(self):
        ''' Initialisation functionality for usage in 'with' statements.

        Only works if in_stream is stdout/stderr.

        '''
        pass

    def __exit__(self, *args):
        ''' Cleanup functionality for usage in 'with' statements.

        Only works if in_stream is stdout/stderr.

        '''
        self.close()

    def write(self, message):
        ''' Wrapper function for 'write', to output to all desired streams. '''
        if self._shell_write is None:
            for stream in self._get_open_streams():
                stream.write(message)
        else:
            self.shell_write(message, self.state)

    def shell_write(self, message, *args, **kwargs):
        ''' Wrapper function for IDLE's shell.write. '''
        for stream_id in range(self.ext_streams):
            stream = self._out_streams[stream_id]
            if stream is not None:
                stream.write(message)

        self._shell_write(message, *args, **kwargs)

    def flush(self):
        ''' Wrapper for stream flush - flush all streams. '''
        for stream in self._get_open_streams():
            stream.flush()
            #os.fsync(stream.fileno()) # unsure if necessary

    def _get_open_streams(self):
        ''' Get the currently open streams. '''
        return [stream for stream in self._out_streams if stream is not None]

    def replace_stream(self, stream_id, stream):
        ''' Replace the stream at 'stream_id' with stream.

        Can be used to re-open a closed stream by opening the same file in
            append mode, and inputting that stream.

        '''
        if stream_id < self._ext_streams:
            self._out_streams[stream_id] = stream

    def close(self, *streams):
        ''' Close all streams, or the streams specified by *streams indices. '''
        if streams:
            for stream_id in streams:
                if stream_id < self._ext_streams:
                    stream = self._out_streams[stream_id]
                    if stream is not None:
                        stream.close()
                        self._out_streams[stream_id] = None
            return

        # streams unspecifed - clean up all streams and close as necessary
        # restore stdout/stderr where possible
        if self.state is not None:
            if self.state == 'stdout':
                sys.stdout = self.in_stream
            elif self.state == 'stderr':
                sys.stderr = self.in_stream
            self.in_stream = None

        for index in range(self.ext_streams):
            stream = self._out_streams[index]
            if stream is not None:
                stream.close()
                self._out_streams[index] = None
                
if __name__ == '__main__':
    # test a basic testing suite
    
    # initial definitions
    a = 2

    # test definitions
    class ExampleTests(TestRun):
        ''' A class of tests used for displaying the test module behaviour. ''' 
        def test_a_value(self):
            ''' Testing if a is 1. '''
            assert a == 1, "'a' should have been 1, but was {}".format(a)

        def test_b_type(self):
            ''' Testing if 'b' is a dictionary. '''
            assert type(b) is dict, "'b' is supposed to be a dictionary"

        def test_a_type(self):
            ''' Testing if 'a' is an integer. '''
            assert type(a) is int, "'a' is supposed to be an integer"

        def test_timeout(self):
            ''' Testing timeout behaviour of test module. '''
            while True:
                continue

    log_file = open('log.txt','w')
    Log = Redirect(sys.stdout, log_file)

    # run tests
    Tests = ExampleTests(log_func=Log.shell_write)
    Tests.run_tests()

    # run failed tests again with explanation
    Tests.run_failed_tests()

    if Tests._TP.mode == 'IDLE':
        print("\nExample 'help' output from auto-set docstring:")
        help(Tests.test_a_value)

    Log.close() # stop logging stdout
    
    # print the logged output
    print('Logging stored the following:\n')
    
    with open('log.txt','r') as f:
        print(f.read())
    import os
    os.remove('log.txt') # delete the log file
