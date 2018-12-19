#!/usr/bin/env python3
################################################################################
#                                                                              #
#                         Challenge Problem 2 - Checker                        #
#                                                                              #
################################################################################

#---------------------------------- TASK 1 -----------------------------------#
'''
    Check decoded message and determined offset are correct
'''

def check_cp2_1():
    '''Check result of task 1. If correct, create an example solution file.

    check_cp2_1(None) -> None/CP2_example_solution.py
    '''
    print('Testing CP2, Task 1.')
    
    all_tests_passed = True

    # Check message comparison
    expected_message = '100100100100111011011010010000001100001001000000' + \
                       '111001101110101011100000110010101110010001000000' + \
                       '111001101100101011000110111001001100101011101000' + \
                       '010000001100011011011110110010001100101001011100' + \
                       '010000001000011011000010110111000100000011110010' + \
                       '110111101110101001000000110011001101001011011100' + \
                       '110010000100000011011110111010101110100001000000' + \
                       '111011101101000011000010111010000100000010010010' + \
                       '010000001110011011000010111100100111111'
    decoded_message = input('Enter the decoded message: \n')
    if decoded_message != bin_decode(expected_message):
        all_tests_passed = False
        print('Decoded message is incorrect.')
    else:
        print('Decoded message is correct.')
    print()

    # Check offset value
    expected_offset = '1101'
    offset = input('Enter the determined offset: \n')
    if int(offset) != int('0b' + expected_offset, 2):
        all_tests_passed = False
        print('Offset value is incorrect.')
    else:
        print('Offset value is correct.')
    print()

    # Generate file if correctly specified
    if all_tests_passed:
        gen_cp2_1_output()
        print("You've cracked the code - well done!")
        print("An example solution is now available.")
    

def bin_decode(string):
    '''Return the string result of a string of binary bits converted to ASCII.

    bin_decode(str(0/1)) -> str
    '''
    n = int('0b' + string, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def gen_cp2_1_output():
    from coded.__pydec__.decoder import decoder
    decoder('coded/coded2_1.txt','CP2_1_example_solution.py')


#----------------------------------- TASK 2 -----------------------------------#
'''
    Test explanations.
'''

def check_cp2_2():
    pass

#<tests>


