#!/usr/bin/env python3
################################################################################
#                                                                              #
#                         Challenge Problem N - Checker                        #
#                                                                              #
################################################################################

#---------------------------------- TASK 1 -----------------------------------#
'''
    Check description
'''

def check_cpN_1():
    '''Check result of task 1. If correct, create an example solution file.

    check_cpN_1(None) -> None/CPN_example_solution.py
    '''
    print('Testing CPN, Task 1.')
    
    all_tests_passed = True

    
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


