#!/usr/bin/env python3

################################################################################
#                                                                              #
#                               Testing Module                                 #
#                                                                              #
###--------------------------------------------------------------------------###
#                                                                              #
# Author: ES Alexander                                                         #
# Released: 2019-02-11                                                         #
#                                                                              #
# This module is exempt from any external license it is provided with, and is  #
#   instead provided under the modified MIT license below:                     #
#                                                                              #
# Copyright 2019 ES Alexander                                                  #
#                                                                              #
# Permission is hereby granted, free of charge, to any person obtaining a copy #
# of this software and associated documentation files (the "Software"), to     #
# deal in the Software without restriction, including without limitation the   #
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or  #
# sell copies of the Software, and to permit persons to whom the Software is   #
# furnished to do so, subject to the following conditions:                     #
#                                                                              #
# The above header, the above copyright notice, this permission notice, and a  #
# note specifying how the module has been modified from the original shall be  #
# included in all copies or substantial portions of the Software.              #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
###--------------------------------------------------------------------------###
#                                                                              #
# This testing module is intended for small-scale testing of python, including #
#   in IDLE. Notable features include:                                         #
#                                                                              #
#       'TestRun': A base class for a test-suite, including automatic test-    #
#           detection (for methods beginning with 'test_'), running all        #
#           available tests or a specified set with 'run_tests', running the   #
#           tests which failed in the last run with 'run_failed_tests', and    #
#           automatic (not in IDLE) and user-generated timeouts while testing. #
#                                                                              #
#       'TestGroup': A class for grouping multiple TestRun instances as though #
#           they are a single instance.                                        #
#                                                                              #
#       'Redirect': A class for stream redirection and multiplication, focused #
#           on stdin, stdout, and stderr, but also usable for general file     #
#           streams. Allows for capturing printed output and simulating typed  #
#           input while testing.                                               #
#                                                                              #
#       'MultiRedirect': A class for managing multiple redirections, allowing  #
#           for methods to be run simultaneously run on all stored             #
#           redirections.                                                      #
#                                                                              #
###--------------------------------------------------------------------------###
#                                                                              #
# Modified: YYYY-MM-DD                                                         #
# Author: _                                                                    #
#                                                                              #
# Modification details                                                         #
#                                                                              #
################################################################################

import traceback # controlled printing of tracebacks (from caught Exceptions)
import multiprocessing # used for automatic timeouts (not available in IDLE)
import time      # used for measuring test times and user-generated timeouts
import sys       # used for shell io functionality (stream redirections)
import os        # for creating folders if necessary

