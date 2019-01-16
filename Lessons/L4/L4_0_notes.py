#!/usr/bin/env python3
################################################################################
#                                                                              #
#                                   Lesson 4                                   #
#      Functional Programming, Functions, List Comprehension, Abstraction      #
#                                                                              #
################################################################################




#--------------------------- FUNCTIONAL PROGRAMMING ---------------------------#
'''
    Python is what is known as a hybrid language, allowing for both functional
    and object-oriented programming. Functional programming is based off sets
    of functions, which can run other functions in the same file, or functions
    which have been imported to the file. Usually a program has some 'main'
    function which runs the other functions in the desired sequence. In
    contrast, object-oriented programming is based off the idea of separate
    objects, all with their own properties (stored variables) and methods
    (related functions).

    This lesson will focus on the basics of functions and functional
    programming, with object-oriented programming covered in lesson 6.
'''




#------------------------------ INBUILT FUNCTIONS -----------------------------#
'''
    To begin with, Python includes a number of inbuilt functions (coloured
    purple by default, if using the IDLE editor). Some of these have been used
    already, in earlier lessons, but the following list provides a brief
    description of the most widely used ones.
'''



# Mathematical Functions
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


# Typecasting Functions
'''
    Typecasting occurs when the user wishes to explicitly declare a variable as
    of a given type, or convert it to the specified type if possible. Given
    this is explicitly user performed, any associated data-loss (e.g. in the
    truncation of a float to an integer [int(1.9) -> 1]) is assumed to be
    intentional, without warning given. At times python may throw errors,
    however, if necessary attributes of a variable are not present when casting
    to another type.
'''
    int(val[,base=10]) # casts val as an integer, with optional base specified
        # val is float -> truncates, val is string -> optional base
    float(val) # casts val as a float
    bool(val) # casts val as a boolean (True if non-zero/non-empty, else False)
    list(iterable) # casts the iterable as a list
    tuple(iterable) # casts the iterable as a tuple
    set(iterable) # casts the iterable as a set (unique set of elements)
    dict(mapping) # casts the key, value pairs of the mapping as a dictionary


# Numerical Conversion Functions
    bin(integer) # returns the binary representation of an integer
    oct(integer) # returns the octal representation of an integer
    hex(integer) # returns the hexadecimal representation of an integer


# Itaration-based Functions
    all(iterable) # returns True when all elements in an iterable are True.
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


# Object/Class Functions
    callable(obj) # checks if obj is callable (as a function)
    delattr(obj, attribute) # deletes the specified attribute from the object
    getattr(obj, attribute) # returns the value of the named attribute of obj
    hasattr(obj, attribute) # checks if obj has an attribute with the given name
    dir(obj) # tries to return the attributes of obj
    help(obj) # invokes the built-in Help System
    isinstance(obj, class/tuple) # checks if obj is an instance of class or one
        # of the classes in the tuple of classes
    issubclass(obj, class/tuple) # checks if obj is a subclass of class or one
        # of the classes in the tuple of classes
    super() # allows access to superclass methods and attributes
    str(obj) # returns an informal representation of obj
    repr(obj) # returns a printable representation of obj
    type(obj) # returns the type/class of obj
    iter(iterable) # returns an iterator for an object


# Miscellaneous Funtions
    print(string) # prints the specified string to the console
    input(message) # requests a console input with the given message
    open(filename, mode) # opens a file in the specified mode


# ----- NOTE: Additional Functions ----- #
'''
    There are various additional inbuilt functions, details of which, along
    with extra details of the presented functions, can be found online. Some of
    the given functions will be explained in greater depth in lessons covering
    related topics.
'''




#------------------------------ CUSTOM FUNCTIONS ------------------------------#
'''
    While inbuilt functions and datatypes tend to form the basis of the
    majority of code, these are complemented by Classes and functions defined
    by you and other programmers. Python uses the keyword 'def' to define a new
    function, followed by the function name, and any input variables it takes.

    Descriptive comments at the start of a function are known as the function's
    docstring (documentation), and should describe what the function does,
    including any inputs it takes, outputs it generates, changes it causes, and
    how the function should be run. The docstring forms the basis for how the
    'help' and 'dir' builtin functions describe the function to users. It's
    important not to describe a function's implementation details in its
    documentation, because doing so restricts your potential to reimplement it
    later, and can also present security issues, or encourage others to use the
    function in ways it's not intended for.

    Functions also have a 'return value', which can be nothing (None), or some
    relevant result or status indication. Return value types are specified in
    the docstring of a function, as part of the 'how to run' code, and within a
    function the return value follows the 'return' keyword.

    Some example functions, with appropriate documentation, are provided below.
'''



