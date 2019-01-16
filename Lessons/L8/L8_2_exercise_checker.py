#!/usr/bin/env python3
################################################################################
# This file contains tests for the L8_1_exercises.py file.                     #
################################################################################

from L8_1_exercises import InvalidFileError
import sys # path, plus standard streams (stdin/stdout/stderr)
sys.path.append('..') # allow for TestRun imports
from TestRun import TestRun, TestGroup, Redirect, MultiRedirect

import os
if not os.path.exists('test_files'):
    os.mkdir('test_files')

import random

class MatrixTests(TestRun):
    ''' Tests for deep-copies in the Matrix class (from L6_1_examples.py). '''
    
    def test_init_rows(self):
        ''' Testing deep-copy nature of rows initialisation. '''
        rows = [[1,2,3],[4,5,6],[7,8,9]]
        row_copy = [list(row) for row in rows]
        M = Matrix(rows=row_copy)
        row_copy[0] = [0,0,0]; row_copy[1][0] = 0 # modify input
        assert M.get_rows() == rows, "Initialising with rows should not " +\
               "maintain links to the row inputs."

    def test_init_columns(self):
        ''' Testing deep-copy nature of columns initialisation. '''
        columns = [[1,4,7],[2,5,8],[3,6,9]]
        col_copy = [list(col) for col in columns]
        M = Matrix(columns=col_copy)
        col_copy[0] = [0,0,0]; col_copy[1][0] = 0 # modify input
        assert M.get_columns() == columns, "Initialising with columns should" +\
               " not maintain links to the column inputs."

    def test_get_rows(self):
        ''' Testing deep-copy nature of the get_rows method. '''
        rows = [[1,2,3],[4,5,6],[7,8,9]]
        M = Matrix(rows=[list(row) for row in rows])
        new_rows = M.get_rows()
        new_rows[0] = [0,0,0]; new_rows[1][0] = 0
        assert M.get_rows() == rows, "'get_rows' should not maintain links " +\
               "to the internal Matrix state."

    def test_get_columns(self):
        ''' Testing deep-copy nature of the get_columns method. '''
        columns = [[1,4,7],[2,5,8],[3,6,9]]
        M = Matrix(columns=[list(col) for col in columns])
        new_cols = M.get_columns()
        new_cols[0] = [0,0,0]; new_cols[1][0] = 0
        assert M.get_columns() == columns, "'get_columns' should not " +\
               "maintain links to the internal Matrix state."
        
    def test_add_row(self):
        ''' Testing deep-copy nature of add_row method. '''
        rows = [[1,2,3],[4,5,6]]
        M = Matrix(rows=[list(row) for row in rows])
        new_row = [7,8,9]; rows += [list(new_row)]
        M.add_row(new_row)
        new_row[0] = 0
        assert M.get_rows() == rows, "'add_row' should not maintain links" +\
               " to the inputted row."

    def test_add_column(self):
        ''' Testing deep-copy nature of add_column method. '''
        columns = [[1,4,7],[2,5,8]]
        M = Matrix(columns=[list(col) for col in columns])
        new_col = [3,6,9]; columns += [list(new_col)]
        M.add_column(new_col)
        new_col[0] = 0
        assert M.get_columns() == columns, "'add_column' should not maintain" +\
               " links to the inputted column."

    def test_transpose(self):
        ''' Testing deep-copy nature of transpose method. '''
        rows = [[1,2,3],[4,5,6],[7,8,9]]
        row_copy = [list(row) for row in rows]
        rows_t = Matrix.transpose(matrix=row_copy)
        rows_t[0] = [0,0,0]; rows_t[1][1] = 0
        assert row_copy == rows, "'transpose' output should not be linked to" +\
               " its input."
        

