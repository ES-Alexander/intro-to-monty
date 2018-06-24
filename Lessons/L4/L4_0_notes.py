################################################################################
#                                                                              #
#                                   Lesson 4                                   #
#                Functional Programming, Functions, Abstraction                #
#                                                                              #
################################################################################




#---------------------------- FUNCTIONAL PROGRAMMING --------------------------#
'''
    Python is what is known as a hybrid language, comprised of both functional
    programming, and object-oriented programming. Functional programming forms
    programs which contain a number of linked functions, usually called within
    some main function which assimilates and runs them in the desired sequence.
    In contrast, object-oriented programming is formed by the creation and
    usage of different Classes (objects), each of which has a number of
    different functions, known as methods, assosciated with them.

    This lesson will focus on the basics of functions and functional
    programming, with object-oriented programming covered in a later lesson.
'''




#------------------------------ INBUILT FUNCTIONS -----------------------------#
'''
    To begin with, Python includes a number of inbuilt functions, by default
    coloured in IDLE in purple colour. Some of these have been
    used already, in earlier lessons, but the following list provides a brief
    description of the most widely used default functions. As mentioned in
    lesson 1, function names in Python are underscore_separated, by convention.
'''

# Mathematical Functions:
    abs(num) # returns the absolute value of a number
    pow(base, num) # returns the value of base^num
    max(numbers) # returns the largest value in an iterable set of data
    min(numbers) # returns the smallest value in an interable set of data
    sum(iterable, start) # returns the sum of 'start' (default 0), plus the
        # addition of all values in the iterable.
    complex(real[, imag]) # creates a complex number from the specified real,
        # and optionally specified imaginary component.
    divmod(num, divisor) # returns a tuple of quotient and remainder
    round(number[, ndigits]) # rounds the float number to the specified number
        # of digits

# Typecasting Functions:
#   Typecasting occurs when the user wishes to explicitly declare a variable
#   as of a given type, even if said variable is not of the specified type.
#   Given this is explicitly user performed, any associated data-loss (e.g. in
#   the truncation of a float to an integer) is assumed to be intentional,
#   without warning given. At times python may throw errors, however, if
#   necessary attributes of a variable are not present when casting to another
#   type.
    int(val) # casts val as an integer
    float(val) # casts val as a float
    bool(val) # casts val as a boolean (True if non-zero/non-empty, else False)

# Numerical Conversion Functions:
    bin(integer) # returns the binary representation of an integer
    oct(integer) # returns the octal representation of an integer
    hex(integer) # returns the hexadecimal representation of an integer

# Itaration-based Functions:
    all(iterable) # returns True when all elements in an iterable are true.
    any(iterable) # returns True if any element of an iterable is True
    enumerate(iterable[, start]) # returns an iterator over the indices and
        # values of an object
    range(stop)/range(start, stop[, step]) # returns the relevant range object
    filter(function, iterable) # returns an iterator over elements in the
        # iterable to which the given function returns True
    len(container) # returns the number of items/elements in a container data
        # type/iterable
    next(iterator[, default]) # returns the next element from the iterator
    reversed(iterable) # returns reversed iterator of a sequence
    sorted(iterable) # returns a new list containing a sorted list of the
        # initial iterable

# Object/Class Functions:
    callable(obj) # checks if obj is callable (a function)
    delattr(obj, attribute) # deletes the specified attribute from the object
    getattr(obj, attribute) # returns the value of the named attribute of obj
    hasattr(obj, attribute) # checks if obj has an attribute with the given name
    dir(obj) # tries to return the attributes of obj
    help(obj) # invokes the built-in Help System
    isinstance(obj, class) # checks if obj is an instance of class
    issubclass(obj, class) # checks if obj is a subclass of class
    super() # allows access to superclass methods and attributes
    str(obj) # returns an informal representation of obj
    repr(obj) # returns a printable representation of obj
    type(obj) # returns the type/class of obj
    iter(iterable) # returns an iterator for an object
    
