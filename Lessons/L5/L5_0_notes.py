#!/usr/bin/env python3
################################################################################
#                                                                              #
#                                   Lesson 5                                   #
#          File Types, User Input, String Formatting, Searching/Regex,         #
#                               Imports/Packages                               #
#                                                                              #
################################################################################




#--------------------------------- FILE TYPES ---------------------------------#
'''
    Text files, with the extension .txt, are un-formatted files containing only
    text, which makes them incredibly versatile for the transfer of data, but
    difficult to extract data from without a well-defined format. A more
    structured file type is the JSON format, (.json), which is made with the
    intention of storing data objects with particular properties, allowing
    key-value pairs, arrays, and a number of other fundamental datatypes. A
    simpler file-type used mainly for storing tabulated data is the CSV, or
    comma-separated value file (.csv).

    Extracting information from a document ('parsing') can be performed in a
    variety of ways. The most important attribute of a file to parse is that
    its format is one the parsing program or script is able to accept. While
    CSV and JSON files are commonly accepted structures, they are, at base,
    comprised of just formatted text, and basic text files can be structured in
    practically any way the programmer desires.
'''



# Opening Files
'''
    Files can be opened in Python using the 'open' function, which accepts a
    filename and an opening mode. Opening modes include 'r' for reading, 'w'
    for writing (deleting any existing file with the same name), 'a' for
    appending (writing to the end of an existing file, or starting a new one if
    the filename doesn't already exist), along with a number of other options
    which can be found using the inbuilt help function.

    It is essential to close any open files (using file.close()) at the end of
    any operations on it, so as to avoid damaging files by attempting to access
    them from multiple places while open in a program.
'''

my_file = open('filename.txt', 'r')

<code>

my_file.close()


# Opening Files (the 'Pythonic' way)
'''
    The open-close method of opening files intuitively makes sense, but
    forgetting to close a file can cause issues with other programs,
    particularly if your program runs for long periods of time. Python also
    includes a method of opening files using a 'context manager'. To start a
    context manager, open it using a 'with' statement (like an 'if' statement
    for a context), and it will automatically clean up at the end of the
    indented block. You can assign the context you've opened to a variable
    using the 'as' keyword. This is the safest way to open a file, because the
    'with' block will make sure the file gets closed, even if an error occurs
    while reading it.
'''

with open('filename.txt', 'r') as my_file:
    # the file is open while in this block
    <code parsing/processing data from file>

# file is closed automatically




#---------------------- READING FROM AND WRITING TO FILES ---------------------#
'''
    Once a file has been opened it can be read from or written to (depending on
    the opening mode). This can be accomplished using the 'read', 'readline',
    and 'write' functions, as below.
'''



# 'read' and 'readline' Functions
'''
    The 'read' function will read the entirety of a file (from the current
    point) as a single string, to be separated and parsed as desired.
    'readline' reads only a single line at a time, and is often quite useful
    when parsing of each line is required. It is also possible to iterate over
    a file, which reads one line per iteration.
'''
with open('filename.txt', 'r') as remaining_lines:
    first_line = remaining_lines.readline()
    second_line = remainng_lines.readline()
    all_the_rest = remaining_lines.read()

with open('filename_2.txt', 'r') as my_other_file:
    for index, line in enumerate(my_other_file):
        print('LINE {}: '.format(index) + line)


# 'write' Function
with open('filename.txt', 'w') as new_file: # overwrite mode
    new_file.write('This is the first')
    new_file.write('line in my file.\n')
    new_file.write('This is another line in my file.\n')

with open('filename2.txt', 'a') as existing_file: # append mode
    existing_file.write('This is a line at the end of my file.\n')


# 'read', parse, 'write'
with open('filename.txt', 'r') as input_data,
        open('output.txt', 'w') as output_data:
    for line in input_data:
        output_data.write('Input: ' + line)


# ----- NOTE: Newlines ----- #
'''
    Python uses '\n' as the newline character, so when writing to a file it is
    important to include '\n' at the end of each line you write.
'''

# ----- NOTE: Closing Files ----- #
'''
    While it is important to close files after using them, if a file is needed
    multiple times within a short space in a script, it is often beneficial to
    leave the file open until you're finished using it, at which point it can
    be closed. Wherever possible, make sure your files are closed when you are
    finished with them, especially before the function you opened them in
    returns.
'''

# ----- NOTE: Streams and Seeking ----- #
'''
    Using the 'open' function returns a file stream, which goes from the top to
    the bottom of the file. If you read part of a file, the stream is moved to
    the position you have reached, so if you want to access a part of the file
    you have already passed you will need to use the 'seek' method of the
    stream to go backwards, or you can close and reopen the file to start again
    from the top. Generally it is best to avoid this by saving parts of the
    file you are interested in to variables so you can refer back to them
    quickly and easily.
'''




