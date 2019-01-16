#!/usr/bin/env python3
################################################################################
#                                                                              #
#                                   Lesson 8                                   #
#                    Error Handling, Security, and Recursion                   #
#                                                                              #
################################################################################




#------------------------------- ERROR HANDLING -------------------------------#
'''
    Code robustness is part of what sets apart hobby programming from
    professionally produced programs intended for distribution. When you write
    a program for yourself to use, it is relatively common to assume function
    inputs will be valid and used correctly, and that functions and classes
    will be used logically and as intended. This generally allows for
    robustness, and even at times commenting, to be significantly neglected.

    When writing a program for general use there are three accepted 'good
    practice' methods of handling errors and invalid user input. The first of
    these is specification, which is often used without additional robustness
    methods when the intended users of a program are other programmers.

    If a programmer writes a specification describing all accepted inputs and
    the expected results, anyone using that program is expected to abide by
    that specification. If a user fails to follow the specification the outputs
    and behaviour of the program are undefined, and any undesired behaviour is
    considered the fault and problem of the user. Of course, this requires
    correct specification, so it is essential to provide accurate and correct
    specifications for all code you write. Under agreement of the specification
    the original programmer is free to implement the specification however they
    please. As such, using a program from its implementation instead of its
    specification can be dangerous, since it is subject to change at the whim
    of the programmer. This also reinforces the need for clear specification,
    since unclear, inaccurate, or incomplete specification can lead to code
    being used outside the realm of its specification.

    Beyond specification, additional error handling can add robustness to a
    program that allows it to fail 'safely', instead of catastrophically from
    an error. This is performed using error flags, or by 'excepting' errors
    which the programmer has reason to expect will occur. Either of these
    approaches can allow the programmer to display a helpful error message to
    the user explaining the issue, and potentially enables them to correct the
    cause of the error without being required to restart the program. Examples
    of basic error flag usage and error excepting is provided below.
'''



# Error Flags
'''
    Often the simplest way of error handling is defining variables to be used
    as flags, which are updated when an error is detected, and later used to
    avoid running extraneous code which relies on the success of earlier parts.
    This is particularly common in class initialisation, as well as in embedded
    micro-controller applications. An example is provided below.
'''

def list_divide(num_list):
    ''' Returns a tuple of the divided num_list, and the success state.

    Successful operation returns num_list with all elements divided by the
        element before, and the boolean value True. The first element is
        divided by the last element.
    Failure returns an empty list and False.

    num_list must contain only numerical values, with at least one element.

    list_divide(list[num]) -> (list[num], bool)

    '''
    success_state = True # set maintained success state error-flag
    for index in range(len(num_list)):
        if num_list[index - 1] == 0:
            num_list = []
            success_state = False
            print('numbers cannot validly be divided by 0.')
            break
        num_list[index] /= num_list[index - 1]
    return (num_list, success_state)


# Error Excepting
'''
    Errors (formally 'Exceptions') in python can also be 'caught' using the
    keywords 'try' and 'except' as below. The following example tries to read a
    file specified by the user, and print the contents of the file to the
    console. If an error occurs in reading the file (in the 'try' block), it is
    caught in the 'except' block and allows the user to try a different file.
    Once an error has been caught, dealing with it is known as 'handling'.
'''

file_input_incomplete = True
while file_input_incomplete:
    filename = input('Input filename: ')
    try:
        # try some code which may cause an exception (error)
        with open(filename, 'r') as file:
            # with __ as __ automatically closes file once with block is closed
            for line in file:
                print(line)
            file_input_incomplete = False
    except Exception as e:
        # run some code if an exception was caught
        # ('Exception' catches every possible error - more options below)
        print('File input failed, please try again.')
        print('Reason: ', e)


# Multiple Exceptions
'''
    It is possible to catch multiple exceptions related to the same 'try'
    block, by using multiple 'except' blocks, or, to deal with different
    exceptions the same way, by using a tuple of exceptions.
'''

try:
    # potentially exceptional code
    pass
except FileNotFoundError as e1:
    print('File Not Found: ', e1)
except (UnicodeError, KeyboardInterrupt) as e2:
    print('Something bad happened: ', e2)