# Miscellaneous Funtions:
    print(string) # prints the specified string to the console
    input(message) # requests a console input with the given message
    open(filename, mode) # opens a file in the specified mode



# ----- NOTE: Additional Functions ----- #
'''
    There are various additional inbuilt functions, details of which, along
    with extra details of the presented functions, can be found online. Some
    of the given functions will be explained in greater depth in lessons
    covering related topics.
'''




#-------------------------- USER DEFINED FUNCTIONS ----------------------------#
'''
    While inbuilt functions and datatypes tend to form the basis of the majority
    of code, these are complemented by user-defined Classes and functions.
    Python uses the keyword 'def' to define a new function, with details of
    each function to be written in the initial comment, later forming the basis
    for how the 'help' and 'dir' functions describe the function.

    Descriptive comments at the start of a function are known as the function's
    documentation, and should describe what the function does, including any
    inputs it takes and outputs it generates or changes it causes. It is
    important not to describe the method by which a function works in its
    documentation, because doing so restricts the programmer's potential to
    reimplement a function with more efficient code at a later date, and can
    also at times present security issues.

    Functions also have what is known as a return value, which can be either
    nothing, represented by the 'None' type, or some relevant variable useful
    to specify the result or effects of the function. Return value types are
    given in the starting comments of a function, and within a function the
    return value follows the 'return' keyword.

    Some example functions, with appropriate documentation, are provided below.
'''

# Example function 1 (no inputs, no outputs)
def my_func_1():
    ''' One-line briefly describing what the function does.

    More in-depth description of the function's purposes and different ways in
        which it can be used.

    my_func_1(None) -> None
    (function_name(datatype of inputs) -> Return type/s)
    '''

    <relevant function code>


# Example function 2 (one input, one output)
def my_func_2(input_var):
    ''' Returns something useful based on the specified input_var.

    my_func_2(str) -> bool
    '''

    <relevant function code>
    if something:
        return True
    else:
        return False



# ----- NOTE: Inputs and Outputs ----- #
'''
    Functions can have any number of inputs, and can return either nothing or
    some version of any other datatype. This includes user-defined datatypes,
    as well as lists and tuples which can contain a number of different
    variables and/or values.

    Input values which are mutable can often be modified within the function
    they are passed to, resulting in changes outside of the function as well.
    Immutable input objects, on the other hand, cannot be modified, so passing
    an immutable object into a function cannot result in modifications to that
    object within the function propagating outside the function's operation
    time.

    The way this works is that immutable objects are passed into a
    function as a value, known as "pass-by-value' passing, and a local variable
    is created within the function to store this value. Any changes to this
    variable then do not affect the inputted variable unless the value of the
    local variable is returned from the function and set as the new value for
    the initial variable. Note that the local variable and the passed in
    variable are permitted to have the same name, which is cause for some
    confusion among many a programmer expecting the two variables to be the
    same thing.

    Mutable objects, on the other hand, are passed in as references to the
    memory where the initial value is stored, meaning the created local variable
    has access to the same memory space as the inputted variable. This means
    that data can be modified from within the function, and when it is re-
    accessed from outside the function the modified data is displayed, since
    the memory itself has been changed, not just where a certain variable
    points.
'''

# ----- NOTE: Return Keyword ----- #
'''
    At any point in a function, the return keyword will end the function where
    it is encountered, ignoring any subsequent code (irrespective of whether or
    not it is followed by an intended return value. It is also worth noting that
    using the return keyword is not necessary in functions where no value is
    returned, in which case the function will end when the last of its code is
    run.
'''

# ----- NOTE: Default Values ----- #
'''
    Functional inputs can have default values, as specified by an equals (=)
    sign, allowing for users to optionally set or ignore a particular input.
    These should be placed after any standard inputs, so parameters entered by
    the user are not assumed to be the optional ones, thus leaving one or more
    required inputs empty.
'''


# Example of a function with an optional input
def my_func_3(input_var, optional_var=False):
    ''' Uses an optional input (default False), returns something cool.

    my_func_3(str, bool) -> str
    '''

    <relevant function code>
    return output_str