#--------------------------------- USER INPUT ---------------------------------#
'''
    While files are one type of possible user-input, Python also provides a
    dedicated 'input' function, accessed through the terminal, allowing users
    to type a message which is then inputted to and parsed by the program. An
    example of this is provided below.

    Additionally, in the design of graphical user interfaces (GUIs), certain
    elements are provided to enable user input of different types. Some
    possibilities are buttons, checklists, selection boxes, and text-entry
    boxes.
'''



# Input Function Usage
'''
    The 'input' function displays the specified message string, and returns
    whatever is entered by the user, as a string.
'''
string_var = input('message_string')




#------------------------ PARSING AND STRING FORMATTING -----------------------#
'''
    Once an input has been accepted from a user, it is often necessary to
    convert the received data into a format appropriate for the intended use.
    Generally this involves splitting the input string into relevant sections,
    and typecasting each section into its required data-type. The principle and
    basics of typecasting were covered in the "inbuilt functions" section of
    lesson 4. It is extensively used in parsing situations, where data is
    passed in as a string, and usually required in some numerical or data-type
    specific format.

    Reversing the process, adding select pieces of data into set positions in a
    string can be accomplished with 'string formatting'. String formatting can
    be used whenever it's desired to specify a string with a set syntax or
    structure, and add necessary/relevant data later.

    Considerable depth of string formatting syntax and possibilities can be
    found online at pyformat.info, but a few basic examples are provided below.
'''



# General String Formatting Example
'''
    Python string formatting is achieved using curly braces ({}) within a
    string and the 'format' function to add in the data. Braces can have any
    number of parameters in them, but the simplest options are to leave them
    empty, or to number them (starting at 0). When the braces are empty, the
    format function must contain the same number of arguments as there are
    brace pairs. Numbered braces allow for specific ordering of format
    parameters, and for using each inputted value multiple times.

    Inputs can be explicit strings or other datatypes, or pre-existing
    variables.
'''
dob = 1901
'my name is {}, and I was born in {}.'.format('Iman Example', dob)
    # 'my name is Iman Example, and I was born in 1901.'

'my name is {1}, and I was born in {0}.'.format(dob, 'Iman Example')
    # 'my name is Iman Example, and I was born in 1901.'

'Hi! My name is {0}, and I was born in {1}. {1} was great!'.format('Name', dob)
    # 'Hi! My name is Name, and I was born in 1901. 1901 was great!'




#------------------- SEARCHING AND REGULAR EXPRESSIONS/REGEX ------------------#
'''
    Beyond formatting existing strings, it is also possible to search
    containers in Python, using the 'in' keyword or the 'index' or 'replace'
    functions. While these are highly useful functions in their own right, they
    become of particular benefit when applied in conjunction with pattern
    recognition in strings. This is implemented using regular expressions, or
    'regex', which allows searching for particular characters, or sets of
    characters in a particular order, as well as most conceivable patterns that
    could occur.

    Regular expressions are powerful, and can be used extensively in the
    parsing of inputted data, from either files or direct user input, and can
    also be useful in stripping out unwanted characters or expressions, or
    determining what type of information a particular string contains. The
    syntax of regular expressions is quite extensive, so is best looked at in a
    resource dedicated to the task (https://docs.python.org/3/library/re.html
    provides a good starting point).
'''



# Membership Operator ('in' Keyword)
'''
    When searching for a distinct element in a container object, or a substring
    within a string, the membership operator discussed in lesson 2 ('in'
    keyword) is the go-to check in Python. The 'in' keyword checks if a
    particular container contains at least one instance of the specified object.
'''
while 'error' in my_code:
    my_code.remove('error') # works if my_code is a list

if ';' in user_input_str:
    print("Invalid character in input, ';'.")


# 'index' Function
'''
    The 'index' function returns the first index an object was discovered at,
    within a container object, such as a list, tuple, or string.
'''
# removes the first item, and adds all the others to the end.
for item in my_list:
    if my_list.index(item) == 0:
        my_list.remove(item)
    else:
        my_list.add(item)


# 'replace' Function
'''
    The 'replace' function is only implemented for strings, and replaces all or
    an optionally specified number of occurrences of a specified substring
    within the string it is run from.
'''
my_code.replace('error', 'no error') # replace all 'error' occurrences
my_code.replace('first error', 'no error', 1) # replace just the first 'error'




