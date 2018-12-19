#!/usr/bin/env python3
################################################################################
#                                                                              #
#                                   Lesson 9                                   #
#              GUIs, Model-View-Controller, Tkinter, Eval and Exec             #
#                                                                              #
################################################################################




#---------------------- GRAPHICAL USER INTERFACES (GUIS) ----------------------#
'''
    So far in the course, all the content and examples have been via a
    command-line interface. You've learnt about and written functions and
    classes, and yet most software that 'normal' people interact with doesn't
    have visible code - so where's the link?

    Graphical User Interfaces, or GUIs, are the programming elements which let
    you write code which creates a visual display, with interactive elements.
    This lesson is a brief introduction to what's known as 'event-driven'
    programming - whereby the user's actions determine which code is run. While
    programming to some degree can certainly be for users of all levels, many
    people would rather interact with visual elements, such as text boxes and
    buttons, than remember function names and calling syntaxes. Writing simple,
    intuitive GUIs to present your content and algorithms can make your
    programs much more accessible, particularly to the general public.
'''




#------------------------- MODEL-VIEW-CONTROLLER (MVC) ------------------------#
'''
    Before introducing you to some common elements of GUIs, it's important to
    understand the purpose of a GUI, and how that can be achieved in code.
    Fundamentally, a GUI is meant to display information to a user. This can be
    extended to be interactive, to display information to multiple users
    simultaneously, to communicate between users, and potentially to create the
    information to display in the first place.

    The Model-View-Controller paradigm is one possible abstraction which
    enables the implementation of a GUI to be separated into three main
    elements. The model is where the data is stored, and includes the format
    (think variable types) of the data, as well as how external code can access
    the data. This can be thought of as a database, and should be able to exist
    without knowing anything about the rest of the GUI. The view is the
    display, it specifies where and how information is to be presented, and
    requires at least some knowledge of the type(s) of data which need display,
    as well as how much data might be needed at any point in time. The
    controller is the communications middle-man, and facilitates the
    connection(s) of the view to the model, while also dealing with user input
    and changing the view as appropriate as a result.

    Note that once connection has been set up by the controller, changes to
    data in the model are allowed to be automatically implemented in the view -
    that is, the view can be effectively given direct read access to the model
    data. In saying that, the view should not be able to modify any data in the
    model without going via the controller, and the model should not try to
    specify a display format for any data - it should just provide access to
    the data requested, if it deems the request allowed. When data is
    determined using an algorithm, the controller can pass parameters to the
    model, but the algorithm itself should be implemented in the model.
'''




#----------------------------------- TKINTER ----------------------------------#
'''
    Tkinter is python's standard GUI library. It contains various predefined
    GUI elements, called widgets, allowing you to reasonably quickly and easily
    get a GUI up and running, with your desired components. The depth and
    breadth of the Tkinter library, along with the majority of other GUI
    libraries, mean that GUI programming generally consists of searching online
    for how to implement desired functionality. This is particularly the case
    until you've used many of the elements extensively, and even then will
    often involve searching for the usage syntax or element properties in the
    Tkinter documentation (tkdocs.com), or for examples in in-depth GUI
    tutorials.
'''



# Common Widgets
'''
    The following are a brief summation of commonly used Tkinter widgets, along
    with their general purpose(s) in a GUI.

        Frame: a container for holding other widgets, can be used for layouts
        and spacing

        Label: a widget for displaying some basic text or an image to the user,
        and generally not interacted with by the user.

        Button: a means for user interaction with a program, will run a script
        when pressed. (Also available: CheckButton and RadioButton)

        Entry: allows a user to provide a single-line string, often identified
        by a Label (e.g. Password, Name, etc). (The Text widget allows for
        multi-line string entries)

        Combobox: specifies a predefined set of selectable options, and
        optionally allows user to specify additional choices.

        Menubar: the bar of menus at the top of your window/screen, lets the
        user select relevant menu items, which run a script when pressed (e.g.
        File->New, Edit->Cut, etc).

        Scrollbar: allows more widgets/information to be stored in a widget
        than immediately visible, letting the user scroll to view additional
        content.

        Canvas: a storage widget for a collection of 2D graphical objects - can
        include drawings, other widgets, images, and more. When placing images
        in a canvas, they should be stored outside of the function they're
        created in, so they don't disappear instantly when the original
        variables they referred to are deleted.

    If a widget is assigned to a variable on creation, its unique ID is stored
    in that variable. This can be used later to modify the properties of the
    widget. Additionally, widgets can be tagged, allowing you to modify the
    property of multiple widgets at the same time.
'''