# Nothing Bad Happened
'''
    Exception blocks also accept the 'else' keyword, the same way it's used in
    an if block, as below.
'''

try:
    # potentially exceptional code
    pass
except Exception as e:
    print(e)
else:
    print('Woohoo! It worked! :-)')


# Finally Blocks
'''
    Additional code which is desired to be run irrespective of any errors
    raised can be placed in a 'finally' block, after a try-except block.
'''

# 'filename' predefined variable
f = open(filename, 'r') # assumes there are no errors when opening the file
try:
    # potentially exceptional code
    file_data = f.read() # could be bad
    output = int(file_data) # probably bad
    second_output = 10/output # also could be bad
except Exception:
    output = 1
    second_output = 10
else:
    print('<does a happy dance>')
finally:
    print("This happens irrespective of if there is or isn't an error")
    f.close() # always close files if opened outside of a with statement.


# Exception Raising
'''
    Often it can be advantageous to raise your own exceptions to force the
    termination of a program once it leaves its defined region of
    specification. This can be at any particular desirable point, but can also
    be within the except block of an exception if the catching behaviour was
    still not fulfilled. An example is provided below, for some code which
    attempts to open a filename, then attempts to open it as a .txt file if the
    initial attempt fails.
'''

# 'filename' predefined variable
try:
    # attempt to open provided filename 'as-is'
    f = open(filename, 'r')
except FileNotFoundError:
    try:
        # attempt to open filename as a .txt file
        f = open(filename + '.txt', 'r')
    except FileNotFoundError:
        # provide exception message about not finding either file option
        raise FileNotFoundError("No such file or directory: '" +
                                filename + "' or '" + filename + ".txt'")
f.close()




#-------------------------- DEEP COPIES AND SECURITY --------------------------#
'''
    As you become more experienced as a programmer, your programs will tend to
    become more important, and may be shared amongst many people. The more
    widespread your code, the more desirable it is to avoid people being able
    to break your programs, intentionally or otherwise. You can partially
    protect against this with code robustness, but it also comes under the
    realm of program security.

    Lesson 4 suggested using immutable data-types as function inputs, to avoid
    functions being able to modify your variables before they return. Returning
    immutable data-types from a function also means that users calling the
    function don't gain access to the input variables. It is not always
    convenient to use immutable inputs and outputs however. Instead, security
    of a function can be improved by using so-called 'deep copies' of variables.

    A 'deep copy' is a copy of every possible aspect of a variable (effectively
    making it pass-by-value instead of pass-by-reference). A 'shallow copy' is
    a copy that still passes one or more references, and hence is inherently
    insecure.

    Copies are relevant to all mutable objects, and copy types are applicable
    to those potentially containing additional mutable objects. The basic
    iterable classes (lists, tuples) have shallow copying implemented by
    default, but deep copies are able to be defined with some knowledge of the
    contents (see note below). Also, although tuples themselves are immutable,
    any mutable contents can still be modified.
'''


# ----- NOTE: List/Tuple Copies ----- #
'''
    Creating a deep copy of a data storage type requires knowing something
    about the data being stored. If a tuple contains no data storage types, any
    copy of it will be a deep copy (including 'my_tuple2 = my_tuple'), due to
    the immutable nature of tuples. If a list contains no data storage types, a
    deep copy is provided by 'deep_copy = list(my_list)'. You may see this
    instead done using my_list[:] in others' code, but using the 'list'
    function is equivalent, and is clearer and easier to understand. Copying
    using the 'list' function is deep for a single layer, so deeper structures
    require additional iteration to get a full deep copy (see the second
    Recursion section example).
'''