#------------------------------ IMPORTS/PACKAGES ------------------------------#
'''
    Pythonic programming is strongly focussed on maintaining simplicity and
    readability in code, but it is also equally important to avoid needlessly
    recreating code which you already have access to. While it can be
    beneficial to learn to write simple code from scratch, in larger
    applications and a performance-focused environment it is often preferable
    to use code found online, from libraries or forums, or even from code
    you've previously written yourself. The principal of abstraction also
    applies here, since code is often more readable if it uses predefined
    functions from external modules than defining every function and variable
    used in a single file. If a program is getting too large, consider
    splitting it into multiple files with independent purposes. This helps
    reduce the amount to search through when you know what you're looking for,
    and also makes separate functionality easier to import and reuse elsewhere.

    A library of code in Python is known as a 'package', with Python files
    inside a package known as 'submodules'. Packages are essentially folders of
    Python files, which can be nested inside one another, and allow for
    structured collections of code with similar functionality or purpose.
    Sub-folders inside a package are 'subpackages', and free-standing Python
    files (outside any packages) are just called 'modules'.

    To make a package requires only a folder with one or more Python files in
    it, as well as a file called '__init__.py', which provides the
    initialisation code for a particular package when it is imported. Many
    packages require no separate initialisation, in which case the __init__.py
    file is still required, but it can be left empty. Generally it is good
    practice inside the __init__.py file to specify a variable called __all__,
    which is a list of the names of all the files in the package that are
    intended to be imported when a user asks to 'import all' (example at the
    end) the files of the package. Further detail on creating and accessing
    packages can be found at
    'https://docs.python.org/3/tutorial/modules.html#packages'.

    Python allows the imports of code from modules and packages, either fully
    or partially, using the 'from', 'import' and 'as' keywords, with examples
    below.
'''


# ----- NOTE: 'Module' vs 'Package' vs 'Library' ----- #
'''
    Technically a 'library' is not a defined thing, and a 'package' is just a
    special type of module which is able to contain other modules. The term
    'library' is generally used to refer to collections of code which have been
    published, and hence are available online. A library could contain multiple
    packages, or even just a single module.

    While it is useful to think of packages and modules as folders and files,
    technically they are not required to be on the file system at all, and any
    module with a '__path__' attribute is considered a package. Modules off the
    file-system can happen if a package is written and compiled in a more
    efficient programming language for higher performance, but which are still
    accessible as normal Python modules.
'''



# 'import' Keyword
'''
    'import' can be used by itself to import entire packages, after which
    submodules and elements from that package must be accessed using so-called
    'dotted module names'. In this dot notation the module name must be used
    before each function or variable, separated by a dot (.). Multiple imports
    can be performed in the same line using comma separation.
'''
import numpy, matplotlib.pyplot # import numerical Python, and plotting tools

my_array = numpy.array([1,2,3]) # creates a numerical array of [1,2,3]
matplotlib.pyplot.plot([1,2,3],[2,4,6]) # plots y=2x over domain [1,3]


# 'as' Keyword
'''
    The 'as' keyword can be used to simplify module names, allowing for imports
    with user-specified nicknames.
'''
import numpy as np, matplotlib.pyplot as plt

my_array = np.array([1,2,3])
my_plot = plt.plot([1,2,3],[2,4,6])


# 'from' Keyword
'''
    'from' is used to specify a module, from which partial imports can be
    performed. Imports with this syntax mean you don't have to use the module
    name when using the imported features. This is a positive when writing
    code, but hides the origin of the features, which can cause difficulties
    when debugging, especially if the person debugging is unaware of a relevant
    import. A programmer unfamiliar with the initial module from which imported
    objects originate may struggle to find where a particular function or
    object is defined before they realise it was imported.
'''
from tkinter import Canvas
from math import sqrt
from matplotlib.pyplot import plot

my_canvas = Canvas()
my_irrational = sqrt(2)
my_plot = plot([1,2,3],[2,4,6])


# Import All Notation
'''
    Sometimes you want full functionality of a module or package, without
    having to use the module name, or individually import each feature. Python
    allows you to import every element within a module or package by using an
    asterisk (*) instead of specifying a specific element to import. This is
    done as in:
'''
from module import *


# ----- NOTE: Module Locations ----- #
'''
    When performing an import, Python searches for the top-level module of your
    import statement in all locations available in the 'sys.path' variable.
    This variable includes where your installed libraries can be found, as well
    as your current working directory (the folder your program is being run
    from), and some other default locations. When importing from your own
    modules, the top-level module of each import must be available at one of
    the locations in the path variable. If this is not the case, you may need
    to add one or more directories to the path manually (using
    sys.path.append), or perform the import in some other way.

    To retrieve a published library and ready for importing, you can download
    and install it using Python's package manager, 'pip'. Note that the correct
    command sent to pip should complete both the download and installation for
    you.
'''

# ----- NOTE: Relative Imports ----- #
'''
    Sometimes it is beneficial to import code relative to your a file you are
    in. To import from the directory which contains your code, you can import
    from '..module_name'. Two preceding dots ('..') refers to one directory up
    in the hierarchy. Each additional dot goes one level further. Be aware,
    however, that these imports only work if the higher directories are
    accessible from your path. This can be the case if they have been manually
    added (e.g. from sys.path.append('..')), or you are running code from
    higher up the hierarchy in a set of nested packages, each containing their
    own __init__.py file.
'''



# Intra-package Referencing
# lower down the hierarchy (further nested)
from folder1.folder2.file import function1, variable1, function2

# higher up the hierarchy ('super' imports, less nested)
from .. import * # import all from one level above the current one


