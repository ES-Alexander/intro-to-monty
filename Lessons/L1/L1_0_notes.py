#!/usr/bin/env python3
################################################################################
#                                                                              #
#                               Welcome to Python                              #
#                             Here are some basics                             #
#                                   Lesson 1                                   #
#                           Commenting and Variables                           #
#                                                                              #
################################################################################




#-------------------------------- COMMENTING ----------------------------------#
'''
    Commenting is one of the most essential aspects of any program. Well-
    commented code should be both readable and maintainable, with sufficient
    comments provided that a suitably experienced programmer can read your
    code and understand its purpose and functions without requiring additional
    explanation or experimentation.

    In Python, single line comments are created using the hash (#) symbol,
    after which the rest of that line is commented out. These are used to
    describe what comes directly afterwards, or if used at the end of a line
    describe the line they're on. Any confusing code that is easily explained
    should be explained using single line comments.

    Multi-line comments require both start and end markings, and are created
    using triples of single OR double quotations, as below.
'''



# I am a single line comment, I describe what comes next
<random code here> # I am a comment describing this piece of code

'''
    I am a multi-line comment.
    I can span as many lines as desired, and am useful for complicated
    explanations, as well as things like function descriptions.
    I am ended with the same symbol I started with:
'''

"""
    I am the other type of multi-line comment. It can be useful to have two
    in order to comment out large sections that already contain other multi-
    line comments.
"""



# ----- NOTE: Section commenting ----- #
'''
    A useful note with commenting out sections is you can use commenting symbols
    in such a way so as to not have to delete them if you want to repeatedly
    comment out sections of code. This can be done as follows:

    # """
        <commented out code goes here>
    # """

    Turn on the commenting by removing the first hash symbol, and turn it off by
    adding it back in.
'''

# ----- NOTE: line length ----- #
'''
    It is worth noting that coding conventions dictate line length should not
    be longer than 80 characters. This is to enable viewing on smaller screens,
    and aso just makes the code look neat. The Python IDLE window is by default
    sized to 80 characters wide (in mono-spaced font) upon opening, but the
    "Col" indicator in the bottom right corner also tells you which character
    you're up to in a line.
'''




#--------------------------------- VARIABLES ----------------------------------#
'''
    Variables are used in programming to store values or as references to
    certain objects or properties. All programming languages have different
    variable types, but in Python these types are specified by implication from
    the data used to define the variable. Additionally, different naming
    conventions are often used depending on the language and programmer,
    namely:
        - lower camel case (lowerCamelCaseVariableName)
        - upper camel case (UpperCamelCaseVariableName)
        - underscore separated (underscore_separated_variable_name)
        - various capitalisations using underscore separated

    We will use underscore separated names for both variables and functions.

    Variable names should be descriptive of the thing they represent so that
    code can be readable, and to minimise having to return to variable creation
    points to find out what a variable is supposed to be and do.
'''

# Example of variable declaration
variable_zero = 0

'''
    The basic types of variables used in python are created as follows:
'''

# Integer:
my_int = 0

# Float (decimal number):
my_float = 1.3

# Boolean (true or false value)
my_bool = True

# String (of characters)
my_first_string = 'String 1'
my_second_string = "String 2"

# List (of any types of item/variable), changeable after definition
my_list = [3, 'random_item', "test"]

# Tuple (of any types of item/variable), set once defined
my_tuple = ('item', 4, 3.8134)

# Dictionary (using key, value pairs)
my_dict = {
    'key1': 'val1',
    'key2': 2,
    'random_key': (0,4)
    }

'''
    Different variable types support different methods and hold different
    properties. This makes sense since it is illogical to try to multiply
    strings together, but doing this with numbers is perfectly natural. To
    find the methods and properties of a variable type, use the "help" function
    in the IDLE console/terminal (these are the same thing). This is done using:
'''

help(int) # integer
help(float) # float
help(bool) # boolean
help(str) # string
help(list) # list
help(tuple) # tuple

'''
    Once a variable has been defined in python, inputting its name to the IDLE
    terminal/console will display its value. It can also at times be useful to
    use the print function, using print(variable_name). Additionally, the
    'type' function returns the type of the inputted object or variable, as in
    type(var_name).

    Two additional object types in Python are the None and NaN types. None is
    the type of a variable or reference which does not exist (is not defined)
    and NaN is used when numbers are assigned non-sensical values, and means
    "Not a number".
'''

# ----- NOTE: Mutability ----- #
'''
    Mutability is a descriptor specifying if a given variable can be changed.
    While it is always possible to redefine a variable in the local context
    (covered in lesson 2), actually changing its value is not always possible.

    This leads to different versions of variables which can and cannot be
    modified, such as lists (mutable, can be changed), and tuples (immutable,
    cannot be changed).
'''