# Example function 1 (no inputs, no outputs)
def my_func_1():
    ''' One line briefly describing what the function does.

    More in-depth description of the function's purposes and different ways in
        which it can be used.

    my_func_1() -> None
    (function_name(datatype of inputs (if any)) -> Return type/s)

    '''

    <relevant function code>


# Example function 2 (one input, one output)
def my_func_2(input_var):
    ''' Returns something useful based on the specified input_var.

    my_func_2(str) -> bool

    '''

    <relevant function code>
    if <something to do with input_var>:
        return True
    else:
        return False


# ----- NOTE: Inputs and Outputs ----- #
'''
    Functions can have any number of inputs, and can return either nothing or
    some version of any other datatype. This includes custom datatypes, as well
    as lists and tuples, which can effectively output several values
    simultaneously.

    Lessons 1 and 3 touched on mutable and immutable datatypes, where mutable
    values allow for internal modification, without being replaced, whereas
    immutable values cannot be changed. This has to do with memory pointers
    (references), whereby an immutable value is from a direct pointer to a
    place in memory where data is stored, whereas a mutable value stores one or
    more pointers to other mutable or immutable values. The mutable value
    pointer(s) can be redirected, so when a variable storing the mutable value
    is accessed, from anywhere in the code, it can then access the current
    stored values, and change them if desired.

    With functions, mutable inputs allow a function to change values from
    outside of itself without needing to return anything. Effectively, a
    'reference' to the outside object is passed into the function and assigned
    to a local variable, which stops existing once the function ends.
    Modifications inside the function (to the local variable) can occur to the
    data being referred to, however, which is also being referred to outside
    the function. This is known as 'pass by reference'.

    Immutable inputs, on the other hand, cannot be modified, so passing an
    immutable object into a function means changes to the object inside the
    function have to occur by replacing it with modified copies, in which case
    the modifications aren't accessible after the function has been run, unless
    the modified object is returned. This is known as 'pass by value', because
    the value is assigned to the local variable, which the code outside the
    function doesn't have access to.
'''

# ----- NOTE: Polymorphism ----- #
'''
    Polymorphism in a programming language is the ability for functions to
    optionally accept multiple types of input. Python is implicitly polymorphic
    in that functions are not required to specify the type of input variables
    they accept, and Python does not (by default) check the type of inputs to a
    function when running a program. This generally makes for simpler coding,
    but also means that if an input of an invalid type for a function is used,
    the program can sometimes throw an error and stop execution.

    Python's implicit polymorphism also comes with benefits, however. Robust
    Python programs can allow for multiple valid input types, and effective
    error handling can be used to present users with error messages informing
    them of allowable input types and why their input was invalid.
    Additionally, different computer hardware may assign different amounts of
    memory to different variable types. This can be problematic if code is
    explicitly written to only allow, for example, numbers of a certain size,
    but a Python program can instead allow a function to accept all integers,
    and the program interpreter abstracts the memory considerations away from
    the programmer.

    To ensure users are able to input valid inputs to a function, if inputs of
    a certain type are required they should be specified in the function's
    docstring.
'''

# ----- NOTE: Local vs Global Namespace ----- #
'''
    Note that inside a function is a local namespace. This means that a
    function can access variables and functions defined outside it (these are
    known as 'global' to the function), but variables (and functions) defined
    inside a function cannot be accessed outside of it, unless they are
    returned, or placed inside a mutable value passed in or global to the
    function. Files, functions, and classes each have their own namespace, and
    can access the namespace of things that contain them, but not of things
    they contain. This means a variable inside and outside of a function can
    have the same name, but if the variable inside the function is set as equal
    to something, it becomes local to the function, and is therefore not
    accessible by the same variable name outside the function.
'''

# ----- NOTE: 'return' Keyword ----- #
'''
    At any point in a function, the return keyword will end the function where
    it is encountered, ignoring any subsequent code. If the return keyword is
    used without a specified return value, 'None' is returned. It is also worth
    noting that using the return keyword is not necessary in functions where no
    value is returned, in which case the function will automatically return
    None when the last of its code is completed.
'''

