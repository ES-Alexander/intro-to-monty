#!/usr/bin/env python3
################################################################################
# This file contains tests for the L5_1_exercises.py file.                     #
################################################################################

import sys; sys.path.append('..')
from TestRun import TestRun, Redirect, MultiRedirect

import os
if not os.path.exists('test_files'):
    os.mkdir('test_files')

class L5Tests(TestRun):
    def __init__(self):
        ''' Initialise this test suite. '''
        super().__init__()

        # create input file
        self._inputs = ['exit','10','exit'] # immediate exit (on 2, not 0)
        self._inputs += ['Name','10','1','2','3','exit'] # random exit
        self._inputs += ['Name','10','1','2','3','4']    # finish questions
        self._in_file = 'test_files/in.txt'
        with open(self._in_file,'w') as in_file:
            in_file.write('\n'.join(self._inputs) + '\n')
        
        # create question file
        self._qs = ['Hmm?', 'And I should care why?', '???', 'No...?']
        self._q_file = 'test_files/qs.txt'
        with open(self._q_file,'w') as q_file:
            q_file.write('\n'.join(self._qs) + '\n')

        # store file names for logging and printed output
        self._out_file = 'test_files/out.txt'
        self._log_file = 'test_files/log.txt'

    # helper methods
    def _run_qs(self, n):
        ''' Runs the question_asker n times with redirected IO. '''
        # redirect standard IO
        IO = MultiRedirect(Redirect(sys.stdin, open(self._in_file)),
            Redirect(sys.stdout, open(self._out_file,'w'), maintain=False))

        try:
            for i in range(n):
                question_asker(self._q_file, self._log_file)
        finally:
            IO.close()

    def _general_exit(self, n):
        ''' Tests that exiting occurs correctly for n runs of input. '''
        num = [7, 7+13, 7+13+14] # expected number of lines of printing
        self._run_qs(n)

        with open(self._out_file) as out:
            num_lines = len(out.readlines())
            assert num_lines == num[n-1], 'question_asker should exit '   +\
                   "after the first 'exit' command received after the "   +\
                   'first two questions. (Look at qs.txt for test-cases)'

    def _general_logging(self, n, r, e):
        ''' Logging test for n runs, r response offset, and e+2 questions.

        A 'question' is counted as one which should validly be logged (not
            one which is responded to with 'exit').

        '''
        self._run_qs(n)

        with open(self._log_file) as log:
            name_q = log.readline()
            assert name_q == 'What is your name?\n', 'First question should ' +\
                   "be 'What is your name?', not '{}'.".format(name_q.rstrip())

            self._response(log.readline(), r)
            
            age_q = log.readline()
            assert age_q == 'How old are you?\n', 'Second question should '  +\
                   "be 'How old are you?', not '{}'.".format(age_q.rstrip()) +\
                   "\n('exit' should only work after the first two questions)"

            self._response(log.readline(), r+1)

            for i in range(e):
                self._q(log.readline(), r+2+i)
                self._response(log.readline(), r+2+i)

            assert log.readline() == '', 'Question and response should not ' +\
                   "be logged for an 'exit' response."

    def _response(self, response, n):
        ''' Checks if nth input == response. '''
        assert response == self._inputs[n] + '\n', 'Log file should log ' +\
                   'all questions and their responses (before a valid exit).'

    def _q(self, question, n):
        ''' Checks if question is expected (from qs.txt). '''
        assert question != '\n', 'Log file should not contain empty lines.'
        assert question.rstrip() in self._qs, 'Question listed does not ' +\
               'match any expected questions ({!r}).'.format(question.rstrip())

    @staticmethod
    def line_between(line):
        ''' Checks if line is empty. Raises AssertionError on failure. '''
        assert line == '\n', 'Responses should be on the next line to ' +\
                   'the question, with an empty line before the next question.'

    # test functions
    def test_startup(self):
        ''' Tests the printed output for qs 1 and 2, and the confirmation. '''
        self._run_qs(1)

        with open(self._out_file) as out:
            name_q = out.readline()
            assert name_q == 'What is your name?\n', 'First question should ' +\
                   "be 'What is your name?', not '{}'.".format(name_q.rstrip())
            
            self.line_between(out.readline())

            age_q = out.readline()
            assert age_q == 'How old are you?\n', 'Second question should '  +\
                   "be 'How old are you?', not '{}'.".format(age_q.rstrip()) +\
                   "\n('exit' should only work after the first two questions)"

            self.line_between(out.readline())

            confirm = out.readline()
            correct = 'Your name is {} and you are {} years old.\n'.format(
                self._inputs[0], self._inputs[1])
            assert confirm == correct, 'Confirmation should take the form: ' +\
                   "{!r}, not {!r}".format(correct.strip(), confirm.strip())

    def test_exit_1(self):
        ''' Tests printed output for the immediate exit case. '''
        self._general_exit(1)

    def test_exit_2(self):
        ''' Tests printed output for a general exit case. '''
        self._general_exit(2)

    def test_exit_3(self):
        ''' Tests printed output for a completion case (no more questions). '''
        self._general_exit(3)

    def test_logging_1(self):
        ''' Tests logging for the immediate exit case. '''
        self._general_logging(1,0,0)

    def test_logging_2(self):
        ''' Tests logging for a general exit case. '''
        self._general_logging(2,3,3)

    def test_logging_3(self):
        ''' Tests logging for a completion case (no more questions). '''
        self._general_logging(3,9,4)
            

        


#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':

    from random import randrange

    def question_asker(q_file, log_file):
        ''' Asks questions found in q_file and records answers in log_file.

        'q_file': a filename specifying a file of 1 or more questions, with
            one question per line and no repetitions.
        'log_file': a filename for where to log asked questions and their
            recorded responses.

        Asks for name and age, before printing a formatted string of form:
            'Your name is __ and you are __ years old.'
        Subsequently, asks questions at random from q_file (with no repeats)
            until no questions remain.

        Responding to a question with 'exit' quits the questioning session.

        question_asker(str'filename.txt', str'filename.txt') -> None
        
        '''
        questions = ['What is your name?\n', 'How old are you?\n']
        with open(q_file) as qs:
            # extract the questions and randomise their order, add to list
            questions += shuffle(qs.readlines())

        with open(log_file, 'w') as log:
            responses = []
            for question in questions:
                responses += [input(question)]
                if len(responses) > 2 and responses[-1] == 'exit':
                    break
                log.write(question + responses[-1] + '\n')
                if len(responses) == 2:
                    print('\nYour name is {} and you are {} years old.'.format(
                        responses[0], responses[1]))
                    
                print()

    def shuffle(shuffle_list):
        ''' Returns the inputted list in a random order.

        shuffle(list) -> list

        '''
        out_list = []
        while len(shuffle_list) > 0:
            out_list += [shuffle_list.pop(randrange(0,len(shuffle_list)))]
        return out_list

    Tests = L5Tests()
    Tests.run_tests(verbose=True)
