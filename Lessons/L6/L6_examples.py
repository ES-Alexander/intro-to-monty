#!/usr/bin/env python3
# L6 Questions

#1
'''
    Define an instantiable 'Person' class, including some common person-specific
    properties as instance variables, such as name, age, etc. Also include some
    class variables as properties that are the same for all people (e.g.
    species, body parts, etc).

    The class outline, known as a 'stub', has been provided below to fill out.
    There's no need to define additional functions beyond those given.
'''

class Person(object):
    ''' Class comment here. '''

    # class variables here

    def __init__(<initialisation parameters>):
        ''' Class usage comment here.

        Additional information about properties and the class.

        Constructor line

        '''
        # instance variables here

    def __repr__():
        ''' Function return comment.

        Description of output.

        Calling code line

        '''
        pass

    def __str__():
        ''' Function return comment.

        Description of output.

        Calling code line

        '''
        pass


#2
'''
    Define an instantiable 'Matrix' class, using python lists as the basis to
    construct 2D matrices. Include the relevant instantiation methods (__init__,
    __repr__, and __str__), as well as methods to get_rows, get_columns
    (returning a list of the rows, and a list of the columns respectively),
    get_num_rows, get_num_columns, (returning as relevant) and add_row,
    add_column (taking in a row/column of the correct length for the matrix,
    and adding it to the current matrix).

    The __init__ method should be able to initialise a matrix from a length and
    width, or from a set of rows, or a set of columns. Lesson 8 will cover a
    more secure way to implement the get_rows and get_columns methods, but for
    now just write them to return the desired information.

    If the add_row or add_column methods are given invalid inputs, they should
    print an error message advising of the failed operation, as well as the
    length the row/column should have beem. An invalid input should not cause
    any adjustment to the internal state of the matrix.
'''
