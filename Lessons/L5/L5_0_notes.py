################################################################################
#                                                                              #
#                                   Lesson 5                                   #
#   File Types, Typecasting, User Input, String Formatting, Searching/Regex,   #
#                               Imports/Libraries                              #
#                                                                              #
################################################################################




#--------------------------------- FILE TYPES ---------------------------------#
'''
    Text files, with the extension .txt, are un-formatted files containing only
    text, which prove highly beneficial in the transfer of data - particularly
    when written in a structure which lends itself to data extraction. A step
    up from this in structured data is the JSON file, (.json), which is made
    with the intention of storing data objects with particular properties,
    allowing key-value pairs, arrays, and a number of other fundamental
    datatypes. A simpler file-type used mainly for storing tabulated data is
    the CSV, or comma-separated value file (.csv).

    Document parsing can be performed in a variety of ways, and what's most
    important is that the files being passed into a program are of a type the
    program is able to accept. While CSV and JSON files are commonly accepted
    structures, they are, at base, comprised of just formatted text, and basic
    text files can be structured in practically any way the programmer desires.
'''



# Opening Files
'''
    Files can be opened in python using the 'open' function, which accepts a
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
    forgetting to close a file can cause issues. Python also includes a method
    of opening files using the 'with' and 'as' keywords, which automatically
    closes the files for you. This is less intuitive to use, but is safer, so
    where possible is the preferred method of reading files. In this case,
    don't try to close the file afterwards - as soon as you exit the with
    block, the file is automatically closed.
'''

with open('filename.txt', 'r') as my_file:
    # the file is open while in this block
    <code>

# file is now closed


# ----- NOTE: Program Robustness ----- #
'''
    While it is possible, and often simpler, to create a program which simply
    fails when presented with an unexpected file or file-structure, it can at
    times be beneficial to allow files of all types and structures to be
    accepted by the program, and present a controlled error message to the
    user. If the only person using the program is the programmer, then this
    kind of robustness is unnecessary, but controlled acceptance of unexpected
    values is practically essential for any code created with the intention of
    general or wide-reaching usage.
'''




#----------------------- READING AND WRITING FROM FILES -----------------------#
'''
    Once a file has been opened it can be read from or written to. This can be
    accomplished using the 'read', 'readline', and 'write' functions, as below.
'''



# 'read' and 'readline' Functions
'''
    The 'read' function will read the entirety of a file as a single string, to
    be separated and parsed as desired. 'readline' reads only a single line,
    and is often quite useful when parsing of each line is required. It is also
    possible to iterate over a file, implicitly using the 'readline' function
    at each iteration.
'''
my_file = open('filename.txt', 'r')
my_file_as_string = my_file.read()
first_line = my_file.readline()
second_line = my_file.readline()
my_file.close()

my_other_file = open('filename_2.txt', 'r')
for index, line in enumerate(my_other_file):
    print('LINE {}: '.format(index) + line)
my_other_file.close()


# 'write' Function
new_file = open('filename.txt', 'w') # empty file and write mode
new_file.write('This is the first line in my file.\n')
new_file.write('This is another line in my file.\n')
new_file.close()

existing_file = open('filename2.txt', 'a') # append to end of file mode
existing_file.write('This is a line at the end of my file.\n')
existing_file.close()


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
    be closed. Wherever possible, close a file before a program has finished
    running, or it can be left open indefinitely.
'''




#--------------------------------- USER INPUT ---------------------------------#
'''
    While files are one type of possible user-input, python also provides a
    dedicated 'input' function, accessed through the IDLE terminal, allowing
    users to type a message which is then inputted to and parsed by the
    program. An example of this is provided below.

    Additionally, in the design of graphical user interfaces (GUIs), certain
    elements are provided to enable user input of different types. These
    usually come in the form of buttons, checklists, selection boxes, or
    text-entry boxes, the last of which can often be set up to allow file input.
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
    The principal and basics of typecasting were covered in the "inbuilt
    functions" section of lesson 4, but it is worth noting here that
    typecasting is extensively used in parsing situations, where data is passed
    in as a string, and usually required in some numerical or data-type
    specific format.

    Beyond this, in giving users input-based feedback it is possible to modify
    strings with pre-defined entry positions, using what's known as 'string
    formatting'. This technique is available in a variety of ways, and can also
    be used more generally, whenever it's desired to specify a string with a
    set syntax or structure, and add necessary/relevant data later.

    Considerable depth of string formatting syntax and possibilities can be
    found at pyformat.info, but a few basic examples are provided below.
'''



# General String Formatting Example
'''
    Python string formatting is achieved using curly braces ({}) and the
    'format' function. Braces can have any number of parameters in them, but
    the simplest options are to leave them blank, in which case the format
    function must contain the same number of arguments as there are brace
    pairs, or to number them (starting at 0), which allows for specific
    ordering of format parameters, and for using each inputted value multiple
    times.

    Inputs can be explicit strings or other datatypes, or pre-existing
    variables.
