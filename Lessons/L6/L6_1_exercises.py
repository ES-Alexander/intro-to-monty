#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following exercises below the appropriate   #
# comment, and click run when complete, using either the menu-bar at the top,  #
# or the F5 key on your keyboard.                                              #
################################################################################

#1
'''
    Define an instantiable 'Person' class, including some common person-specific
    properties as instance variables, such as name, age, etc. Also include some
    class variables as properties that are the same for all (or most) people
    (e.g. species, body parts, etc).

    The class outline, known as a 'stub', has been provided below to fill out.
    Also define at least one classmethod and one staticmethod.
'''

class Person(object):
    ''' Class comment here. '''

    # class variables here

    def __init__(self): #<initialisation parameters>):
        ''' Class usage comment here.

        Additional information about properties and the class.

        Constructor line

        '''
        # instance variables here
        pass

    def __repr__(self): #<parameters>):
        ''' Function return comment.

        Description of output.

        Calling code line

        '''
        pass

    def __str__(self): #<parameters>):
        ''' Function return comment.

        Description of output.

        Calling code line

        '''
        pass


#2
'''
    Define an instantiable 'Matrix' class, using python lists as the basis to
    construct 2D matrices. Include the relevant instantiation methods (__init__,
    __repr__, __str__, and __eq__), as well as methods to get_rows, get_columns
    (returning a list of the rows, and a list of the columns respectively),
    get_dims, (returning as [num_rows, num_cols]) and add_row, add_column
    (taking in a row/column of the correct length for the matrix, and adding it
    to the current matrix). You should also create a 'transpose' staticmethod
    which takes a list of lists, and returns the inputted data transposed (e.g.
    if a list of row lists is entered, the return value should be a list of
    column lists).

    The __init__ method should be able to initialise a matrix from a set of
    rows, a set of columns, or a 2 element list 'dims' of [num_rows, num_cols]
    (create a matrix of zeros with the specified dimensions). The provided
    'def __init__(...)' line is required for automatic testing, so please do not
    modify it.

    If the add_row or add_column methods are given invalid inputs, they should
    print an error message advising of the failed operation, as well as the
    length the row/column should have beem. An invalid input should not cause
    any adjustment to the internal state of the matrix.
'''

class Matrix(object):
    ''' '''
    def __init__(self, dims=[], rows=None, columns=None):
        ''' '''
        pass





'''
    When you're done, click Run or F5 to check that you've followed the
    instructions. Example solutions can be found at the bottom of the exercise
    checker file.

    The code below isn't for editing, it's used to run the test file when this
    program is run.
'''

if __name__ == '__main__':
    # import and set up the tests
    from L6_2_exercise_checker import PersonTests, MatrixTests, TestGroup
    L6Tests = TestGroup(PersonTests(), MatrixTests())
    
    # run the tests (with feedback)
    L6Tests.run_tests(verbose=True)