# ----- NOTE: Default Values ----- #
'''
    Function inputs can have default values, specified by an equals (=) sign,
    allowing for users to optionally set or ignore a particular input. These
    should be placed after any standard inputs, so parameters entered by the
    user are not assumed to be the optional ones, thus leaving one or more
    required inputs empty.

    Any optional inputs should be denoted by a preceding asterisk (*) in the
    function calling code in the docstring (as below).
'''



# Example of a function with an optional input
def my_func_3(input_var, optional_var=False):
    ''' Uses an optional input (default False), returns something cool.

    my_func_3(str, *bool) -> str

    '''

    <relevant function code>
    return output_str


# ----- NOTE: Unspecified Inputs ----- #
'''
    Beyond the standard defined inputs, it is also possible to enable a user to
    input an unspecified number of their own inputs to a function, either in
    the form of normal inputs, or key-value pairs. This is done using one and
    two asterisks in front of variable names respectively, for "unspecified
    arguments" and "unspecified key-word arguments" (e.g. *args and **kwargs).
    Note that optional arguments with defaults specified by an equals (=) sign
    are considered to be keyword arguments. All standard arguments must be
    placed before all keyword arguments, and all unspecified inputs must be
    placed after specified (required or default) inputs, because there is no
    delimiting character to denote the end of the unspecified values. Keyword
    arguments can be in any order, because the purpose of each value is
    identifiable by its key. *args and **kwargs are common variable names to
    use for undefined inputs when the variables have no particular predefined
    meaning. In examples where the additional values have some predefined
    purpose, more meaningful variable names can be used.

    The values within *args and **kwargs can then be accessed by iterating over
    args or over the keys of kwargs.
'''



# Example of a function with unspecified inputs
def my_func_4(input_var, *args, my_default=True, **kwargs):
    ''' Prints out all provided inputs in a pretty-print format.

    my_func_4(str, *args, *bool, **kwargs) -> None

    '''
    print("Initial value:", input_var)
    # Prints a new-line, before printing the variables in *args
    print("\n*args:")
    for argument in args:
        print(argument)
    print("\n**kwargs:")
    for key in kwargs:
        print(key, '=', kwargs[key])

# how to call my_func_4 (default value left as default)
my_func_4('first',2,3,'four',5.0,first_kwarg=0,key='value',etc='and the rest')


# Dereferencing with Asterisks
'''
    Asterisks can also be used to turn an iterable or mapping variable into
    inputs to a function. This is useful when passing inputted unspecified
    inputs into another function to be dealt with, or when transforming a
    list/tuple or dictionary into an ordered set of function inputs.

    Try running the following example and see if you can understand how it
    works.
'''

def my_print(*objects, **kwargs):
    ''' Print each object in objects, and each key-value pair in kwargs.

    my_print(*obj) -> None

    '''
    extra_stuff = ['this', 'is', 'kinda', 'cool']
    print('My print printed: ', *objects, *extra_stuff)
    for key in kwargs:
        print(key, kwargs[key])
    
# to dereference a dictionary into keyword arguments, keys must be strings
my_dict = {'great':True, 'stuff':'weee', 'me':'too'}
my_print('How cool is this?', 'pretty great', **my_dict)




#------------------------------ LAMBDA FUNCTIONS ------------------------------#
'''
    Sometimes you have a one line, reasonably self-evident function, and you
    don't feel like documenting it would be helpful or necessary. The 'lambda'
    keyword allows you to do just this - you can define a one line function
    with no documentation, and all it needs is somewhere to live. Unlike a
    function defined with 'def', lambda functions can be completely anonymous -
    they don't need a name. Instead, creating a lambda function returns a
    function instance, which can be assigned to a name (like a normal
    function), or could be put in a list, or a dictionary, or anywhere you want
    it stored.

    Most commonly, lambda functions are required in conjunction with the 'map',
    'filter', and 'reduce' functions, which allow effective comprehension of
    lists, in terms of element-wise operations and filtering. Detailed
    explanations of these functions can be found online, and will not be
    covered in this course. Additionally, a lambda function can be used where a
    function is required, but parameter input is desired without calling said
    function in the process. This is common practice in things such as event
    bindings, which will be covered in greater depth in a later lesson.

    If a function is required throughout a program, but is not intended to be
    accessible to users, defining it as a lambda function allows it to avoid
    appearing in comprehensible documentation altogether.
'''



