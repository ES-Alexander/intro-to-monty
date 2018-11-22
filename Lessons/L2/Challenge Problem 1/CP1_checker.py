################################################################################
#                                                                              #
#                         Challenge Problem 1 - Checker                        #
#                                                                              #
################################################################################

# Import relevant aspects from CP1_file.py
from CP1_file import *
from helpers import is_defined

# Set global variables for progress display
num_tests = 6
detailed_progress = False
failed = 0
passed = 0


def cp1_tests():
    '''Runs the specified tests for each task.

    cpn_tests(None) -> None
    '''
    test_count = 0
    # TASK 1
    t1_test()
    # TASK N
    #tests()


#---------------------------------- TASK 1 -----------------------------------#
'''
    General task test explanations.
'''

def t1_test():
    '''Tests the assigned property checks of rand_1, rand_2, and rand_3.

    Checks based off the variables:
        - largest
        - smallest
        - even
        - divisible_by_3
        - positive
        - absolute_sum_of_values

    t1_test(None) -> None
    '''

    print("TASK 1: [" + str(rand_1) + ", " + str(rand_2) + ", " +
          str(rand_3) + "].")
    
    # Largest test
    if test('largest'):
        if largest == max(rand_1, rand_2, rand_3):
            print("PASSED: 'largest' has the expected value,",
                  max(rand_1, rand_2, rand_3), ".")
        else:
            print("FAILED: '" + str(largest) + "' is not the expected value,",
                  max(rand_1, rand_2, rand_3))


    # Smallest test
    if test('smallest'):
        pass

    # Even test
    if test('even'):
        pass
        

    # Divisible by 3 test
    if test('divisible_by_3'):
        pass



    # Positive test
    if test('positive'):
        pass

        


    # Absolute sum of values
    if test('absolute_sum_of_values'):
        pass
        
        
    
        



#----------------------------------- TASK 2 -----------------------------------#
'''
    Test explanations.
'''

#<tests>


#------------------ BASE TEST ----------------------#

def test(var_name):
    ''' Returns definition state, prints initialisation.

    test(str) -> bool
    '''
    print('Testing \'' + var_name + '\'')
    print_test_progress()

    if not is_defined(var_name):
        print("FAILED: '" + var_name + "' is not defined.")
        return False
    print("Pass: '" + var_name + "' is defined.")
    return True

    
    

#---------------------------------- RUN CODE ----------------------------------#

def print_test_progress():
    '''Prints the progress of the full set of tests.

    print_test_progress(None) -> None
    '''
    # Print running tally of tests completed
    print('\nRunning test ' + str(test_count) + ' of ' + str(num_tests) + '.')
    print('' + str(100 * (test_count - 1) / num_tests) + '% completed.')
    if detailed_progress:
        print('\nPresently:')
        print(str(passed) + ' of ' + str(test_count - 1) + ' passed,')
        print(str(failed) + ' of ' + str(test_count - 1) + ' failed,')
        print('(' + str(100 * passed/(test_count - 1)) + '% success rate)')
    test_count += 1


# When running this file, run the relevant tests
if __name__ == '__main__':
    cp1_tests()