#---------------------------------- RECURSION ---------------------------------#
'''
    Recursion is the name given to any function which calls itself in a
    program. It is generally considered one of the most confusing topics for a
    beginner programmer to learn, which mostly stems from the difficulty of
    thinking through, in a formal manner, a function calling itself multiple
    times. In saying that, recursion is in fact a powerful tool which can
    largely simplify the requirements of certain problems, and often uses less
    code to do so than a corresponding 'for' or 'while' loop.

    Recursion as a useable programming principle has two requirements: a
    function which calls itself, and an inevitable terminating case. If the
    recursive loop has no inevitable termination it just forms an infinite
    loop, which is usually undesirable. If an infinite loop is started, a
    program can be terminated manually using a keyboard interrupt, by pressing
    CTRL+C, sometimes repeatedly. If a program can't be interrupted, python can
    be forced to quit to stop the program, and reopened afterwards.

    Computer memory places a third requirement on recursion - the computer must
    provide sufficient memory to reach the terminating case of the recursive
    loop.

    Python itself applies a recursion limit which, if exceeded, terminates the
    program. Sometimes this limit is counted as exceeded some number of
    iterations below the limit, so try to avoid it where possible. This can
    cause issues when very long recursive loops are desired, but is usually
    good for automatically terminating infinite recursive loops. If need be the
    limit can be modified (using 'sys.setrecursionlimit(num)'), but try to
    avoid this unless absolutely necessary.

    Recursion is incredibly useful in rendering functions, such as those of
    fractals, where a specifiable amount of detail is able to be provided as
    the terminating condition, and a recursive rendering function works in
    sweeps to render to the desired level of detail. It also finds use in
    depth-first searching, and various other situations where it can be
    conceptually easier to think of a set of recursive loop conditions than to
    implement some other form of loop.
'''


# ----- NOTE: Loop Equivalency (Revisited) ----- #
'''
    The lesson 3 notes presented the fact that 'for' and 'while' loops are
    proven to be technically equivalent, in the sense that any loop written as
    one type can also be expressed as the other. Adding to this, any recursive
    loop can also technically be expressed as a for or while loop, it is just
    preferable in some cases to use one particular loop type to solve a given
    problem. Generally, recursion is used in cases where it is relatively easy
    to see the terminating case(s) and have a function which re-applies itself
    until completion.

    Be aware that in cases where an algorithm has multiple self-references at
    different stages (see third example), recursive implementations will
    generally be much less efficient than for or while loops. This is because
    recursion can't directly re-use the previously calculated result, so a
    recursive function might have to make the same low-level call multiple
    times, while a traditional loop can calculate it once and re-use the result.
'''



# Recursive Factorial (n!)
'''
    Factorials are a common topic in mathematics, representing the
    multiplication of a non-negative integer with all the integers below it
    (e.g. 4! = 4*3*2*1). The general form for calculating a factorial is n! = n
    * (n-1)!. Additionally, 0! = 1.

    In this case, the terminating cases are if n is 0 or 1, and the input is
    considered invalid if n is negative, not an integer, or above 2/3 of the
    system's recursion limit. The maximum limit is set to have a defined
    largest input, above which a meaningful 'invalid input' result can be
    returned, instead of causing errors when the actual recursive limit is
    reached.
'''

def factorial(n):
    ''' Returns the factorial of n (n!) if n is valid, else returns -1.
    
    'n' must be a non-negative integer to be valid.

    Works up to at least n = 500.

    factorial(int) -> int

    '''
    import sys # used for checking maximum number of recursive calls
    if not isinstance(n, int) or n < 0 or n > (sys.getrecursionlimit()*2)//3:
        # invalid input
        return -1
    elif n == 0 or n == 1:
        # terminating case
        return 1
    else:
        # make recursive call
        return n * factorial(n - 1)


# Recursive Deep Copy (List)
'''
    Consider a list which can contain numbers, strings, and more lists like
    itself. To get a deep copy of this variable requires iterating over each
    element, but for each element which is a list another layer of searching is
    required. Here our end condition is when an element is a number or string,
    and our copying function can recursively apply to each element. An example
    implementation of this is below.
'''

def list_deep_copy(old_list):
    ''' Returns a deep copy of the specified list, 'old_list'.

    'old_list' can contain numbers, strings, and more lists like itself.
        - if old_list is a number or string, it is returned.

    list_deep_copy(list) -> list
    list_deep_copy(int) -> int
    list_deep_copy(float) -> float
    list_deep_copy(str) -> str

    '''
    # check if old_list is an immutable type (not a list)
    if isinstance(old_list, str) or isinstance(old_list, int) or \
            isinstance(old_list, float):
        return old_list

    # old_list must be a list (by specification)
    new_list = list(old_list) # make a deep copy of old_list first layer
    for index, element in enumerate(old_list):
        # replace the shallow copy of each element with a deep copy
        if element is old_list:
            # just in case old_list contains itself...
            new_list[index] = new_list
        else:
            new_list[index] = list_deep_copy(old_list[index])
    return new_list