class LoopTests(TestRun):
    ''' Tests for the recursive and loops section. '''
    # class-variable RecursionCheck class
    class RecursionCheck(object):
        ''' A class for checking if a function is recursive. '''
        def __init__(self, func):
            self.count = 0
            self._func = func
        def __call__(self, *args, **kwargs):
            self.count += 1
            return self._func(*args, **kwargs)
            
    def __init__(self, num_tests=500):
        ''' Initialises this set of loop tests. '''
        super().__init__()
        self._num_tests = num_tests

    # general test helpers
    def max_sort_output(self, max_sort):
        ''' Tests the output of a max_sort function. '''
        start_list = []
        for i in range(random.randint(0,100)):
            start_list += [random.uniform(-10000,10000)]
        in_list = list(start_list); result = max_sort(in_list)
        correct = list(start_list); correct.sort(reverse=True)
        assert result == correct, 'Incorrect sorting:\n' + str(start_list) +\
               '\nshould become\n' + str(correct) + '\nnot\n' + str(result)

    def max_sort_data(self, max_sort):
        ''' Tests if a max_sort function modifies its input. '''
        start_list = []
        for i in range(random.randint(0,100)):
            start_list += [random.uniform(-10000,10000)]
        in_list = list(start_list); result = max_sort(in_list)
        assert in_list == start_list, "'max_sort' should not modify its input."

    # test functions
    def test_max_sort1_data(self):
        ''' Tests if max_sort1 modifies its input. '''
        for i in range(self._num_tests):
            self.max_sort_data(max_sort1)
        
    def test_max_sort1_output(self):
        ''' Tests if max_sort1 outputs correctly. '''
        for i in range(self._num_tests):
            self.max_sort_output(max_sort1)

    def test_max_sort1_recursion(self):
        ''' Tests if max_sort1 is correctly implemented (recursively). '''
        global max_sort1
        max_sort1 = self.RecursionCheck(max_sort1)
        max_sort1([1,3.5,2,4])
        assert max_sort1.count > 1, "'max_sort1' should be recursively "+\
               "implemented."

    def test_max_sort2_data(self):
        ''' Tests if max_sort2 modifies its input. '''
        for i in range(self._num_tests):
            self.max_sort_data(max_sort2)
        
    def test_max_sort2_output(self):
        ''' Tests if max_sort2 outputs correctly. '''
        for i in range(self._num_tests):
            self.max_sort_output(max_sort2)

    def test_max_sort2_recursion(self):
        ''' Tests if max_sort2 is correctly implemented (not recursively). '''
        global max_sort2
        max_sort2 = self.RecursionCheck(max_sort2)
        max_sort2([1,3.5,2,4])
        assert max_sort2.count == 1, "'max_sort2' should not be recursively "+\
               "implemented."

