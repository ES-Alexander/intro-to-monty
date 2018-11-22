# Random Coder Generator
from coder import coder
from random import randint

def rand_coder(file, code_name, incr_range, swap_list_length_range, swap_range):
    """ Creates a coded file code_name, based on the text contained in file.

    Used to code an inputted file with a randomly generated coder, using
        generated values for character swapping and alpha incrementation.

    rand_coder(file.txt/file.py, str.txt/str.py tuple(int, int), int,
        tuple(int, int)) -> None
    """
    # Generate the swap list
    extra_list = gen_swap_list(swap_list_length_range, swap_range)
    # Generate the incrementation value
    incr = gen_incr(incr_range)
    # Run the coder
    coder(file, code_name, incr, extra_list)

def gen_incr(incr_range):
    """ Generates an increment value based off the specified range.

    Attempts to avoid zero increment case using hardcoded swap list length
        values.

    gen_incr(tuple(int, int)) -> int
    """
    min_incr = incr_range[0]
    max_incr = incr_range[1]
    incr = randint(min_incr, max_incr)
    # Avoid zero increment case
    while (incr % 26 == 0) or (incr % 29 == 0):
        incr = randint(min_incr, max_incr)
    print(incr)
    return incr

def gen_swap_list(length_range, swap_range):
    """ Generates a swap list based off specified lengths and range.

    gen_swap_list(int, int, tuple(int, int)) -> List[tuple(int, int)]
    """
    # Initialise empty list
    swap_list = []
    # Extract relevant parameter values
    min_length = length_range[0]
    max_length = length_range[1]
    swap_min = swap_range[0]
    swap_max = swap_range[1]
    # Generate list within parameters
    for x in range(randint(min_length, max_length)):
        swap_list += [(randint(swap_min, swap_max),
                       randint(swap_min, swap_max))]
    print(swap_list)
    return swap_list