# Recursion Inefficiencies
'''
    The Fibonacci sequence of numbers is a numerical sequence commonly found in
    nature, and is named after Leonardo Da Vinci, otherwise known as Fibonacci.
    The nth Fibonacci number is defined by the sum of the two previous
    Fibonacci numbers (e.g. F(n) = F(n-1) + F(n-2). Once again, n should be a
    non-negative integer. In this case, F(0) = 0, and F(1) = 1.

    At first glance, this seems similar to the factorial example, where the
    terminating cases and recursive case are easy to identify. While this is
    true, implementing the fibonacci sequence with a recursive algorithm is
    highly inefficient, since F(n-1) requires the re-calculation of F(n-2), and
    the same applies for all lower levels until the terminating case.
'''

def inefficient_fibonacci(n):
    ''' Returns the nth number in the Fibonacci sequence.
    
    'n' must be a non-negative integer, else -1 is returned.

    inefficient_fibonacci(int) -> int

    '''
    if not isinstance(n, int) or n < 0:
        return -1
    if n == 0 or n == 1:
        return n
    return inefficient_fibonacci(n-1) + inefficient_fibonacci(n-2)

'''
    The solution to the inefficiency here is to store the results as they're
    calculated, and only calculate each result once. To achieve this, the
    results must be stored externally to the function calls. The following
    class uses the __call__ method to be callable like a function, and sets up
    the memory storage to be hidden from the user. A dictionary is used for
    storing the memory, because it has faster access times (relative to a list)
    as more values are stored.
'''

class Fibonacci(object):
    ''' A class for recursively calculating Fibonacci numbers. '''
    def __init__(self):
        ''' A class which recursively calculates and stores Fibonacci numbers.

        Due to recursive memory requirements, fails when attempting to calculate
            more than about 900 new numbers. Calculating in blocks of 900 at a
            time should work quickly.

        Constructor: Fibonacci()

        '''
        self._memory = {0:0, 1:1}

    def __call__(self, n):
        ''' Returns the nth number in the Fibonacci sequence.

        'n' must be a non-negative integer, else -1 is returned.

        self(int) -> int

        '''
        if not isinstance(n, int) or n < 0:
            return -1
        if n not in self._memory:
            self._memory[n] = self.__call__(n-1) + self.__call__(n-2)
        return self._memory[n]

'''
    Alternatively, this sequence is perhaps better calculated using a
    traditional loop than a recursive one. While doing this is slightly slower
    than the class version presented above, it avoids the issues of too many
    function calls, so can calculate arbitrarily large numbers in the sequence
    if given enough time. Note that this rearrangement isn't as directly
    related to the initial mathematical expression, but comes with significant
    efficiency improvements over the inefficient direct implementation.

    The loop form of calculation is presented below as both a function and a
    callable class (with memory storage).
'''

def fibonacci_loop(n):
    ''' Returns the nth number in the Fibonacci sequence.

    'n' must be a non-negative integer, else -1 is returned.

    fibonacci_loop(int) -> int

    '''
    if not isinstance(n, int) or n < 0:
        return -1
    if n == 0 or n == 1:
        return n
    # calculate the nth value
    old, new = 0, 1
    for i in range(n-1):
        (old, new) = (new, old + new)
    return new

class FibonacciLoop(object):
    ''' A class for calculating Fibonacci numbers. '''
    def __init__(self):
        ''' A class which calculates and stores Fibonacci numbers using a loop.

        Constructor: FibonacciLoop()
        
        '''
        self._memory = {0:0, 1:1}
        self._nMax = 1
    def __call__(self, n):
        ''' Returns the nth number in the Fibonacci sequence.

        'n' must be a non-negative integer, else -1 is returned.

        self(int) -> int
        
        '''
        if not isinstance(n, int) or n < 0:
            return -1
        if n not in self._memory:
            # calculate additional required values
            (old, new) = (self._memory[self._nMax-1], self._memory[self._nMax])
            for i in range(self._nMax-1, n-1):
                (old, new) = (new, old + new)
                self._nMax += 1
                self._memory[self._nMax] = new
        return self._memory[n]
                