class ErrorsTests(TestRun):
    ''' Tests for the error-handling section. '''
    def __init__(self):
        ''' Initialise tests and test files. '''
        super().__init__()
        # generate some valid files
        for i in range(3):
            with open('test_files/valid{}.txt'.format(i+1), 'w') as valid_file:
                number = random.randint(1,40)
                lines = []
                for line_ind in range(number):
                    line = ''
                    letter_count = 0
                    while letter_count != number:
                        char = self.char()
                        line += char
                        if char.isalpha():
                            letter_count += 1
                    lines += [line]
                valid_file.write('\n'.join(lines) + '\n')
        
        # create some invalid files
        with open('test_files/invalid1.txt', 'w') as invalid_file:
            invalid_file.write('14>32 9.30') # 1 line, 0 letters
        with open('test_files/invalid2.txt', 'w') as invalid_file:
            invalid_file.write('abc123\nd4e5f6') # 2 lines, 3 letters per line
        with open('test_files/invalid3.txt', 'w') as invalid_file:
            invalid_file.write('abc\ndefg\nhij') # 3 lines, 4 letters 2nd line

        # store redirect filenames
        self._in_name = 'test_files/in.txt'
        self._err_name = 'test_files/err.txt'
        self._out_name = 'test_files/out.txt'

    def char(self):
        ''' Returns a random character. '''
        options = '1234567890qwertyuiopasdfghjklzxcvbnm,./?`~' +\
                  'QWERTYUIOPASDFGHJKLZXCVBNM[]{}()*&^%$#@!<>'
        return options[random.randrange(0, len(options))]

    def test_check_file(self):
        ''' Tests the 'check_file' function. '''
        check_file # check existence
        
        for i in range(3):
            filename = 'test_files/valid{}.txt'.format(i+1)
            # test a valid file
            try:
                assert check_file(filename) # raises exception on failure
            except Exception:
                assert False, "File {} should register as valid.".format(
                    filename)

            # test an invalid file
            try:
                check_file('test_files/invalid{}.txt'.format(i+1))
                assert False, "File in{} should register as invalid.".format(
                    filename)
            except InvalidFileError:
                pass # test successful (correct error raised)
            except Exception as e:
                assert False, "Raised exception from an invalid openable file"+\
                       " should be InvalidFileError, not {}".format(e.__name__)

        # test a nonexistent (invalid) file
        try:
            check_file('')
            assert False, "Non-existent files should register as invalid."
        except InvalidFileError:
            assert False, "InvalidFileErrors should only be raised if the " +\
                   "file can be opened and read."
        except Exception:
            pass # test successful


    def test_user_interface(self):
        ''' Tests the 'user_interface' function. '''
        user_interface # check existence

        # set up input
        with open(self._in_name, 'w') as in_file:
            in_file.write('test_files/valid1.txt\n' +\
                          'test_files/invalid1.txt\n' + \
                          'test_files/valid2.txt\n')

        redirects = MultiRedirect(Redirect(sys.stdin, open(self._in_name, 'r')),
            Redirect(sys.stderr, open(self._err_name, 'w'), maintain=False),
            Redirect(sys.stdout, open(self._out_name, 'w'), maintain=False))
        
        user_interface()
        redirects.close(0, ids=[1,2]) # close error and out files
        try:
            with open(self._err_name,'r') as err_file:
                error_text = err_file.read()
                assert error_text == '', "No prints should be made to stderr"+\
                       " for a valid file input.\n" +\
                       "'{}' should have been ''.".format(error_text)
                           
            with open(self._out_name,'r') as out_file:
                out_text = [line for line in out_file.readlines() if line != '']
                num_lines = len(out_text)
                assert num_lines == 1, "Only 1 prompt should be displayed"+\
                       " for a valid file input, not {}.".format(num_lines)
                prompt = out_text[0]
                
            # reopen error and out files
            redirects.replace_stream(0, open(self._err_name, 'w'), ids=[1])
            redirects.replace_stream(0, open(self._out_name, 'w'), ids=[2])
            
            user_interface()
            
            redirects.close(0, ids=[1,2]) # close error and out files
            with open(self._err_name,'r') as err_file:
                assert err_file.read() != '', "Prints should be made to " +\
                       "stderr for an invalid file input."
                
            with open(self._out_name,'r') as out_file:
                out_text = out_file.read()
                assert out_text.count(prompt) == 2, "2 prompts should be " +\
                       "displayed for an invalid then a valid file input, " +\
                       "not {}.".format(num_lines)
        finally:
            redirects.close() # restore stdin, stderr, and stdout




