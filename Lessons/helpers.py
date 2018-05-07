# Helper functions for checking files

def is_defined(var_name):
    ''' Returns whether or not the specified variable is defined. '''
    try:
        eval(var_name)
        return True
    except NameError:
        return False

def are_defined(var_list):
    ''' Returns whether or not all specified variables are defined. '''
    defined = True
    for var in var_list:
        defined = defined and is_defined(var)
        if not defined:
            break
    return defined