class TestRun(object):
    ''' A class for running tests. '''

    PASS = 1
    FAIL = 0
    ERROR = -1
    TIMEOUT = -2
    
    def __init__(self, timeout=5):
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
            
        Constructor: TestRun(*int)

        '''
        # initialise instance variables
        self._TP = TestPrint()
        self._timeout = timeout
        self._last_failed = []

        # update test method docstrings with run information
        for method_name in self.get_test_methods():
            method = eval('self.' + method_name)
            method.__func__.__doc__ += \
                    '\n\nself.run_test({!r}) -> None\n\n'.format(
                        method_name)

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
        
        if passes == 0 and methods == self.get_test_methods():
            print("  Run 'help({})'".format(type(self).__name__),
                  "to find out more about this test suite.", file=sys.stderr)
            
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
            TestRun.ERROR, TestRun.TIMEOUT].

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

        if self._TP.mode == 'TERM':
            # only auto-check for timeout if not in IDLE
            # set up a pipe for the result
            recv_end, send_end = multiprocessing.Pipe(False)
            # set up the test function for running
            p = multiprocessing.Process(name = test_name,
                target = self._run_test, args=(test_name,verbose,timeout,
                                               send_end))
            # run and check for timeout
            p.start(); p.join(timeout)
            
            if p.is_alive():
                p.terminate(); p.join() # automatic timeout has occurred
                self._TP.test_timeout(test_name)
                if verbose:
                    print('    Automatic timeout after {}'.format(timeout),
                          'seconds\n')
                return TestRun.TIMEOUT
            # test completed without timeout
            return recv_end.recv() # extract and return result
        else:
            # run the test with only user-generated timeouts
            return self._run_test(test_name, verbose, timeout)
                
    def _run_test(self, test_name, verbose, timeout, send_end=None):
        ''' Returns the result of running test_name with the given parameters.

        If send_end is specified, sends the result via the result pipe.

        self._run_test(str, bool, int, pipe) -> str/None

        '''
        start = time.time()
        self._TP.test_run(test_name)
        try:
            exec('self.{}()'.format(test_name)) # run the function normally
            self._TP.test_result('PASS')        # test succeeded if no errors
            if send_end: send_end.send(TestRun.PASS)
            return TestRun.PASS
        except (AssertionError,NameError) as e:
            self._TP.test_result('FAIL')        # test failed
            if verbose: print('    ' + str(e) + '\n')
            if send_end: send_end.send(TestRun.FAIL)
            return TestRun.FAIL
        except KeyboardInterrupt:
            # User-specified timeout of test occurred
            duration = time.time() - start
            self._TP.test_result('TIMEOUT')
            if verbose:
                print('    User-generated timeout after',
                      '{:.2f} seconds\n'.format(duration))
            if send_end: send_end.send(TestRun.TIMEOUT)
            return TestRun.TIMEOUT
        except Exception as e:
            self._TP.test_result('ERROR')       # unknown error occurred
            if verbose:
                traceback.print_tb(e.__traceback__)
                print('    {}: {}'.format(type(e).__name__, str(e)) + '\n',
                      file=sys.stderr)
            if send_end: send_end.send(TestRun.ERROR)
            return TestRun.ERROR

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
    
    def __init__(self):
        ''' A class for printing coloured, formatted test success states.

        Implements behaviour for both IDLE and a standard terminal.

        Constructor: TestPrint(func)

        '''
        try:
            # assume the user is using IDLE
            self._colour = sys.stdout.shell
            self.mode = 'IDLE'
        except AttributeError:
            # using a standard terminal, not IDLE
            self.mode = 'TERM'

    def test_result(self, success_state):
        ''' Prints success state in a standardised format.

        success_state can be one of 'PASS', 'FAIL', 'ERROR' or 'TIMEOUT'.

        self.test_result(str) -> None

        '''
        ss = TestPrint.ColourMap[self.mode][success_state]
        if self.mode == 'TERM':
            # use ANSI escape codes to print desired colour
            print('\033[0;{};40m{}\033[0;32;0m'.format(ss, success_state))
        else:
            # mode must be IDLE, use sys.stdout.shell to write standard colours
            a = self._colour.write(success_state + '\n', ss)

    @staticmethod
    def test_run(test_name):
        ''' Prints the test name in a standardised format.

        TestPrint.test_run(str) -> None

        '''
        print('  {0:<45}'.format(test_name), end='')

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


class Emulator(object):
    ''' A class for holding multiple instances and emulating one. '''
    # Inspiration: https://stackoverflow.com/q/616645 (shx2)
    def __init__(self, default, *objs):
        ''' A class for holding and maintaining a group of objects.

        Takes the place of a single instance and runs all called methods on all
            stored instances. Keyword-argument 'runs' can be set to a tuple
            of classes to limit which obj(s) to run the calls on. By default,
            runs is set to 'default' - generally used as the highest
            superclass common to all stored objs. Keyword-argument 'ids' can be
            set to a tuple of indices of the stored objs, to limit which
            obj(s) to run calls on. By default, ids is set to all ids in objs.
            Methods are called only on classes which match both 'runs' and 'ids'
            criteria.
            
        All methods are the same as those for a stored object in objs, with
            the addition of the 'runs' and 'ids' arguments in each. If both
            'runs' and 'ids' are unspecified, methods should only be called that
            are common to all stored objs.

        Constructor: Emulator(superclass, *objs)

        '''
        self._default = default
        self._objs = objs
        
    def __getattr__(self, attr, *args):
        ''' Wraps called methods with _wrap function (+ 'runs', 'ids'). '''
        return self._wrap(attr, *args)
    
    def _wrap(self, attr, *args):
        ''' Calls requested method on all stored instances that match at least
            one class in 'runs' and have their id (index) in 'ids'.
        '''
        def g(*a, runs=self._default, ids=range(len(self._objs)), **kw):
            res = None
            for index, obj in enumerate(self._objs):
                if isinstance(obj, runs) and index in ids:
                    res = getattr(obj, attr, *args)(*a, **kw)
            return res
        return g

        
class TestGroup(Emulator):
    ''' A class for grouping TestRun instances. '''
    
    def __init__(self, *test_runs):
        ''' A class for holding and maintaining a group of TestRun instances.

        Allows for running tests from all or select TestRuns, using the
            run_tests() method. Keyword-argument 'runs' can be set to a tuple
            of TestRun classes to determine which run(s) to run tests from. By
            default, runs is set to TestRun, which runs all runs. Keyword-
            argument 'ids' can be set to a tuple of indices of the stored
            TestRuns, to limit which run(s) to run tests from. By default, ids
            is set to all ids in objs. Tests are only run for instances which
            match both 'runs' and 'ids' criteria.

        All methods are the same as those for an instance of the TestRun class,
            with the addition of the 'runs' argument in each.

        Constructor: TestGroup(*TestRun)

        '''
        super().__init__(TestRun, *test_runs)


class Redirect(object):
    ''' Redirect a stream to one or more places. '''
    # Inspiration: https://stackoverflow.com/q/616645
    def __init__(self, in_stream, *out_streams, maintain=True):
        ''' Mimic the functionality of the Unix 'Tee' command.

        Redirects calls to in_stream to all streams in out_streams. By default,
            out_streams includes in_stream unless 'maintain' is set to False.

        Automatically restores on Redirect.close() for in_stream a standard
            system stream (sys.stdout, sys.stderr, sys.stdin), as in:

            Out = Redirect(sys.stdout, *out_streams, *maintain)
            <desired tracked code>
            Out.close() # close all out_streams, restore sys.stdout

        For non-standard in_streams, do:
            
            in_stream = Redirect(in_stream, *out_streams, *maintain)
            <desired tracked code>
            in_stream.close() # close all out_streams
            in_stream = in_stream.in_stream # restore original in_stream

        Constructor: Redirect(stream, *streams, **bool)

        '''
        self._maintain = maintain  # store 'maintain' state internally
        self.in_stream = in_stream # back up in_stream for later restoring

        # determine appropriate state (in_stream == system stream?)
        if in_stream is sys.stdout:
            try:
                # attempt to redirect IDLE direct shell writes
                self._shell = sys.stdout.shell
                self.IDLE_mode = True

                class Shell(object):
                    ''' Add stream.shell.write method for IDLE. '''
                    def __init__(self, func):
                        self.write = func
                self.shell = Shell(self.shell_write)
            except AttributeError:
                self.IDLE_mode = False # not using IDLE
            # redirect normal sys.stdout
            sys.stdout = self
            self.state = 'stdout'
        elif in_stream is sys.stderr:
            sys.stderr = self
            self.state = 'stderr'
        elif in_stream is sys.stdin:
            sys.stdin = self
            self.state = 'stdin'
        else:
            self.state = None

        # determine the list of output streams
        self._out_streams = list(out_streams)
        self.ext_streams = len(self._out_streams)
        if self._maintain:
            self._out_streams += [self.in_stream]
            if self.state is None:
                self.ext_streams += 1 # standard streams not counted

    def __del__(self):
        ''' Clean up the streams in use. '''
        self.close()

    def __enter__(self):
        ''' Initialisation functionality for usage in 'with' statements.

        Only works if in_stream is stdout/stderr/stdin.

        '''
        pass

    def __exit__(self, *args):
        ''' Cleanup functionality for usage in 'with' statements.

        Only works if in_stream is stdout/stderr/stdin.

        '''
        self.close()

    # read-mode stream functionality
    def read(self, size=-1):
        ''' Wrapper function for 'read', for accepting input from streams. '''
        ret = ''
        for stream in self._get_open_streams():
            if size > 0:
                extra = stream.read(size)
                ret += extra
                size -= len(extra)
                if size <= 0:
                    return ret
            else:
                ret += stream.read()
        return ret

    def readline(self, size=-1):
        ''' Wrapper function for 'readline', for multiple streams. '''
        for stream in self._get_open_streams():
            ret = stream.readline(size)
            if ret != '':
                return ret
        return ''

    def readlines(self, hint=-1):
        ''' Wrapper function for 'readlines', for multiple streams. '''
        ret = []
        for stream in self._get_open_streams():
            if hint > 0:
                extra = stream.readlines(hint)
                ret += extra
                hint -= sum(len(line) for line in extra)
                if hint <= 0:
                    return ret
            else:
                ret += stream.readlines() 
        return ret

    # write-mode stream functionality
    def write(self, message):
        ''' Wrapper function for 'write', to output to all desired streams. '''
        for stream in self._get_open_streams():
            stream.write(message)
        return len(message)

    def writelines(self, lines):
        ''' Wrapper function for 'writelines', for multiple streams. '''
        for line in lines:
            self.write(line)

    def shell_write(self, message, *args, **kwargs):
        ''' Wrapper function for IDLE's sys.stdXXX.shell.write. '''
        for stream_id in range(self.ext_streams):
            stream = self._out_streams[stream_id]
            if stream is not None:
                stream.write(message)
        if self._maintain:
            self._shell.write(message, *args, **kwargs)
        return len(message)

    # mode independent functionality
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
        if stream_id < self.ext_streams:
            self._out_streams[stream_id] = stream

    def close(self, *stream_ids):
        ''' Close all out_streams, or the streams specified by *stream_ids.

        'stream_ids' is an iterable of indices referring to the out_streams
            streams specified at initialisation (0 is the first out_stream).

        streams = [] -> also restores in_stream if one of stdin/stdout/stderr.

        '''
        if stream_ids:
            for stream_id in stream_ids:
                if stream_id < self.ext_streams:
                    stream = self._out_streams[stream_id]
                    if stream is not None:
                        stream.close()
                        self._out_streams[stream_id] = None
            return

        # streams unspecifed - clean up all streams and close as necessary
        # restore stdout/stderr/stdin if modified
        if None not in [self.in_stream, self.state]:
            if self.state == 'stdout':
                sys.stdout = self.in_stream
                if self.IDLE_mode:
                    assert sys.stdout.shell == self._shell, \
                           "shell should be restored!"
            elif self.state == 'stderr':
                sys.stderr = self.in_stream
            elif self.state == 'stdin':
                sys.stdin = self.in_stream
            self.in_stream = None

        for index in range(self.ext_streams):
            stream = self._out_streams[index]
            if stream is not None:
                stream.close()
                self._out_streams[index] = None
                
