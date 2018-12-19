#!/usr/bin/env python3
################################################################################
#                                                                              #
#                              Challenge Problem 1                             #
#                                                                              #
# Challenge problems are intended to test the limits of the content covered to #
# a certain point. If you understand the content well, they should be doable   #
# with some thought, but if you find yourself struggling considerably it may   #
# be worth revising the relevant aspects of course content.                    #
#                                                                              #
# When all tests have been passed for any particular challenge problem, an     #
# example solution will become available to the course                         #
# participant.                                                                 #
#                                                                              #
################################################################################

# import statement for random integer generation
from random import randint


#----------------------------------- TASK 1 -----------------------------------#
'''
    One essential aspect of programming is the conditional evaluation of code,
    depending on often unknown variable values. It is important to consider all
    possible sets of values a variable could be prior to attempting to write
    conditional code based on it.

    This task is centred around evaluating specific pieces of code based off
    the randomly generated integer values rand_1, rand_2, and rand_3.
'''

rand_1 = randint(-100,100)
rand_2 = randint(-50,150)
rand_3 = randint(-200,0)

'''
    The following variables should be defined, with values dependent on the
    values of the random variables above.

        - largest (largest of the values)
        - smallest (smallest of the values)
        - even (list of even values)
        - divisible_by_3 (list of values divisible by three)
        - positive (list of values equal to or greater than zero)
        - absolute_sum_of_values (absolute value of the sum of the values)

    While it is potentially possible to complete this task more efficiently
    using loops and certain inbuilt functions, the intention for this specific
    exercise is to use if statements and blocks.
'''

# <your code here>




#----------------------------------- TASK 2 -----------------------------------#
'''
    Explanation
'''

#<relevant code/space>




#========================== CHALLENGE TESTER IMPORT ===========================#

if __name__ == '__main__':
    from CP1_checker import *
    cp1_tests()