#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    class Matrix(object):
        ''' A Matrix class. '''
        def __init__(self, dims=[], rows=None, columns=None):
            ''' A class for storing and operating on matrices.

            Creates an m*n zero matrix if constructed with dims=[m,n], else
                stores the specified 'rows' OR 'columns'.

            Constructors:
                Matrix(dims=list[int,int])
                Matrix(rows=list[list[int/float]])
                Matrix(columns=list[list[int/float]])

            '''
            if rows:
                # make a deep copy of rows
                self._rows = [list(row) for row in rows]
            elif columns:
                self._rows = self.transpose(columns)
            elif dims:
                blank_row = [0] * dims[1] # create a blank row
                # duplicate the blank row with list comprehension
                self._rows = [list(blank_row) for row in range(dims[0])]

        def get_dims(self):
            ''' Returns the dimensions of this Matrix instance as
                [rows,columns].

            self.get_dims() -> list[int,int]

            '''
            return [len(self._rows), len(self._rows[0])]
                
        def get_rows(self):
            ''' Returns a deep copy of the rows in this Matrix.

            self.get_rows() -> list[list[int/float]]

            '''
            return [list(row) for row in self._rows]

        def get_columns(self):
            ''' Returns a deep copy of the columns in this Matrix.

            self.get_columns() -> list[list[int/float]]

            '''
            return self.transpose(self._rows)

        def add_row(self, row):
            ''' Adds a row to this Matrix.

            self.add_row(list[int/float]) -> None

            '''
            self._rows += [list(row)]

        def add_column(self, column):
            ''' Adds a column to this Matrix.

            self.add_column(list[int/float]) -> None

            '''
            self._rows = self.transpose(
                self.transpose(self._rows) + [list(column)])

        @staticmethod
        def transpose(matrix):
            ''' Returns a transposed list of the inputted matrix data.

            self.transpose(list[list[int/float]]) -> list[list[int/float]]

            '''
            rows = matrix
            # initialise column matrix to zeros
            blank_col = [0] * len(rows)
            columns = [list(blank_col) for col in range(len(rows[0]))]
            # copy across elements
            for row_ind, row in enumerate(rows):
                for col_ind, element in enumerate(row):
                    columns[col_ind][row_ind] = element

            return columns

        def __str__(self):
            ''' A human-readable string representation of this Matrix instance.

            self.__str__() -> str

            '''
            return 'Matrix:\n\t' + '\t'.join(
                [', '.join([str(el) for el in row]) + '\n' \
                 for row in self._rows])

        def __repr__(self):
            ''' A formal string representation of this Matrix instance.

            self.__repr__() -> str

            '''
            return 'Matrix(rows={!r})'.format(self._rows)

        def __eq__(self, obj):
            ''' Returns True if this is equivalent to obj.

            self.__eq__(object) -> bool

            '''
            # check type first, then data
            if not isinstance(obj, type(self)) or self._rows != obj._rows:
                return False
            
            # instances are equivalent
            return True

    def max_sort1(a):
        ''' Returns a copy of 'a', sorted from largest to smallest.
        
        max_sort1(list[int/float]) -> list[int/float]
        
        '''
        a = list(a) # make a copy of 'a' to work with
        if len(a) <= 1:
            return a
        maxVal, maxInd = (a[0], 0) # initialise max as first element
        # find the largest value, and move it to the start of the returned list
        for index, val in enumerate(a):
            if val > maxVal:
                # new maximum determined
                maxVal, maxInd = val, index
        a.pop(maxInd) # remove the maximum value from the original list (copy)
        return [maxVal] + max_sort1(a)

    def max_sort2(a):
        ''' Returns a copy of 'a', sorted from largest to smallest.
        
        max_sort2(list[int/float]) -> list[int/float]
        
        '''
        a_copy = list(a)
        changes = 1
        while changes > 0: # continue until no further changes occur
            changes = 0 # start off with no changes
            # iterate, swapping each pair that's in the wrong order 
            for index, curr in enumerate(a_copy):
                if index > 0 and curr > prev:
                    # swap curr and prev, because current > previous
                    a_copy[index-1], a_copy[index] = curr, prev
                    changes += 1
                else:
                    prev = curr # update/set prev if no swap occurred
        return a_copy

    def check_file(filename):
        ''' Returns True if letters per line == number of lines in the file.

        Letters can be capitalised or lower-case, but should be in the English
            alphabet.

        Raises an InvalidFileError on invalid file, and Exception if file
            cannot be found or read.

        check_file(str) -> bool

        '''
        with open(filename, 'r') as file:
            try:
                letter_count = 0
                line_count = 0
                for line in file:
                    line_count += 1
                    num_letters = sum(c.isalpha() for c in line)
                    if letter_count == 0:
                        letter_count = num_letters
                    elif letter_count != num_letters:
                        raise InvalidFileError(
                            'Lines must all contain the same number of letters')
                    elif letter_count < line_count:
                        raise InvalidFileError('There must be the same number'+\
                                               'of lines as letters per line.')
                if letter_count != line_count:
                    raise InvalidFileError('There must be the same number of' +\
                                           ' lines as letters per line.')
            except Exception as e:
                raise InvalidFileError(e)
        return True
        

    def user_interface():
        ''' Repeatedly prompts user for filename until valid.

        Validity is determined by the 'check_file' function.

        user_interface() -> None

        '''
        filename = input('Input filename: ')
        try:
            check_file(filename)
        except Exception as e:
            print(str(e), file=sys.stderr)
            user_interface()
        
    L8Tests = TestGroup(MatrixTests(), LoopTests(), ErrorsTests())
    L8Tests.run_tests(verbose=True)