# Bindings and Callback Functions
'''
    Bindings in Tkinter allow you to specify the results of certain user
    actions, such as when they click on a particular widget, or move their
    mouse. Actions can be bound to particular widgets, with a 'callback
    function' specified to trigger when that action occurs. This allows you to
    specify a function such as one to draw a line, and allows the user to click
    and drag their mouse on a canvas, with the line drawn tracking their mouse
    motions.
'''


# Geometry Management
'''
    With an established set of elements, the remaining aspect of the display is
    to position each widget in a desired position. This is known as geometry
    management. Tkinter has inbuilt geometry management functionality using
    either 'pack', 'grid', or 'place'. Pack allows you to specify the direction
    in which widgets should be placed within a container widget (e.g. a Frame
    or Canvas), with subsequent widgets positioned relative to the earlier
    positioned widgets. Grid allows for position specification in a grid (i.e.
    simply and nicely lines things up), and remembers previous settings when
    hiding widgets, so they can be easily restored. Place allows you to specify
    the pixel locations of widgets, but that also makes it incredibly
    inflexible, and it's rarely used as a result.

    Pack and grid should never be used within the same window - they don't play
    nice with each other. Pack was established before grid, so many online
    examples use pack, and you may find old code which uses it. Pack is
    generally considered easier to use for laying out widgets in a single
    column or row, but otherwise grid is suggested (tkdocs suggests using grid
    for most, if not all geometry management).

    Widgets will not appear in the GUI until they have been put in place with a
    geometry manager.
'''


# ----- NOTE: Widget Creation and Geometry Management ----- #
'''
    When creating widgets and putting them into place, it's generally best
    practice to keep the creation separate from the layout. This helps to make
    code much more readable, and easier to debug. If a widget is put in place
    in the same line it's created, it is anonymous - assigning the result to a
    variable just leaves None in that variable. Sometimes anonymous behaviour
    is desired, particularly if you have no desire to access certain widgets
    once they've been created, but only do so if you know what you're doing,
    and generally for small numbers so debugging isn't made too difficult.
'''



# GUI Example
'''
    An in-depth GUI example can be found in the GUI_Example folder with these
    lesson notes. The use of the Model-View-Controller framework means it is
    split into separate classes, each in their own file. The GUI is runnable
    from the Controller.py file, so feel free to run it before looking through
    the different files to see how each section of code is implemented. It may
    be helpful to make a copy of the entire GUI, and play around with modifying
    geometries and widgets.

    The GUI example requires the libraries: numpy (numerical python), opencv
    (open-source computer vision), and Pillow (python image library for python
    3). If you have pip (python package installer), open a terminal/command
    prompt and run the command:
        python3 -m pip install numpy opencv-python Pillow
'''




#-------------------------------- EVAL AND EXEC -------------------------------#
'''
    The evaluate (eval) and execute (exec) functions are two powerful python
    functions which allow dynamic specification and execution of code. 'eval'
    takes a string, and determines (evaluates) and returns the result (e.g.
    eval('1+3')), whereas 'exec' takes a string and executes it, returning
    nothing.

    Both eval and exec are known as potential security risks when run directly
    off user input - and this should never be done. Instead, they should be
    used for testing purposes, or use user input that has been verified as
    valid, using regex (regular expressions) or comparison to a list of valid
    inputs. Be aware that in most situations where eval or exec could be used,
    there is a better, safer, and more efficient way to get the same
    performance not using them. Additionally, dynamically generated and/or
    executed code is problematic in that it can't be debugged, since you don't
    know what code was run (unless it's logged before running it). In saying
    that, there are cases where eval and exec are highly beneficial, or even
    required.

    As a security note, ANY time a user provides input, it should be treated as
    untrustworthy unless fully parsed into a set of proven safe
    values/characters.
'''



# Eval and __repr__
'''
    In lesson 6, with the introduction of classes, it was specified that the
    __repr__ method, if evaluated, should return a copy of the current class
    instance. While it is possible to copy and paste the output from typing a
    variable name into the console, this is not particularly efficient,
    particularly for large numbers of variables. Here the __repr__ function is
    tested for an instance T1. The following behaviour should be the case for
    any and every class you define, assuming it has a valid __eq__ method
    defined for checking instance equality.
'''

