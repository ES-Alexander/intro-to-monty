################################################################################
# This file contains a function used to test the L1_examples file, checking    #
# that the correct variables are defined, and as the correct types and values. #
################################################################################

# imports all the variables from L1_examples
from L1_2_examples import *

def run_tests():
    """ Prints the results of checking the variables from L1_examples.py

    tests(None) -> None
    """
    print()
    integer_test()
    float_test()
    list_test()
    tuple_test()
    dict_test()


#----------------------------------- Tests ------------------------------------#

def integer_test():
    ''' Testing my_int. '''
    
    print('Integer Test: my_int')
    invalid_int = 'Please define an integer called "my_int".'
    # Check if my_int exists
    if is_defined('my_int'):
        # Check if my_int is not an integer, else test has succeeded.
        if not isinstance(my_int, int):
            print('FAILURE: my_int is defined as ' + type(my_int).__name__ +
              ' type, not an Integer. ')
            print(invalid_int)
        else:
            print('SUCCESS: my_int is defined, with an integer value.')
    else:
        print(invalid_int)
    print()


def float_test():
    ''' Testing my_float. '''
    
    print('Float Test: my_float')
    invalid_float = 'Please define a float called "my_float".'
    # Check if my_float exists, else throw not defined error.
    if is_defined('my_float'):
        # Check if my_float is not a float, else test has succeeded.
        if not isinstance(my_float, float):
            print('FAILURE: my_float is defined as ' + type(my_float).__name__ +
              ' type, not a Float. ')
            print(invalid_float)
        else:
            print('SUCCESS: my_float is defined, with a float value.')
    else:
        print(invalid_float)
    print()


def list_test():
    ''' Testing my_list. '''
    
    print('List Test: my_list')
    invalid_list = 'Please define a list called "my_list".'
    # Check if my_list exists
    if is_defined('my_list'):
        # Check if my_list is not a list, else test has succeeded.
        if not isinstance(my_list, list):
            print('FAILURE: my_list is defined as ' + type(my_list).__name__ +
              ' type, not a List. ')
            print(invalid_list)
        else:
            # Check if my_int and my_float are defined
            try:
                expected_items = [my_int, my_float]
                expected_length = 3
                # check if my_list is the right length and contains
                # my_int and my_float
                passed = check_items_in_group(expected_items, expected_length,
                                              my_list, 'my_list')

                # check if my_list contains a boolean
                if any(isinstance(item, bool) for item in my_list):
                    print('Pass: my_list contains a boolean.')
                else:
                    passed = False
                    print('Fail: my_list does not contain a boolean value.')
                    
                # print success state to console
                if passed:
                    print('SUCCESS: my_list is defined, as a list, ' +
                          'and includes the expected values.')
                else: print('FAILURE: Please check your implementation of ' +
                            'my_list.')
            except NameError:
                print('FAILURE: my_int or my_float is not defined.')
                
    else:
        print(invalid_list)
    print()


def tuple_test():
    ''' Testing my_tuple. '''

    print('Tuple Test: my_tuple')
    invalid_tuple = 'Please define a tuple called "my_tuple".'
    # check if my_tuple exists, else throw not defined error.
    if is_defined('my_tuple'):
        # check if my_tuple is not a tuple
        if not isinstance(my_tuple, tuple):
            print('FAILURE: my_tuple is defined as ' + type(my_tuple).__name__ +
              ' type, not a Tuple.')
            print(invalid_tuple)
        else:
            expected_length = 2
            passed = check_number_of_items(expected_length, my_tuple,
                                           'my_tuple')
            # wrapper for non-existence of my_list
            try:
                expected_items = [my_list]
                passed = passed and check_group_inclusion(
                    expected_items, my_tuple, 'my_tuple')
            except NameError:
                passed = False
                print('Fail: my_list is not defined, or included.')
            
            # print success condition
            if passed:
                print('SUCCESS: my_tuple is defined, with the expected value.')
            else:
                print('FAILURE: Please review your implementation of my_tuple.')
    else:
        print(invalid_tuple)
    print()


