#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following exercises below the appropriate   #
# comment, and click run when complete, using either the menu-bar at the top,  #
# or the F5 key on your keyboard.                                              #
################################################################################


# Default variables
'''
    Write a function 'light_switch' which takes a variable 'is_on', set to a
    list containing 'True' by default (ie [True]). Calling light_switch should
    toggle the switch, so if is_on contains True it should be swapped out for
    False, with 'turned off the light' printed to the console. If is_on contains
    False, it should be swapped for True, and 'turned on the light' should be
    printed. If a boolean is passed in as is_on (can check with the 'isinstance'
    function) the light cannot be toggled, so do not attempt to replace the
    contents, and instead print 'light is stuck on' if is_on is True and
    'light is stuck off' if is_on is False. No value should be returned.

    e.g.
        light_switch() # -> turned off the light
        a = [False]
        light_switch(a) # -> turned on the light
        print(a) # -> [True]
        b = False
        light_switch(b) # -> light is stuck off
        print(b) # -> False
'''

# <light_switch>



# * Dereferencing (Unknown Number of Parameters)
'''
    Implement the function 'flatten' below, which takes in an unknown number of
    lists and returns a single list of all the inputted lists joined together.
    You may find it helpful to use a builtin function to help achieve this, but
    you are not required to do so.

    Write a second method 'flatten2' beneath, which uses a different
    implementation to achieve the same result as 'flatten'.

    e.g.
    flatten([1,2,3,4],[5,6,7],[9,10,11]) -> [1,2,3,4,5,6,7,8,9,10,11]
'''

def flatten(*lists):
    ''' docstring '''
    pass # your implementation goes here

# <flatten2>



# Lambdas and List Comprehension
'''
    Write a lambda function 'a_only' which takes two lists (a,b) and returns a
    list of all elements that are in 'a' but not in 'b' (effectively a copy of
    'a' without any element values shared by 'b').
    
    Write a lambda function 'overlap' which takes in two lists (a,b) and returns
    a list of all elements that are in both 'a' AND 'b'.

    Write a lambda function 'breakdown' which takes in two lists (a,b), and
    returns a tuple with its first element as a list of elements only in 'a',
    its second element as a list of elements in both 'a' and 'b', and its third
    element as a list of elements only in b. You may use your 'overlap' and
    'a_only' functions to help implement this.

    e.g.
    a = [1,2,3,4,1]
    b = [4,2,5,9]
    a_only(a,b)    # returns [1,3,1]
    overlap(a,b)   # returns [2,4]
    breakdown(a,b) # returns ([1,3,1],[2,4],[5,9])
'''
# your code here





'''
    When you're done, click Run or F5 to check that you've followed the
    instructions. Example solutions can be found at the bottom of the exercise
    checker file.

    The code below isn't for editing, it's used to run the test file when this
    program is run.
'''

if __name__ == '__main__':
    from L4_2_exercise_checker import L4Tests
    L4Tests = L4Tests()
    # run the tests (with feedback)
    L4Tests.run_tests(verbose=True)