# ----- NOTE: Unspecified Inputs ----- #
'''
    Beyond the standard defined inputs, it is also possible to enable a user
    to input an unspecified number of their own inputs to a function, either
    in the form of variables, or key-value pairs. This is done using the words
    *args and *kwargs respectively, for "unspecified arguments" and "unspecified
    key-word arguments". These must be placed last in the functional input list,
    because there is no delimiting character to denote the end of the
    unspecified values.

    The values within *args and *kwargs can then be accessed by iterating over
    *args or over the keys of *kwargs.
'''


# Example of a function with unspecified inputs
def my_func_4(input_var, *args, *kwargs):
    ''' Prints out all provided inputs in a pretty-print format.

    my_func_4(str, *args, *kwargs) -> None
    '''
    print("Initial value:", input_var)
    # Prints a new-line, before printing the variables in *args
    print("\n*args:")
    for argument in *args:
        print(argument)
    print("\n*kwargs:")
    for key, value in *kwargs:
        print(key, '=', value)
    

    

#------------------------------ LAMBDA FUNCTIONS ------------------------------#
'''
    Lambda functions are essentially short, one-line functions with no name.
    They are user-defined, and tend to be used in places where a function is
    required, but its behaviour is relatively simple, and calling it by name
    is not required at any point. This is most commonly required in conjunction
    with the 'map', 'filter', and 'reduce' functions, which allow effective
    comprehension of lists, in terms of elementwise operations and filtering.
    Detailed explanations of these functions can be found online, and will not
    be covered in this course. 

    Additionally, a lambda function can be used where a function is required,
    but parameter input is desired without calling said function in the process.
    This is common practice in things such as event bindings, which will be
    covered in greater depth in a later lesson.
'''

# Example lambda function
lambda x, y : x + y



# ----- NOTE: Accessing ----- #
'''
    While lambda functions are commonly anonymous (without a name), it is
    possible to assign a lambda function to a name when it is defined, or
    to set it as a stored value in any form of container data-type (e.g. list,
    tuple, dictionary, etc.). This may seem somewhat counterintuitive, but
    allows the programmer to specify short functions without the usually
    required documentation and commenting overheads which can be preventative
    to rapid development of programs.

    If a function is required throughout a program, but is not intended to be
    accessible to users, defining it as a lambda function allows it to avoid
    appearing in comprehensible documentation altogether.
'''

# Example of naming a lambda function
my_lambda_func = lambda x, y : x + y

# Example of setting a lambda function as a list element
my_list = [
    lambda x : x + 3,
    lambda x, y: x / (y - (x % 4))
    ]



# ----- NOTE: List Comprehension ----- #
'''
    Lambda functions are a common source of struggle and confusion amongst
    beginning programmers, but the list comprehension aspects, namely the usage
    of lambda functions in conjunction with 'map', 'filter', and 'reduce', can
    be entirely substituted with python's own list comprehension syntax. This
    syntax extends to both generators and sets, and can be used to great effect
    by programmers competent in its nuances.

    Given the relative complexity of list comprehension features, combined with
    the limited usage in the average program, this syntax is left out of this
    course, and can be further studied online by interested students.
'''
    



#-------------------------------- ABSTRACTION ---------------------------------#
'''
    An essential aspect of programming, and indeed of much of modern
    technological or, more generally, technical work, is abstraction. This is
    the process by which a specific idea or action is considered in a more
    general case. Mathematically this is realised through the substitution of
    numerical values with algebraic formulae, and programatically this can be
    perfomed through avoiding unnecessary restrictions on user input, and the
    domain over which each function is specified.

    A common realisation of this principle is to try to ensure each function has
    only one purpose, and that where possible code should be reused from
    external sources as opposed to being rewritten by the programmer. While
    understanding can often be greatly improved by finding solutions to problems
    which have already been solved, this should take place when there is ample
    time and opportunity to do so. If solutions are required to new problems,
    existing code should be used where circumstances permit, and often it's
    beneficial to use code that is known to work well without having to write
    every program from the absolute bottom up.
'''