'''
dob = 1901
'my name is {}, and I was born in {}.'.format('Name', dob)
    # 'my name is Name, and I was born in 1901.'

'my name is {1}, and I was born in {0}.'.format(dob, 'Name')
    # 'my name is Name, and I was born in 1901.'

'Hi! My name is {0}, and I was born in {1}. {1} was great!'.format('Name', dob)
    # 'Hi! My name is Name, and I was born in 1901. 1901 was great!'




#------------------- SEARCHING AND REGULAR EXPRESSIONS/REGEX ------------------#
'''
    Beyond formatting existing strings, it is also possible to search
    containers in python, using the 'in' keyword or the 'index' or 'replace'
    functions. While these are highly useful functions in their own right, they
    become of particular benefit when applied in conjunction with pattern
    recognition in strings. This is implemented using regular expressions, or
    'regex', which allows searching for particular characters, or sets of
    characters in a particular order, as well as most conceivable patterns that
    could occur.

    This is incredibly beneficial in the parsing of inputted data, from either
    files or direct user input, and can also be useful in stripping out
    unwanted characters or expressions, or determining what type of information
    a particular string contains. Unfortunately the syntax of regular
    expressions is quite content-heavy, so it is left for the reader to search
    for themselves.
'''



# 'in' Keyword
'''
    The 'in' keyword checks if a particular container contains one or more
    instances of the specified object.
'''
if 'password' in list_of_options:
    print('Potential hack discovered!')

while 'error' in my_code:
    my_code.remove('error')


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
    an optionally specified number of occurrences of a specified string within
    the string it is run from.
'''
my_code.replace('error', 'no error') # replace all errors
my_code.replace('first error', 'no error', 1) # replace the first error




#------------------------------ IMPORTS/LIBRARIES -----------------------------#
'''
    There is a common saying in life that there is no need to reinvent the
    wheel. Pythonic programming is strongly focussed on maintaining simplicity
    and readability in code, but it is also equally important to avoid
    needlessly recreating code which has already been written previously. While
    it can be beneficial to learn to write simple code from scratch, in larger
    applications and a performance-based environment, it is often highly
    valuable to use code found online, from forums or libraries, or even from
    code you've previously written yourself. The principal of abstraction also
    applies here, since often code is more readable if it uses predefined
    functions from external modules than to explicitly include every function
    and variable used in a single file.

    As such, Python allows the imports of code from external files, either
    fully or partially, using the 'from', 'import' and 'as' keywords, with
    examples below.
'''



# 'import' Keyword
'''
    'import' can be used exclusively, in importing a whole module, after which
    elements from that module must be accessed using so-called 'dot-notation',
    whereby the module name must be used before each function or variable,
    separated by a dot. Multiple imports can be performed in the same line
    using comma separation.
'''
import numpy, matplotlib.pyplot

matplotlib.pyplot.plot([1,2,3],[2,4,6]) # plots y=2x over domain [1,3]


# 'as' Keyword
'''
    The 'as' keyword can be used to simplify extensive module structure names,
    allowing a file or function to be imported with a user-specified moniker.
'''
import matplotlib.pyplot as plt
import tkinter as tk

my_frame = tk.Frame()
my_plot = plt.plot([1,2,3],[2,4,6])

# Without the 'as' above, this would be
my_frame = tkinter.Frame()
my_plot = matplotlib.pyplot.plot([1,2,3],[2,4,6])


# 'from' Keyword
'''
    'from' is used to specify a module, from which imports of a particular
    function or set thereof can be performed. If individual functions or
    objects are imported, this allows the user to avoid specifying the module
    before using these. The potential detriment of this is the loss of clear
    origin of each function or object, meaning a programmer unfamiliar with the
    initial module from which imported objects originates may struggle to find
    where a particular function or object is defined before realising it was
    imported.
'''
from tkinter import Canvas
from math import sqrt
from matplotlib.pyplot import plot

my_canvas = Canvas()
my_irrational = sqrt(2)
my_plot = plot([1,2,3],[2,4,6])


# ----- NOTE: Import All Notation ----- #
'''
    It is worth noting that python provides a notation to import every element
    within a module or package, namely by using an asterisk (*) instead of
    specifying a specific element to import. This is done as in:

    'from module import *'
'''

# ----- NOTE: External Module Locations ----- #
'''
    When importing from existing files, it often makes sense to do this from
    the same directory as the file you are running (known as the current
    working directory). This means imports can be made directly, and also means
    that any time some code module is provided to someone else, it is simple to
    also provide any imported files by just copying the whole folder it comes
    in. If necessary, it is possible to modify the path from which files are
    imported, instructions for which can be found online.

    As mentioned, it is also possible to import externally implemented
    libraries/packages. These can be both downloaded and installed using
    python's package manager, pip. Note it is not usually necessary to manually
    download and install a package - the correct command sent to pip should
    complete both the download and installation for you.
