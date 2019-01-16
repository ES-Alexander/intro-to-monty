#!/usr/bin/env python3
################################################################################
# This file contains tests for the L6_1_exercises.py file.                     #
################################################################################

import sys; sys.path.append('..')
from TestRun import TestRun, TestGroup

class PersonTests(TestRun):
    ''' Tests for the Person class. '''
    def __init__(self):
        ''' Initialises this test suite. '''
        super().__init__()
        
        # initialise types and counts
        self._types = {'instance method':0, 'static method':0, 'class method':0,
                       'class variable':0}
        self._doc_check = True

        # Can't test instance variables, because don't have instances

        # unbound instance methods have the same type as external functions
        instancemethod = type(lambda:None)
        exclusions = ['__module__','__doc__','__dict__','__weakref__']
        
        cls_vars = vars(Person)
        cs = [cls_vars[c] for c in cls_vars if c not in exclusions]
        for c in cs:
            if isinstance(c, (classmethod, staticmethod, instancemethod)):
                self._doc_check = self._doc_check and c.__doc__
                if isinstance(c, classmethod):
                    self._types['class method'] += 1
                elif isinstance(c, staticmethod):
                    self._types['static method'] += 1
                elif isinstance(c, instancemethod):
                    self._types['instance method'] += 1
            else:
                self._types['class variable'] += 1

    def test_instance_methods(self):
        ''' Tests for >= 3 instance methods. '''
        assert self._types['instance method'] >= 3, \
               'Should have at least three instance methods.'

    def test_class_methods(self):
        ''' Tests for at least one classmethod. '''
        assert self._types['class method'] > 0, \
               'Should have at least one classmethod.'

    def test_static_methods(self):
        ''' Tests for at least one staticmethod. '''
        assert self._types['static method'] > 0, \
               'Should have at least one staticmethod.'

    def test_class_variables(self):
        ''' Tests for at least two class variables. '''
        assert self._types['class variable'] >= 2, \
               'Should have at least two class variables.'

    def test_docs_exist(self):
        ''' Tests that all methods have a docstring. '''
        assert self._doc_check, 'All methods should have a docstring.'