def dict_test():
    ''' Testing my_dict. '''

    print('Dict Test: my_dict')
    invalid_dict = 'Please define a dictionary called "my_dict".'
    # check if my_dict exists, else throw not defined error.
    if is_defined('my_dict'):
        # check if my_dict is a dict, else test has failed.
        if isinstance(my_dict, dict):
            passed = True
            keys = my_dict.keys()
            # check if my_dict contains the expected number of keys.
            expected_length = 4
            passed = check_number_of_items(expected_length, keys,
                                           'my_dict keys')
            # check if expected values exist.
            try:
                expected_dict = {
                    'integer': my_int,
                    'float': my_float,
                    'list': my_list,
                    'tuple': my_tuple
                    }
                passed = passed and check_dict_inclusion(expected_dict,
                                                        my_dict, 'my_dict')
            except NameError:
                passed = False
                print('Fail: one or more of my_int, my_float, my_list, '
                      'or my_tuple do not exist.')

            # print success condition
            if passed:
                print('SUCCESS: my_dict is defined, with the expected ' +
                      'key-value pairs.')
            else:
                print('FAILURE: please review your implementation of my_dict')
        else:
            print('FAILURE: my_dict is defined as ' + type(my_dict).__name__ +
              ' type, not a Dictionary. ')
            print(invalid_dict)
    else:
        print(invalid_dict)
    print()


#------------------------------ Helper Functions ------------------------------#

def is_defined(var_name):
    ''' Returns whether or not the specified variable is defined. '''
    try:
        eval(var_name)
        print('Pass:', var_name, 'is defined.')
        return True
    except NameError:
        print('FAILURE:', var_name, 'is not defined.')
        return False

def are_defined(var_list):
    ''' Returns whether or not all specified variables are defined. '''
    defined = True
    for var in var_list:
        defined = defined and is_defined(var)
        if not defined:
            break
    return defined

def check_items_in_group(expected_items, expected_length, group, group_name):
    '''Returns if the expected items and number of items are in the group.

    Prints status updates to console.

    check_items_in_group(List, int, List/Tuple, String) -> bool
    '''
    passed = check_number_of_items(expected_length, group, group_name)
    passed = passed and check_group_inclusion(expected_items, group, group_name)

    return passed

    
def check_number_of_items(expected_length, group, group_name):
    '''Returns if no. expected items == no. items in group.

    Prints status to console.

    check_number_of_items(int, List/Tuple, String) -> bool
    '''
    passed = True
    if expected_length != len(group):
        passed = False
        if len(group) < expected_length:
            print('Fail: ' + group_name +
                  ' contains fewer items than expected.')
        else:
            print('Fail: ' + group_name +
                  ' contains more items than expected.')
    else:
        print('Pass: ' + group_name + ' contains the expected number of items.')
    return passed


def check_group_inclusion(expected_items, group, group_name):
    ''' Returns if group includes all expected items.

    Prints status updates to console.

    check_group_inclusion(List, List/Tuple, String) -> bool
    '''
    passed = True
    for item in expected_items:
        if (item not in group) or (item in group and item is not
                                   group[group.index(item)]):
            passed = False
            print('Fail: ' + group_name + ' does not contain', item)
        else:
            print('Pass: ' + group_name + ' contains', item)

    return passed


def check_dict_inclusion(expected_dict, dictionary, dict_name):
    ''' Returns if the dict includes all expected keys and values.

    Prints status updates to console.

    check_dict_inclusion(List, Dict, String) -> bool
    '''
    passed = True
    keys = dictionary.keys()
    for key in expected_dict.keys():
        if key not in keys:
            passed = False
            print('Fail: no "' + key + '" key present in ' + dict_name + '.')
        elif dictionary[key] is not expected_dict[key]:
            passed = False
            print('Fail: value of "' + key + '" key is not ' + dict_name + '.')
        else:
            print('Pass: "' + key + '" key exists with correct value.')

    return passed
    

#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    # Integer Test

    # Solution
    my_int = 5 # Note that any integer value could have been selected


    # Float Test

    # Solution
    my_float = 2.0 # Note that any float value could have been selected


    # List Test
    
    # Solution
    my_list = [my_int, my_float, True]


    # Tuple Test

    # Solution
    my_tuple = (my_list, 'extra')


    # Dictionary Test

    # Solution
    my_dict = {
        'integer': my_int,
        'float': my_float,
        'list': my_list,
        'tuple': my_tuple
    }


    # Run tests
    
    run_tests()
