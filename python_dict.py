#!/usr/bin/env python3
################################################################################
#
#   Python 3 - Dictionary of terms
#
#   As assembled by ES Alexander (5/11/2016)
#
################################################################################


# GENERAL SPECIFIER SYNTAX IN THIS DOCUMENT

"""
{}  : User defined input
<>  : Link to predefined term
... : etc.
"""


# IMPORTING

"""
import {library/filename} (as {caller})
    Commands from here are later used as <caller>.{command}
    
from {library/filename} import {command/*(everything)}
    Commands imported in this way are used as if defined in current program
"""

# VARIABLES

""" DEFINING:
{variable_name} = [class/data_type]({value}) -- Brackets iff type specified
"""
""" TYPES:
integer   : integer value
                int({value})
float     : float value
                float({value})
string    : string of characters
                '{iterable value(s)}    or    str({iterable value(s)})
                '\n' is new line
                '\t' is tab
boolean   : boolean value (True/False)
                bool({value})
list      : mutable list of values
                [{value1, value2, ...}]    or    list({value1, value2, ...})
tuple     : immutable list of values
                ({value1, value2, ...})    or    tuple({value1, value2, ...})
"""

# COMMON OPERATIONS

"""
addition                   : +
multiplication             : *
subtraction                : -
division (floating point)  : /
division (floor)           : //
modulo                     : %
power                      : ^
"""

# LOGIC

"""
if {boolean condition (and {boolean(s)}) (or {boolean(s)})}:
    {then}
elif <additional condition(s)>:
    {then}
else:
    {then}


'not' is able to be used for reversing boolean values.
'==' checks for equivalency.
'!=' checks for inequivalency.
'<' checks for less than.
'>' checks for greater than.
'<=' checks less than or equal to.
'>=' checks greater than or equal to.
'()' allow for grouping.
"""

# LOOPS

"""
for {value(, additional values)} in {iterable}:
    {repeating code}

while {boolean(s)}:
    {repeating code}

'break' breaks out of loops.

'continue' skips to the end of the current loop iteration.
"""

# FUNCTIONS

"""
def {function_name}({input_arguments}):
    '''{Returning comment}

    {Details of function usage}

    Preconditions: {}

    Raises:
        {Errors raised}
        
    '''
    {function definition}


'return {value}' is used for returning values.

functions can call themselves recursively.
"""

# CLASSES

"""
class {class_name}({parent_class (usually object)}):
    '''{Basic class description}'''
    def __init__(self,{initialisation_arguments}):
        '''{More detailed class desctiption comment}

        Constructor: <class_name>(<initialisation_arguments (type)>)

        '''
        {initialisation}

    {Additional methods}

    @classmethod
    def {class_method}(cls,{input_arguments}):
        '''Comments for class method'''
        {definition}

    @staticmethod
    def {static_method}({input_arguments}):
        '''Comments for static method'''
        {definition}


Additional methods often include:
    '__str__' : readable string representation of class
    '__repr__': formal representation of class
    '__len__' : function of size(class_instance) function
    '__add__' : function of class_instance1 + class_instance2 function
    '__sub__' : subtraction (-)
    '__mul__' : multiplication (*)
    '__mod__' : modulo (%)
    '__pow__' : power (^)
    '__eq__'  : equivalency check behaviour
    '__lt__'  : less than check behaviour
    '__gt__'  : greater than check behaviour
    '__le__'  : less than or equal to check behaviour
    '__ge__'  : greater than or equal to check behaviour

Class- and Static-methods are callable by:
    {class_name}.{method_name}({input_arguments})

Methods in a class can call access methods and values from the parent with:
    super().{parent_method}({input_arguments})
"""

# Graphical User Interfaces (tkinter)

""" SETUP
import tkinter as tk

{tkinter-based code definitions}

root = tk.Tk()
app = {application_class_name}(root) -- root given as application master
root.mainloop() -- runs application until closure before code continues
"""
""" USAGE
item = tk.{Item_name}({master}, {configurations})


ITEMS:
    Button -- pressable button
    Canvas(Widget, XView, YView) -- allows for drawing of shapes and images
    Checkbutton -- check-list button
    Entry(Widget, XView) -- text entry widget
    Frame -- organiser
    Label
    LabelFrame --organiser specifically for labels
    Listbox(Widget, XView, YView) -- list of items
    Menu
    Menubutton
        OptionMenu
    Message
    PanedWindow
    Radiobutton
    Scale
    Scrollbar
    Spinbox(Widget, XView)
    Text(Widget, XView, YView)

    messagebox.{type}({input_arguments})
        types can be found by help(tk.messagebox)
       

ITEM CONFIGURATIONS (BASIC):
    text = <str> -- sets item's text
    bg = <str> -- sets item's background colour
    fg = <str> -- sets item's foreground colour
    command = {command} -- sets item's command
    **More complicated configurations found in help and dir**
    

PACKING ARGUMENTS:
    side=tk.TOP/BOTTOM/LEFT/RIGHT -- side of pack within master
    anchor = tk.N/E/S/W -- directional placement within packing
    fill = tk.X/Y/BOTH -- directional expansion upon window resize
    pady = {int} -- pixels of external padding in y-direction
    padx = {int} -- pixels of external padding in x-direction
    ipady = {int} -- pixels of internal padding in y-direction
    ipadx = {int} -- pixels of internal padding in x-direction
    expand = {bool} -- expansion of item upon window resize

    
ITEM METHODS:
    Widgets:
        config('{configuration_name}',{value})
    Items:
        item_config('{configuration_name}',{value})
    Canvas:
        create_image(x,y,tk.PhotoImage(file_directory))
        create_rectangle(x1,y1,x2,y2)
        bind("<{bind_event}>", command={command})
        etc...
    