class MatrixTests(TestRun):
    ''' Tests for the Matrix class. '''
    def test_constructors(self):
        ''' Testing different constructor methods. '''
        M1 = Matrix(dims=[4,20])
        M2 = Matrix(rows=[[1,2,3,4,5],[6,7,8,9,10]])
        M3 = Matrix(columns=[[1,6],[2,7],[3,8],[4,9],[5,10]])

    def test_representation(self):
        ''' Testing for __str__ and validity of __repr__ method. '''
        # existence check/definition in Matrix class
        for method in ['__str__', '__repr__']:
            assert method in vars(Matrix), '{} method '.format(method) +\
                   'should be defined in this class.'

        for M1_str in ['Matrix(dims=[3,4])', 'Matrix(rows=[[1,2],[3,4]])',
                       'Matrix(columns=[[1,3],[2,4]])']:
            
            M1 = eval(M1_str)
            try:
                M2 = eval(repr(M1))
            except Exception:
                assert False, '__repr__ method output should be instantiable.'

            assert M1 == M2, 'Instantiation from __repr__ method should ' +\
                   'produce an equivalent copy of the original instance.' +\
                   'Failed for {!r}'.format(M1_str)

    def test_equivalency(self):
        ''' Tests the __eq__ method. '''
        M1 = [Matrix(dims=[3,4]), Matrix(rows=[[1,2,3,4,5],[6,7,8,9,10]])]
        M2 = [Matrix(rows=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
              Matrix(columns=[[1,6],[2,7],[3,8],[4,9],[5,10]])]
        for i in range(len(M1)):
            assert M1[i] == M2[i], 'Equivalent matrices should register as ' +\
                   'equivalent.\nTest: {!r} == {!r}'.format(M1[i], M2[i])

    def test_get_rows(self):
        ''' Tests the get_rows method. '''
        rows = [[1,2,3],[4,5,6],[7,8,9]]
        rM1 = Matrix(rows=[list(row) for row in rows]).get_rows()
        assert rM1 == rows, 'rows = {} -> get_rows() = {}'.format(
            rows, rM1) + '\n(should be {})'.format(rows)

        dims2 = [3,4]
        rows2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        rM2 = Matrix(dims=dims2).get_rows()
        assert rM2 == rows2, 'dims = {} -> get_rows() = {}'.format(
            dims2, rM2) + '\n(should be {})'.format(rows2)

        cols3 = [[1,6],[2,7],[3,8],[4,9],[5,10]]
        rows3 = [[1,2,3,4,5],[6,7,8,9,10]]
        rM3 = Matrix(columns=[list(col) for col in cols3]).get_rows()
        assert rM3 == rows3, 'columns = {} -> get_rows() = {}'.format(
            cols3, rM3) + '\n(should be {})'.format(rows3)

    def test_get_columns(self):
        ''' Tests the get_columns method. '''
        cols = [[1,2,3],[4,5,6],[7,8,9]]
        cM1 = Matrix(columns=[list(col) for col in cols]).get_columns()
        assert cM1 == cols, 'columns = {} -> get_columns() = {}'.format(
            cols, cM1) + '\n(should be {})'.format(cols)

        dims2 = [4,3]
        cols2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        cM2 = Matrix(dims=dims2).get_columns()
        assert cM2 == cols2, 'dims = {} -> get_columns() = {}'.format(
            dims2, cM2) + '\n(should be {})'.format(cols2)

        rows3 = [[1,6],[2,7],[3,8],[4,9],[5,10]]
        cols3 = [[1,2,3,4,5],[6,7,8,9,10]]
        cM3 = Matrix(rows=[list(row) for row in rows3]).get_columns()
        assert cM3 == cols3, 'rows = {} -> get_columns() = {}'.format(
            rows3, cM3) + '\n(should be {})'.format(cols3)
        
    def test_add_row(self):
        ''' Tests the add_row method. '''
        M1 = Matrix(columns=[[1,2,3],[5,6,7],[9,10,11]])
        M1.add_row([4,8,12])
        assert M1.get_rows() == [[1,5,9],[2,6,10],[3,7,11],[4,8,12]], \
               'Adding row [4,8,12] to rows=[[1,5,9],[2,6,10],[3,7,11]] ' +\
               'should yield rows=[[1,5,9],[2,6,10],[3,7,11],[4,8,12]], ' +\
               'but gave rows={}'.format(M1.get_rows())

    def test_add_column(self):
        ''' Tests the add_column method. '''
        M1 = Matrix(rows=[[1,2,3],[5,6,7],[9,10,11]])
        M1.add_column([4,8,12])
        assert M1.get_columns() == [[1,5,9],[2,6,10],[3,7,11],[4,8,12]], \
               'Adding column [4,8,12] to columns=' +\
               '[[1,5,9],[2,6,10],[3,7,11]] should yield ' +\
               'columns=[[1,5,9],[2,6,10],[3,7,11],[4,8,12]], ' +\
               'but gave columns={}'.format(M1.get_columns())

    def test_transpose(self):
        ''' Tests the transpose staticmethod. '''
        assert isinstance(vars(Matrix)['transpose'], staticmethod), \
               "'transpose' method should be a staticmethod."

        rows = [[1,6],[2,7],[3,8],[4,9],[5,10]]
        cols = [[1,2,3,4,5],[6,7,8,9,10]]
        assert Matrix.transpose(rows) == cols, 'The transpose of {}'.format(
            rows) + ' should be {}, not {}.'.format(cols,
                                                    Matrix.transpose(rows))
        
    def test_general_use(self):
        ''' Tests some general usage of a Matrix instance. '''
        M1 = Matrix(dims=[1,2])
        assert M1.get_rows() == [[0,0]], 'Matrix(dims=[1,2]) should have ' +\
               'rows=[[0,0]], not get_rows()={}'.format(M1.get_rows())

        M1.add_row([1,2])
        assert M1.get_columns() == [[0,1],[0,2]]

        M1.add_column([0,3])
        M1.add_row([4,5,6])
        M2 = Matrix(columns=M1.get_rows())
        assert M2.transpose(M2.get_rows()) == M1.get_rows()
        assert M1.get_dims() == M2.get_dims(), \
               'Matrices of the same size should have the same dimensions.'

#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    class Person(object):
        ''' A Person class. '''
        
        species = 'human'
        planet = 'earth'
        
        def __init__(self, name, age, gender, sexuality):
            ''' Initialises a Person instance for tracking.

            Constructor: Person(str, int, str)

            '''
            self._name = name
            self._age = age
            self._gender = gender
            self._sexuality = sexuality

        def __repr__(self):
            ''' A formal string representation of this Person instance.

            self.__repr__() -> str

            '''
            return \
                'Person(name={!r},age={!r},gender={!r},sexuality={!r})'.format(
                    self._name, self._age, self._gender, self._sexuality)

        def __str__(self):
            ''' A human-readable representation of this Person instance.

            self.__str__() -> str

            '''
            return 'Person:\n\tname={!s}\n\tage={!s}'.format(self._name,
                    self._age) + '\n\tgender={!s}\n\tsexuality={!s}'.format(
                        self._gender, self._sexuality)

        @classmethod
        def info(cls):
            ''' Prints information about the Person class.

            cls.info() -> None

            '''
            print("Hello stranger, a 'Person' is a member of the {!s}".format(
                cls.species), "species, who mostly live on planet {!s}.".format(
                cls.planet))

        @staticmethod
        def find_and_destroy(verbose=False):
            ''' Finds and destroys all active global Person instances.

            If verbose is set to True, mourns those passed.

            Person.find_and_destroy(*bool) -> None

            '''
            instances = globals()
            first = True; count = 0 # initialise state tracking
            # get a list of all current Person instances
            people = [var_name for var_name in instances \
                      if isinstance(instances[var_name], Person)]
            # remove them, one by one...
            while people:
                next_to_go = people[0]
                if first:
                    print('Mwahahahaaa...',end=' ')
                    first = False
                else:
                    print('Aaaaand another one bites the dust...',end=' ')
                name = instances[next_to_go]._name
                age = instances[next_to_go]._age
                del instances[next_to_go]
                count += 1
                print(count, 'down!')
                # mourn those passed if asked to
                if verbose:
                    from random import randrange
                    ad1 = ['much','highly','very','somewhat'][randrange(0,4)]
                    ad2 = ['loved','respected','disliked','looney']\
                          [randrange(0,4)]
                    n1 = ['friend','lover','baker','daredevil'][randrange(0,4)]
                    n2 = ['family member','phantom','joker','pet']\
                         [randrange(0,4)]
                    eulogy = ' '.join(['A',ad1,ad2,n1,'and',n2])
                    print('R.I.P. {} ({}) - {}'.format(name, age, eulogy))
                people = [var_name for var_name in instances \
                          if isinstance(instances[var_name], Person)]
                    
    
    class Matrix(object):
        ''' A Matrix class. '''
        def __init__(self, dims=[], rows=None, columns=None):
            ''' A class for storing and opoerating on matrices.

            Creates an m*n zero matrix if constructed with dims=[m,n], else
                stores the specified 'rows' OR 'columns'.

            Constructors:
                Matrix(dims=list[int,int])
                Matrix(rows=list[list[int/float]])
                Matrix(columns=list[list[int/float]])

            '''
            
            if rows:
                self._rows = rows
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
            ''' Returns the rows in this Matrix.

            self.get_rows() -> list[list[int/float]]

            '''
            return self._rows

        def get_columns(self):
            ''' Returns a deep copy of the columns in this Matrix.

            self.get_columns() -> list[list[int/float]]

            '''
            return self.transpose(self._rows)

        def add_row(self, row):
            ''' Adds a row to this Matrix.

            self.add_row(list[int/float]) -> None

            '''
            self._rows += [row]

        def add_column(self, column):
            ''' Adds a column to this Matrix.

            self.add_column(list[int/float]) -> None

            '''
            self._rows = self.transpose(self.transpose(self._rows) + [column])

        def __str__(self):
            ''' A human-readable string representation of this Matrix instance.

            self.__str__() -> str

            '''
            return 'Matrix:\n\t' + '\t'.join(
                [', '.join([str(element) for element in row]) + '\n' \
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
            
        
    L6Tests = TestGroup(PersonTests(), MatrixTests())
    L6Tests.run_tests(verbose=True)