class MultiRedirect(Emulator):
    ''' A class for grouping Redirect instances. '''
    def __init__(self, *redirects):
        ''' A class for holding and maintaining a group of Redirect instances.

        Allows for maintaining a group of Redirect instances as connected -
            function calls are made to all stored instances. Keyword-argument
            'ids' can be set to a tuple of indices of the stored objs, to limit
            which Redirect(s) to run calls on. By default, ids is set to all ids
            in 'redirects'.

        All methods are the same as those for an instance of the Redirect class,
            with the addition of the 'ids' argument in each.

        Constructor: MultiRedirect(*Redirect)

        '''
        super().__init__(Redirect, *redirects)

if __name__ == '__main__':
    # test a basic testing suite
    
    # initial definitions
    a = 0

    # test definitions
    class ExampleTests(TestRun):
        ''' A class of tests used for displaying the test module behaviour. ''' 
        def test_a_value(self):
            ''' Testing if a is 1. '''
            assert a == 1, "'a' should have been 1, but was {}".format(a)

        def test_a_division(self):
            ''' Testing if 'a' is a factor of 10. '''
            assert 10 % a == 0, "'a' is supposed to be a factor of 10"

        def test_a_type(self):
            ''' Testing if 'a' is an integer. '''
            assert isinstance(a, int), "'a' is supposed to be an integer"

        def test_b_type(self):
            ''' Testing if 'b' is a dictionary. '''
            assert isinstance(b, dict), "'b' is supposed to be a dictionary"

        def test_timeout(self):
            ''' Testing timeout behaviour of test module. '''
            while True:
                continue

    class RedirectTests(TestRun):
        ''' A class of example tests using stream redirections. '''
        def __init__(self):
            ''' Initialise this test suite. '''
            super().__init__()
            self._in = 'test_files/in.txt'
            self._err = 'test_files/err.txt'
            self._out = 'test_files/out.txt'

        # test functions
        def test_stdin_stdout(self):
            ''' Testing stdin and stdout redirection (manual restore). '''
            # create input file with some basic text
            text = 'testing\ntesting\n1\n2\n3'
            with open(self._in,'w') as in_file:
                in_file.write(text)

            # redirect stdin to come from in.txt, ignore user input
            # redirect stdout to go to out.txt, do not display in shell
            IO = MultiRedirect(
                Redirect(sys.stdin, open(self._in,'r'), maintain=False),
                Redirect(sys.stdout, open(self._out,'w'), maintain=False))

            print(input()) # run some input/output

            # close in.txt and out.txt, and restore stdin and stdout
            #   (restore on close only works for standard system streams)
            IO.close()

            # check that the test was successful
            with open(self._out,'r') as out_file:
                with open(self._in,'r') as in_file:
                    assert out_file.read() == in_file.readline(), \
                           "{!r} should contain the first line of {!r}'".format(
                               self._out, self._in)

        def test_stdin_stderr(self):
            ''' Testing stdin and stderr redirection (auto restore). '''
            # create input file with some basic text
            text = 'testing\ntesting\n1\n2\n3'
            with open(self._in,'w') as in_file:
                in_file.write(text)

            # Set up automatically restored redirections (only for sys.std*)
            # redirect stdin to come from in.txt, ignore user input
            with Redirect(sys.stdin, open(self._in,'r'), maintain=False):
                 # redirect stdout to go to out.txt, do not display in shell
                with Redirect(sys.stderr, open(self._err,'w'), maintain=False):
                    print(input(), file=sys.stderr) # run some input/output

            with open(self._err,'r') as err_file:
                with open(self._in,'r') as in_file:
                    assert err_file.read() == in_file.readline(), \
                           "{!r} should contain the first line of {!r}".format(
                               self._err, self._in)

    # create a folder for the test files, if one doesn't already exist
    if not os.path.dirname('test_files'):
        os.mkdir('test_files')

    # first redirection (tests also internally redirect the same streams)
    log_out = 'test_files/logout.txt'; log_err = 'test_files/logerr.txt'
    Log = MultiRedirect(Redirect(sys.stdout, open(log_out,'w')),
                        Redirect(sys.stderr, open(log_err,'w')))

    # create test runs and run tests
    ET = ExampleTests(timeout=2) # create a test suite instance
    Tests = TestGroup(ET, RedirectTests()) # create a group of TestRuns
    Tests.run_tests() # run tests for all TestRuns in the group

    # run failed tests again with explanation (only check in ExampleTests)
    Tests.run_failed_tests(runs=ExampleTests)

    if ET._TP.mode == 'IDLE':
        print("\nExample 'help' output from auto-set docstring:")
        help(ET.test_a_value)

    Log.close() # close logging and restore stdout and stderr

    # display logged content
    log_out_head = \
             '#####--#####-----#####-----#####-----#####-----#####--#####\n' +\
             '#                                                         #\n' +\
             '#                     LOGGED OUTPUT:                      #\n' +\
             '#                                                         #\n' +\
             '#####--#####-----#####-----#####-----#####-----#####--#####\n'
    print(log_out_head)

    log_out = open(log_out)
    print(log_out.read())
    log_out.close()

    log_head = \
             '#####--#####-----#####-----#####-----#####-----#####--#####\n' +\
             '#                                                         #\n' +\
             '#                     LOGGED ERRORS:                      #\n' +\
             '#                                                         #\n' +\
             '#####--#####-----#####-----#####-----#####-----#####--#####\n'
    print(log_head, file=sys.stderr)
    
    log_err = open(log_err)
    print(log_err.read(), file=sys.stderr)
    log_err.close()
    
    
