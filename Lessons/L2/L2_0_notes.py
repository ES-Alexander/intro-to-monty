################################################################################
#                                                                              #
#                                   Lesson 2                                   #
#                Conditionals, Variable Domains, and Operators                 #
#                                                                              #
################################################################################




#-------------------------------- CONDITIONALS --------------------------------#
'''
    With basic data types established, almost every computer program requires
    the use of conditional statements. These involve the use of boolean (True/
    False) values, and allow for consideration of different parameters, and
    code which can distinguish between different situations, and respond
    accordingly.

    In Python, conditional statements are made using the keywords 'if', and
    'else', with multiple conditionals in the same block using the word 'elif',
    short for "else if". The usage of these is described in the examples below.
'''



# This is a basic 'if' block, no additional blocks are required
if <condition>:
    <relevant code>

# A more complicated 'if' block can include 'elif's and 'else' statements.
if <condition 1>:
    <relevant code 1>
elif <condition 2>:
    <relevant code 2>
...
elif <condition n>:
    <relevant code n>
else:
    <relevant code for if no conditions were true>

# An if-else block in a single line
<relevant code 1> if <condition> else <relevant code 2>



# ----- NOTE: Indentation ----- #
'''
    It is important to note that Python is a language based off indentations.
    Once a block has been entered, it is indented, and any return to the
    previous indentation level will end that block.
'''

# ----- NOTE: Evaluation ----- #
'''
    Each 'if' block will have at most ONE section evaluated. Conditions are
    checked successively from the initial 'if' condition, and if one condition
    holds true, all subsequent sections of the same block will be ignored. If
    no conditions hold true, and there is no 'else' statement, the entire 'if'
    block will be ignored.

    To write code which considers multiple conditions separately, use separate
    'if' blocks.
'''




#------------------------------ VARIABLE DOMAINS ------------------------------#
'''
    Separated code blocks introduce a new and important situation related to
    how and where variables are defined. A variable defined within an 'if'
    statement does not exist outside that statement, so when blocks are in play
    it is essential to consider where a variable is defined if its usage is
    required outside of a particular block, or is intended to be restricted to
    within only one block, or part thereof.

    This applies to conditional blocks, as presented in this lesson, but also
    applies more broadly to loops, functions, and classes discussed in future
    lessons.

    The examples below provide a brief display of a variable which is
    conditionally defined, and one which is defined as able to be used from both
    outside and within a given block
'''

# A variable which is conditionally defined
<some initial code>
if <some condition>:
    my_new_var = True
    <do things with my_new_var>
<other code which CANNOT depend on my_new_var>

# A variable which is defined outside a block in which it is used
<some initial code>
my_new_var = True
if <some condition>:
    <code which may depend on and/or change my_new_var>

if my_new_var:
    <code dependent on the current value of my_new_var>



# ----- NOTE: Continuity ----- #
'''
    In order for a variable to be used outside of a specified block, it must
    be defined outside of it. If this is the case, the variable can be used
    within any blocks where it exists, and can also be altered within these
    blocks, with the effects passing through to outside the block.

    A variable defined fully outside of any blocks or functions is generally
    considered as 'global', and can also be specified as such using the 'global'
    keyword. This can technically be applied at any level of block in the code,
    properly global variables as a whole are generally regarded as non-ideal
    solutions to problems due to difficulties in debugging and potentially with
    naming clashes for locally defined variables. This becomes more important
    with the introduction of multiple functions and classes defined in the same
    program file, as discussed later in the course.
    
    Variables defined within some section, and not specified as global, are
    considered to be 'local', or locally defined. Many programming errors come
    from the assumption that certain variables are or are not defined within a
    certain local domain, and this will be discussed further with the
    introduction of functions.
'''




#---------------------------------- OPERATORS ---------------------------------#
'''
    All programming languages implement a number of operators by default, to
    use both in the evaluation of conditionals, as well as to modify existing
    variables. The standard programming operators in python are as follows:
'''

# Basic Mathematical (Arithmetic) Operators:

    # Addition (+)
        a + b
    # Subtraction (-)
        a - b
    # Multiplication (*)
        a * b
    # Division (/)
        a / b
    # Integer Division [divides integers to the nearest truncated integer] (//)
        a // b
    # Modulo/Mod [provides the remainder of the number (a) divided by the base
    # (b). This is the complement of integer division.] (%)
        a % b
    # Power (**)
        a ** b

    # NOTE: The modulo operator is commonly used to keep a count within a
    #   specified range, or to check if an integer is evenly divisible by
    #   another, in which case a % b is 0.

    # Additional mathematical operators and functions can be accessed by
    # importing the math library which will be discussed in a later lesson.


# Bitwise Operators (applied to numerical values in binary)

    # Bitwise AND (&)
    #   Returns the decimal value of the matching bits in a and b.
        a & b
    # Bitwise OR (|)
    #   Returns the decimal value of all 'on' bits in a and b.
        a | b
    # Bitwise XOR (^)
    #   Returns the decimal value of all non-matching bits in a and b.
        a ^ b
    # Bitwise NOT (~)
    #   Returns the decimal value of all the bits in a, flipped.
        ~ a
    # Bitwise left shift (<<)
    #   Returns the decimal value of all the bits in a, shifted b bits left
        a << b
    # Bitwise right shift (>>)
    #   Returns the decimal value of all the bits in a, shifted b bits right
        a >> b


# Modificaition (Assignment) Operators

    # Basic (=)
        a = b
    # Shorthand of a = a Operator b [defined for most of the above operators]
    a Operator= b
        (e.g. a += b)


# Comparison Operators [return boolean values]

    # Greater than (>)
        a > b
    # Less than (<)
        a < b
    # Greater than or equal to (>=)
        a >= b
    # Less than or equal to (<=)
        a <= b
    # Equals (==)
        a == b
    # Not equals (!=)
        a != b


# Logical Operators [return boolean values]

    # Logical AND (and)
        a and b
    # Logical OR (or)
        a or b
    # Logical not (not)
        not a


# Identity Operator

    # Checks if a is located in the same place in memory as b (is)
        a is b
    # Invertible using 'not' keyword
        a is not b

    # NOTE: two equal values are not necessarily in the same memory space, in
    #   which case they are separate objects with equal values.


# Membership Operator

    # Checks if a contains an instance equal to b (in)
        a in b
    # Invertible using 'not' keyword
        a not in b

    # NOTE: the membership operator can be used on dictionaries, but only to
    #   check if a specified KEY is part of the dictionary (not value)
    

    
