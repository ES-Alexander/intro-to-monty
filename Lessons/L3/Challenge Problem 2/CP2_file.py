################################################################################
#                                                                              #
#                              Challenge Problem 2                             #
#                                                                              #
################################################################################

#----------------------------------- TASK 1 -----------------------------------#
'''
    One of the first uses of computers was in cryptography, where
    computationally challenging cypher problems required rapid computation to
    decypher codes in a sufficiently short time that the decoded information was
    still relevant. A famous example of this is the German Enigma machine, from
    WWII, which was altered daily with new parameters, and was only eventually
    overcome with the advent of Alan Turing's invention, the computer.

    This first challenge task centres around the cyphering and decyphering
    process, but for a much simpler code than the likes of Enigma. This code
    is known as 'Shifted Alphabet Code', or 'Alpha Offset'. It is implemented
    by every letter of a message being incremented in the alphabet by a set
    number. To decode the message simply requires shifting all the letters
    back by the initial amount. If you reach the end of the alphabet while going
    up, or the start while going down, simply start continue incrementing from
    the other end. Punctuation, spacing, and other non-numerical characters are
    left as is.

    Using a 'for' or 'while' loop, shift the letters of the following message
    by every possible amount (e.g. 0 to 25 letters offset), printing each
    new shift, and the amount shifted, to the console. If you implement this
    correctly, one of the shifts should crack the code! Correctly entering the
    offset value and the decoded message will make an example solution to the
    problem available.
'''

# ----- HINT: Operators ----- #
'''
    As discussed in lesson 3, the mod (%) operator is highly beneficial for
    any operation requiring numbers to increment continuously between a given
    set of values without going out of the range of the search list.
'''

# ----- HINT: Conditions ----- #
'''
    Separating or sorting characters based on their type in order to deal with
    them in the appropriate manner is an example of where an 'if' block of some
    sort is necessary. In this case you'll need to consider lower case letters,
    upper case letters, and characters which aren't letters at all.
'''

# ----- HINT: Strings ----- #
'''
    Strings in python are a special form of list, composed entirely of
    characters. This means individual characters in a string can be referenced
    using indices as if they were in a list (e.g. first character = my_str[0]).

    Additionally, strings can be added to using the += operator, with a string
    added (e.g. my_str += 'addition').
'''

# ----- HINT: Additional Functions -----#
'''
    Python has a number of functions implemented by default on each datatype,
    which can be found using help(<data_type>), as mentioned in L1. If a
    particular feature is required which you aren't aware of, try to use the
    help function to determine if that feature is already implemented for the
    relevant data type.

    It is worth noting that Python convention has functions which begin and end
    with a double underscore (__) as private functions, which shouldn't directly
    be accessed by users. Relevant functions will most likely be found below
    the section of functions named with double underscores.
'''


lower_case_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                       'o','p','q','r','s','t','u','v','w','x','y','z']
upper_case_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                       'O','P','Q','R','S','T','U','V','W','X','Y','Z']

coded_message = "V'z n fhcre frperg pbqr. Pna lbh svaq bhg jung V fnl?"


# <your code here>
for/while ... :
    ...
    print(...)




#----------------------------------- TASK 2 -----------------------------------#
'''
    Explanation
'''

#<relevant code/space>




#=========================== CHALLENGE TESTER CODE ============================#

if __name__ == '__main__':
    from CP2_checker import check_cp2_1, check_cp2_2
    check_cp2_1()
    check_cp2_2()

