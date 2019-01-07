#!/usr/bin/env python3
################################################################################
#                                                                              #
#                                   Lesson 2                                   #
#                          Operators and Conditionals                          #
#                                                                              #
################################################################################




#---------------------------------- OPERATORS ---------------------------------#
'''
    Operators are special functions which act on two objects together. Lesson 1
    introduced the idea of variable values being objects, with their methods
    and properties determined by their type. Some of these methods determine
    how each data type interacts when an operator acts on it and another
    object. All programming languages implement several operators by default,
    to allow for common mathematical operations, creating and modifying
    variables, and for value comparisons. The standard operators in python are
    as follows:
'''



# Basic Mathematical (Arithmetic) Operators

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


# ----- NOTE: Modulo (%) ----- #
'''
    The modulo operator is commonly used to keep a count within a specified
    range, or to check if a number is evenly divisible by another (in which
    case a % b = 0).
'''

# ----- NOTE: More Maths? ----- #
'''
    Additional mathematical operators and functions can be accessed from the
    'math' library, which will be discussed in a later lesson.
'''



# Bitwise Operators (applied to numerical values in binary)

    # Bitwise AND (&)
    # Returns the decimal value of the matching bits in a and b.
        a & b
    # Bitwise OR (|)
    # Returns the decimal value of all 'on' bits in a and b.
        a | b
    # Bitwise XOR (^)
    # Returns the decimal value of all non-matching bits in a and b.
        a ^ b
    # Bitwise NOT (~)
    # Returns the decimal value of all the bits in a, flipped.
        ~ a
    # Bitwise left shift (<<)
    # Returns the decimal value of all the bits in a, shifted b bits left
        a << b
    # Bitwise right shift (>>)
    # Returns the decimal value of all the bits in a, shifted b bits right
        a >> b


# Modification (Assignment) Operators

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
    # Logical Inversion (not)
        not a


# Identity Operator [returns boolean value]

    # Checks if 'a' is located in the same place in memory as 'b' (is)
        a is b
    # Invertible using logical inversion (is not)
        a is not b


# ----- NOTE: Equality ----- #
'''
    Two equal/equivalent values/objects are not necessarily stored in the same
    place in memory, in which case 'a == b' is True, but 'a is b' is False.
'''



# Membership Operator [returns boolean value]

    # Checks if 'x == a' is True for at least one element 'x' in container
    # variable 'b' (in)
        a in b
    # Invertible using logical inversion (not in)
        a not in b


# ----- NOTE: Dictionary Membership ----- #
'''
    The membership operator can be used on dictionaries, but if used directly
    checks only if a specified key is in the dictionary, not a value. To check
    values, use 'a in my_dict.values()'.
'''




#-------------------------------- CONDITIONALS --------------------------------#
'''
    With basic data types and operators established, almost every computer
    program requires the use of conditional statements. These involve the use
    of boolean (True/False) values, and allow for consideration of different
    parameters, and code which can distinguish between different situations,
    and respond accordingly.

    In Python, conditionally-executed code is made using the keywords 'if', and
    'else', with multiple separate conditional checks in the same block using
    the keyword 'elif', short for "else if". The usage of these is described in
    the examples below. Each section of code labelled '<condition>' denotes
    some conditional statement, such as a boolean value, or a statement using
    logical or comparison operators (as in the previous section).
'''



# Conditional Block Syntax
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
    Python is a language with enforced indentation. An indentation denotes that
    a new block of code has been entered. Returning to a previous indentation
    level ends all blocks that are further indented than the level returned to.
'''



# Indentation
if <condition>:
    if <condition2>:
        <code>
    elif <condition3>:
        <code2>
# both if blocks ended
<code3>


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
'''