T1 = [1,2,3]
T2 = eval(repr(T1))
T2 == T1 # True


# Exec with Valid Options and Type Checking (Using Eval)
'''
    The following example defines some basic functions, then gets a user to
    input a semicolon-separated list specifying which function they'd like to
    run, and the variable values they'd like to pass to it. Exec is used to
    execute the function once the user input has been validated, and eval is
    used in the validation process.

    This code is still vulnerable to having time wasted from a user entering an
    integer large enough to cause a memory error (e.g. 10**50**50), but the
    internal variables and code are safe from external modification. Also,
    adding more valid functions is easy, and could even be done automatically,
    by detecting all defined functions in the document or class, or some
    specifiable subset of these functions.

    Note that in a GUI program, the function validity check could be eliminated
    by simply providing the full set of valid options in a drop-down menu, but
    allowing a user to specify inputs will usually still require some form of
    type (and potentially value) checking.
'''

# a set of predefined functions, and the argument types they take
valid_funcs = {'test': ['int', 'int', 'str'],
            'func2': ['float', 'int'],
            'derp': ['int', ['int']],
            'boop': ['dict', 'list']}

import re # import regular expressions (regex)

def user_run_func(valid_funcs):
    ''' Takes a dictionary of predefined functions with input argument types.
    Internally requests a user-specified string and runs a requested function
        if the function and inputs are deemed to be valid according to
        valid_funcs.

    valid_funcs should be of form:
        {'func1': ['type1','type2',...],
        ...}
    If a function uses *args with arguments of the same type, it can have
        'funcN': ['type1','type2',['type3']]
    where all arguments in *args have to be of type3.
    Type checking is only performed at the top layer.

    If user function request is invalid, prints an error message.

    user_run_func(dict{str:list[str/list[str]]}) -> None

    '''
    input_func = input(
        'Specify a semicolon-separated list of func;var1;var2;...\n')
    inputs = input_func.split(';')
    func = inputs[0]; func_inputs = inputs[1:]; valid_inputs = ''

    # run the desired function
    if func in valid_funcs.keys():
        persistent_type = None
        executable = True
        for ind, var in enumerate(func_inputs):
            # check if type is valid, and add to valid_inputs, else error
            try:
                if persistent_type:
                    persistent_type(var) # check if type is valid
                    continue # already checked, don't try to check again
                    
                input_type = valid_funcs[func][ind]
                if type(input_type) is str and input_type in \
                ['int','str','float','bool']:
                    # check type validity - don't store result
                    eval('{}(var)'.format(input_type))
                elif type(input_type) is list:
                    # remaining inputs are all of specified type,
                    # only convert to type (from string) once, and store result
                    persistent_type = eval(input_type[0])
                    persistent_type(var) # check if type is valid
                # use a regular expression to check for modifier accessing,
                # without disabling floats in container objects
                elif re.search(r"\.[a-zA-Z_]", var) is None:
                    # remove spaces to get rid of obscure hacks
                    var = var.replace(' ','')
                    test_obj = eval(var)
                    assert type(test_obj) == eval(input_type)
                else:
                    raise Exception('Invalid variable input {0}'.format(var))
            except Exception as e:
                for index, var_type in enumerate(valid_funcs[func]):
                    if type(var_type) is list:
                        valid_funcs[func][index] = str(var_type)
                print(('Invalid input "{0}". {1} function should be used '+
                    'as:\n\t{1};{2}').format(
                        var, func, ';'.join(valid_funcs[func])))
                executable = False
                break # having no break here would identify all input var issues
        if executable:
            # function name and inputs have been fully checked for validity
            # -> call desired function with specified inputs
            exec('{0}({1})'.format(func, ','.join(func_inputs)))
    else:
        print("Invalid function '{0}'. Functions must be one of {1}".format(
            func, list(valid_funcs.keys())))

def test(a,b,c):
    ''' test(int, int, str) -> None '''
    print(c + str(a+b/2))

def func2(a,b):
    ''' func2(float, int) -> None '''
    print(str(a+b))

def derp(a, *args):
    ''' derp(int, [int]) -> None '''
    total = sum([*args],a)
    print('Start value =', a)
    print('Result =', total)

def boop(a,b):
    ''' boop(dict, list) -> None '''
    print(a); print(b);
    print('boop boop')
