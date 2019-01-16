#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following exercises below the appropriate   #
# comment, and click run when complete, using either the menu-bar at the top,  #
# or the F5 key on your keyboard.                                              #
################################################################################

# Security
'''
    Return to the lesson 6 exercises and modify the Matrix class so it uses deep 
    copies for __init__, get_rows, get_columns, add_row, add_column, and
    transpose, such that no user inputs are used directly, and no method outputs
    allow direct access to the internal state of a Matrix instance.
'''

# Recursion/Loops
'''
    Write a recursive method max_sort1 to take a list of numbers and sort it 
    from largest to smallest. The end result should be returned, and the 
    original list should not be modified.
    
    Then write max_sort2 to perform the same function as max_sort1, but using a
    traditional (for/while) loop instead. Do not use the existing 'max' function
    in max_sort1 or max_sort2.
    
    e.g. a = [1,3.5,2], b = max_sort(a) -> b = [3.5,2,1], a = [1,3.5,2]
'''

# <your recursion/loops practice code here>

# Exception Handling/Raising
'''
    Write a function 'check_file' which takes a filename and attempts to open it
    and check its validity. If the file opens successfully but is not valid, an
    'InvalidFileError' (defined below) should be raised, with a meaningful
    message. A valid file should exist, should be readable, and should have the
    same number of lines as letters per line (e.g. a file with five lines should
    have five letters per line). Note that lines can also contain an arbitrary
    number of non-letter characters. Letters that should be counted are
    lowercase and uppercase letters of the English alphabet*. If the file is
    valid, check_file should return True. Any errors raised after the file has
    opened should be re-raised as InvalidFileErrors, with their error message
    intact. This can be accomplished by:

    except ExceptionName as e:
        raise InvalidFileError(e)
    
    Write another function 'user_interface' which takes no arguments. It should
    repeatedly prompt the user for a filename until one is provided which passes
    the check_file function. Any errors raised by check_file should be caught,
    with any messages printed to the user before the re-prompt. The error
    messages should be printed to 'standard error', instead of normal printing
    which goes to 'standard output'. This can be accomplished with:
        print('message', file=sys.stderr) # import sys if necessary

    * check stackoverflow.com/questions/9072844 for some hints as to how to do
        this - it hasn't been covered in this course.
'''

# <your exception practice code here>

class InvalidFileError(Exception):
    ''' An error for invalid file format.

    raise InvalidFileError(str'message'/Exception)
    
    '''
    pass
    




'''
    When you're done, click Run or F5 to check that you've followed the
    instructions. Example solutions can be found at the bottom of the exercise
    checker file.

    The code below isn't for editing, it's used to run the test file when this
    program is run.
'''

if __name__ == '__main__':
    # get the Matrix class from lesson 6
    import sys; sys.path.append('..')
    from L6.L6_1_exercises import Matrix
    
    # import and set up the tests
    from L8_2_exercise_checker import MatrixTests, LoopTests, ErrorsTests, \
         TestGroup
    L8Tests = TestGroup(MatrixTests(), LoopTests(), ErrorsTests())

    # run the tests (with feedback)
    L8Tests.run_tests(verbose=True)
