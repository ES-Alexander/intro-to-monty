#!/usr/bin/env python3
light_on = (False, 'off')


# Create a function "toggle_light" which toggles the state of the light,
# returning the new state, and printing both the old and the new state as
# 'old state: <old>, new state: <new>'

def toggle_light(light_para):
    ''' Toggles between on and off states of the light, printing the result.

    Returns the new state of the light as a boolean value for "light_on"
    and prints the old state and new state as:
    "old state: <old>, new state: <new>"

    toggle_light(bool) --> bool
    '''

    if light_para[0] == True:
        print('old state: on, new state: off')    
        light_para = (False, 'off')
    else:
        print('old state: off, new state: on')
        light_para = (True, 'on')
    return light_para

toggle_light(light_on)
