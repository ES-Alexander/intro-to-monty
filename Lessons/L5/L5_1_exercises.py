#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following exercises below the appropriate   #
# comment, and click run when complete, using either the menu-bar at the top,  #
# or the F5 key on your keyboard.                                              #
################################################################################

'''
    Write a function which opens and reads a text file of questions, as well as
    opens and writes to a log file, also of txt format, recording the questions
    and answers. These files should be accepted as filenames, as parameters to
    your function. The first questions to be asked should always be "What is
    your name?", and "How old are you?", values for which should be stored as
    appropriate variables, with a formatted string printed after these two
    questions stating 'Your name is __ and you are __ years old.'

    After this, questions can be selected at random from the list of questions.
    Random selection can be accomplished by reading the question file into a
    list (each line is one question), and using the random module to determine
    which index of the list is accessed. No question should be asked more than
    once, and you can assume the question file will not include duplicate
    questions, will always exist, and will always have at least one question.
    Every question will be followed by a newline character in the file.

    Users should be prompted to answer questions beneath where they are asked,
    with a gap between each response and the subsequent question,  e.g.
    
    question_asker('questions.txt', 'my_log.txt')
        What is your name?
        Monty Python
        
        How old are you?
        42
        
        Your name is Monty Python and you are 42 years old.
        
        QN?
        AN
        
        ...
        
    This should also be the format of the log file, except without the gaps
    between questions, and the 'Your name is ...' statement should not be
    logged. Multiple calls to question_asker should overwrite the log file, not
    append to it.

    If the user responds to a question with just the word 'exit', that question
    should not be logged, and the question asker should stop asking questions
    and close the relevant files (this can only be done after the first two
    required questions have been asked). There should be no empty line after a
    valid 'exit' response.

    Feel free to add additional helper methods if you want to split up the
    functionality - just make sure that running the 'question_asker' function
    performs as specified.
'''

import random

def question_asker(q_file, log_file):
    ''' docstring '''
    pass # your code here





'''
    When you're done, click Run or F5 to check that you've followed the
    instructions. Example solutions can be found at the bottom of the exercise
    checker file.

    The code below isn't for editing, it's used to run the test file when this
    program is run.
'''

if __name__ == '__main__':
    # import and set up the tests
    from L5_2_exercise_checker import L5Tests
    L5Tests = L5Tests()
    
    # run the tests (with feedback)
    L5Tests.run_tests(verbose=True)
    # Once tests are run, data files used for testing can be found in the
    #   'test_files' folder. Test-inputs can be found in 'in.txt', questions can
    #   be found in 'qs.txt', and logging can be found in 'log.txt'. 'out.txt'
    #   contains the output that would normally be printed (without input
    #   values). Note that 'log.txt' and 'out.txt' are not for the full set of
    #   tests - just the last test that was run that used them.