# 'def' vs 'lambda'
# assigning to a name
def my_func(*input_vars):
    ''' Wrapper for the builtin print function '''
    print('mine', *input_vars)

my_func = lambda *input_vars : print('mine', *input_vars)

# assigning somewhere else
my_list = [1,2,3]
my_list[0] = my_func # if defined already, by either method
my_list[1] = lambda x,y : x+y

# calling the functions
my_func('testing this', 'one:', 1) # either definition
my_list[0]('testing this', 'two:', 2)
my_list[1](1,2) # returns 3




#----------------------------- LIST COMPREHENSION -----------------------------#
'''
    Lambda functions are a common source of struggle and confusion amongst
    beginning programmers, but the list comprehension aspects, namely the usage
    of lambda functions in conjunction with 'map', 'filter', and 'reduce', can
    be entirely substituted with python's own list comprehension syntax.

    Given the relative complexity of list comprehension features, combined with
    the limited usage in the average program, only the basic syntax is covered
    in this course, which can be further studied online by interested students.
'''



# Basic List Comprehension
'''
    Think of list comprehension as a way of turning an iterable into a list,
    usually with some kind of filter applied. The general syntax is:
'''
my_list = [<element_expr> for element in <iterable> if <filter_expr>]
'''
    where element_expr is the result added to the list, and filter_expr is some
    boolean expression relevant to 'element' (can be a function which returns a
    boolean). The resultant list is set as element_expr applied to all elements
    in the iterable that match the filter expression. As an example,
    'my_double_evens' (below) is set as double the value of all the even
    integers between 0 and 19, inclusive. If 'range(20)' was replaced with a
    list variable, my_evens would be double all the even numbers in that list.
    'num_threes' uses more memory than a traditional loop, but counts the
    elements in an iterable that matched a condition in a single line of code.
'''
my_double_evens = [2*num for num in range(20) if num % 2 == 0]

num_list = [1,4,2,3,6,3,8,3,5,6,3,9,0]
num_threes = len([val for val in num_list if val == 3]) # num_threes = 4


# ----- NOTE: Set Comprehension ----- #
'''
    The same syntax can be used for 'set comprehension', which works the same
    way as for lists, just with sets, which are like lists but every element is
    unique. A list can be typecast into a set, using set(my_list), which
    removes any duplicate elements. A set is created with curly-braces (e.g.
    {1,2,3}), and set comprehension is just list comprehension syntax with
    curly-braces instead of the square-brackets used by lists.
'''




#--------------------------------- ABSTRACTION --------------------------------#
'''
    An essential aspect of programming, and indeed of much of modern
    technological or, more generally, technical work, is abstraction. This is
    the process by which a specific idea or action is considered generally, as
    opposed to as a specific case. Mathematically this is realised through the
    substitution of numerical values with algebraic formulae, and
    programatically it can be performed with functions which avoid unnecessary
    restrictions on user input and the domain over which each function is
    specified. So-called 'hard coding' fails to use abstraction, and
    accordingly fails to allow for general behaviour, so should be avoided
    where possible. Generalised behaviour means the same code can be used for
    multiple purposes, which means code written once can be used in multiple
    programs, and less code needs to be written in the long term.

    Commonly, useful abstraction can be encouraged by trying to ensure each
    function has only one purpose, and that where possible code should be
    reused from external sources as opposed to you developing and writing all
    your code yourself. While understanding can often be greatly improved by
    personally solving problems which have already been solved by others, this
    should take place when there is ample time and opportunity to do so. If
    solutions are required to new problems, existing code should be used where
    circumstances permit. It's often beneficial to use code that is known to
    work well without having to write every program from the absolute bottom up.

    To reinforce the point, python itself is several layers of abstraction away
    from the actual hardware being programmed, which allows millions of people
    to write computer programs that work across billions of devices and can
    even be run directly through internet browsers. Without those abstractions
    we'd be left writing in binary, attempting to talk directly to the computer
    in a language it understands, instead of one that humans understand.
    Further, without the hardware abstractions provided by computer designers
    and manufacturers, we'd likely still be flipping individual switches in
    circuits.
'''
