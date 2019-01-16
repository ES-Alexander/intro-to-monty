#!/usr/bin/env python3
################################################################################
#                                                                              #
#                                   Lesson 1                                   #
#        'Hello World', General Introduction, Commenting, and Variables        #
#                                                                              #
################################################################################




#--------------------------------- HELLO WORLD --------------------------------#
'''
    A common programming convention when starting a new project or learning
    experience is to check that your system is set up and running as intended.
    This is often referred to as the 'hello world' protocol, where you get your
    machine to tell you it's communicating as desired. In Python, this can be
    done by opening a console (IDLE or some other option) and typing the
    command "print('hello world')", then pressing enter. It's also possible to
    just type in the string 'hello world', because Python automatically prints
    back any values entered in the console.

    Once you've run your 'hello world' and are happy the computer is talking to
    you, you can return to these lesson notes.
'''




#---------------------------- GENERAL INTRODUCTION ----------------------------#
'''
    This course is intended for people wanting to learn python syntax, as well
    as several more general programming principles as we go. If you have
    already learnt to program in another language (or even in Python), the
    principles are likely the most interesting aspects to you. The exercises in
    the first few lessons are quite simple, so will be most useful to beginner
    programmers who haven't programmed at all before, or as a refresher of
    basic programming ideas.

    Reiterating the README file, the course has been written and developed for
    use in Python IDLE. Using any other shell is perfectly fine, and all
    features should still work, but some descriptions may be less clear. If you
    have access to a Python shell, and are able to edit, save, and run .py
    files, you should be mostly fine. With IDLE open, new and existing files
    can be opened from the File menu in the menubar at the top of your window
    (on Windows or Linux) or the top of your screen (on Mac). Files can also be
    saved from the File menu. To run a file (while you're in it), use the Run
    menu, and select Run Module (or use the shortcut F5).

    In general, there will be 3 files of interest per lesson. The first is
    LN_0_notes.py, which is where the notes are stored. The second is
    LN_1_exercises.py, where you will find exercises based off the content
    covered in the notes and up to that point in the course. The third is
    LN_2_exercise_checker.py, which is where automated tests for the exercises,
    as well as sample solutions (at the bottom of the file) can be found. Note
    that running the exercise file will run the tests on your attempt at the
    exercises. Running the exercise_checker file will instead run the tests on
    the provided sample solution.

    Significant effort has been put into making useful exercises to accompany
    the notes in each lesson, as well as automated tests to give you feedback
    as you complete the exercises. These tests are written to cover as much of
    the specified functionality as possible, while still giving you room for
    some creative freedom to explore the language. If you have any questions or
    concerns regarding the exercises or tests, feel free to raise an issue on
    the GitHub repository where this course is stored
    (ES-Alexander/intro-to-monty), or contact me directly at
    'sandman.esalexander@gmail.com'. The same applies for any other course
    feedback or suggestions you might have.
'''




#--------------------------------- COMMENTING ---------------------------------#
'''
    Commenting is one of the most essential aspects of any program. Well-
    commented code should be both readable and maintainable, with sufficient
    comments provided that a suitably experienced programmer can read your code
    and understand its purpose and functions without requiring additional
    explanation or experimentation.

    In Python, single line comments are created using the hash (#) symbol,
    after which the rest of that line is commented out. These are used to
    describe what comes directly afterwards, or if used at the end of a line
    describe the line they're on. Any confusing code that is easily explained
    should be explained using single line comments.

    Multi-line comments require both start and end markings, and are created
    using triples of single OR double quotations, as below.
'''



# Commenting Types
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


# ----- NOTE: Section Commenting ----- #
'''
    A useful note with commenting out sections is you can use commenting
    symbols in such a way so as to not have to delete them if you want to
    repeatedly comment out sections of code. This can be done as follows:

    # """
        <commented out code goes here>
    # """

    Turn on the commenting by removing the first hash symbol, and turn it off by

    adding it back in.
'''

# ----- NOTE: Line Length ----- #
'''
    Coding conventions dictate line length should not be longer than 80
    characters. This is to enable viewing on smaller screens, and also makes
    your code look neat. The Python IDLE window is by default sized to 80
    characters wide (in mono-spaced font) upon opening, but the "Col" indicator
    in the bottom right corner also tells you which character you're up to in a
    line.
'''




#---------------------------------- VARIABLES ---------------------------------#
'''
    Variables are used in programming to store values or as references to
    certain objects or properties. All programming languages have different
    variable types, but in Python these types are specified by implication from
    the data used to define the variable. Additionally, different naming
    conventions are often used depending on the language and programmer, namely:

    - lower camel case (lowerCamelCaseVariableName)
    - upper camel case (UpperCamelCaseVariableName)
    - underscore separated (underscore_separated_variable_name)
    - various capitalisations using underscore separated

    We will use underscore-separated names for both variables and functions.

    Variable names should be descriptive of the thing they represent so that
    code can be readable, and to minimise having to return to where a variable
    was defined to find out what it is supposed to be and do.
'''



# Variable Declaration and Definition
'''
    In Python, defining a variable also 'declares' it to the computer -
    effectively saying 'I am a variable, please remember my name for later'.
    Some programming languages have declaration separate to definition, but in
    Python all variables are declared when they are first defined.

    Just like when you're reading, the computer doesn't know about things
    written in your code until it's passed them, so make sure you define your
    variables before you try to use their values.

    Variables are defined as below, with examples provided of various different
    data-types available in python, and the symbols and syntax used to define
    them.
'''

zero = 0 # generic variable definition

# Integer:
my_int = 0

# Float (decimal number):
my_float = 1.3

# None (nothing here)
nothing = None

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


# ----- NOTE: Methods and Properties ----- #
'''
    Everything in Python is treated as an object, with its own methods
    (functions, things you can do to act on it, or to get information from it),
    and properties (data it stores). This will become more important later, but
    for now just understand that different variable types support different
    methods, and hold different properties to one another. This makes sense,
    since it it illogical to try to multiply strings together, but multiplying
    numbers is perfectly natural.

    To find the available properties and methods of an object in python, use
    the 'help' function, calling it with help(object) in IDLE or another python
    console/terminal window. In the case of the basic python datatypes, they
    can be referenced as 'int' (integer), 'float' (decimal number), 'bool'
    (True/False boolean), 'str' (text string), 'list' (list of objects),
    'tuple' (unchangeable list of objects), and 'dict' (dictionary of key-value
    pairs) (e.g. help(int)).

    Once a variable has been defined in python, inputting its name to the IDLE
    terminal/console will display its value. It can also at times be useful to
    use the print function, using print(variable_name). Additionally, the
    'type' function returns the type of the inputted object or variable, as in
    type(var_name).
'''

# ----- NOTE: Mutability ----- #
'''
    A datatype is 'mutable' if it has stored values which can be changed. While
    it is always possible to redefine a variable, changing a value without
    redefining the variable is not always possible. All the builtin datatypes
    which can't store other variables are immutable, and cannot be changed once
    defined. This includes integers, strings, floats, booleans, and None.
    Dictionaries and lists are mutable, so their stored values can be changed
    after they've been defined. A tuple is like an immutable list, so it must
    keep the values it's defined with. Note that if a mutable value is stored
    inside a tuple, the values inside that can still be accessed and modified.
'''
