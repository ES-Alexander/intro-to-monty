#!/usr/bin/env python3
################################################################################
# This file contains a challenge problem to test some of the content which has #
# been covered so far. You will likely have to revise some of the notes from   #
# previous lessons to find correct syntaxes, but if you have learnt the        #
# content well it shouldn't be too hard to find.                               #                              Challenge Problem                               #
################################################################################

# Description
'''
    One of the first uses of computers was in cryptography, where
    computationally challenging cypher problems required rapid computation to
    decypher codes in a sufficiently short time that the decoded information was
    still relevant. A famous example of this is the German Enigma machine, from
    WWII, which created coded messages with a code which was updated daily with
    new parameters. It was only eventually overcome when Alan Turing invented
    a machine which could crack the code fast enough - the computer.

    This challenge task centres around the cyphering and decyphering process,
    but for a much simpler code than the likes of Enigma. This code is known as
    'Shifted Alphabet Code', or 'Alpha Offset'. It is implemented by every
    letter of a message being incremented in the alphabet by a set number. To
    decode the message simply requires shifting all the letters back by the
    initial amount. If you reach the end of the alphabet while going up, or the
    start while going down, simply continue incrementing from the other end.
    Punctuation, spacing, and other non-numerical characters are left as is.

    Using a 'for' or 'while' loop, shift the letters of the following message
    by every possible amount (e.g. 0 to 25 letters offset), printing each
    new shift, and the amount shifted, to the console. If you implement this
    correctly, one of the shifts should crack the code! Correctly entering the
    offset value and the decoded message will make an example solution to the
    problem available.
'''

# Hints
'''
    The Lesson 3 notes present a way to search through a container data-type, as
    well as how to not index outside the allowed region. Note that a string in
    Python can be considered as just an ordered container of characters, so it
    can be searched/iterated through the same way as any other container type.
    A string can also be added to using string_var += 'more string'.

    Lesson 2 introduced running code depends on some condition. Here you'll need
    to consider lower-case letters, upper-case (capital) letters, and characters
    which aren't letters at all.

    Python also has a number of functions implemented by default on each
    datatype, which can be found using help(<data_type>), as mentioned in L1.
    If a particular feature is required which you aren't aware of, try to use
    the help function to determine if that feature is already implemented for
    the relevant data type.

    It is worth noting that Python convention has functions which begin and end
    with a double underscore (__) as special functions, generally used to
    implement how particular operators behave. These usually shouldn't be
    accessed directly - relevant functions will most likely be found below
    the section of functions named with double underscores.
'''


lower_case_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_case_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

coded_message = "V'z n fhcre frperg pbqr. Pna lbh svaq bhg jung V fnl?"


# <your code here>
for/while ... :
    ...
    print(...)


