#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following exercises below the appropriate   #
# comment, and click run when complete, using either the menu-bar at the top,  #
# or the F5 key on your keyboard.                                              #
################################################################################

import tkinter as tk
# Getting Started
'''
    Implement the GUI below. The desired functionality is:

    Shape on a Canvas:
        Set this up with the method 'View._setup_canvas()'.
        Create a Frame widget for storing this section. Use the grid geometry
            manager to place it on the right hand side of the master window. The
            following widgets should be put into a grid as you desire, inside
            this outer frame.
        Create a Canvas widget. Clicking on the blank canvas should add the
            first point of a polygon (a red circle). Subsequent clicks should
            add the remaining points of the polygon (also red circles), until
            the user double-clicks, at which point a full polygon should be
            drawn on the canvas, with the last clicked point joined to the first
            point. The original circle points should maintain their position as
            the polygon is scaled - this shows the original defining points as
            the polygon moves and changes. Double-clicking before there are
            three points should print an error (see Controls), and add no point.
            Once the polygon is completed, the canvas should change to
            reference-point selecting mode for the next click - which defines
            the point about which the polygon should be scaled. This point
            should be displayed as a blue circle. This mode is maintained until
            the canvas is cleared (see Menubar), and the blue cross should
            continually move to the most recently clicked position.

    Controls:
        Set this up with the method 'View._setup_controls()'.
        Create a Frame widget for storing this section. Use the grid geometry
            manager to place it on the left hand side of the master window. The
            following widgets should be put into a grid as you desire, inside
            this outer frame.
        Create a Label widget with the text "Scale Controls".
        Create an Entry widget and a Button widget below the Scale Controls
            Label. The Entry should have no contents, and the Button should have
            the text "Scale", and be used to apply the scale value in the Entry
            widget to the polygon in the canvas, about the selected scaling
            point. If no polygon exists, or no scaling point is selected, or the
            specified scale value would cause the shape to leave the canvas, an
            appropriate error message should be printed (see below). The scale
            value in the Entry is with respect to the current shape. Clicking
            the Scale Button multiple times should result in multiple scales.
        Create a Label widget for displaying errors and instructions to the
            user. This should be below the scale controls, and should display
            usage instructions on startup.

    Menubar:
        Set this up with the method 'View._setup_menubar()'.
        Create a menubar with a drop-down File menu. This menu should contain
            at least a button with label 'Clear All', which should set the Entry
            text to '', and reset the Canvas to be blank, and ready to draw a
            new polygon.

    The View class should initialise the external bindings to do nothing, using
        the method 'View._init_bindings()'. The main window should have the
        title 'Parametric Polygon'.

    The Model class should store the relevant information for the polygon, and
        should perform the scaling calculations. Note that Canvas widgets
        already have a 'scale' method inbuilt. You can use this to guide your
        calculations, but do not use the inbuilt method - implement your own in
        the Model.

    The Controller class should set up the bindings between the model and the
        view, using the method 'Controller._add_bindings'.

    The following resources may be useful, along with their main websites:
        https://tkdocs.com/tutorial/canvas.html
        http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        http://www.scoberlin.de/content/media/http/informatik/tkinter/
            x9170-window-related-information.htm
        
    The GUI Example provided with this course also provides examples of using
        all the specified widgets (in the View class), and is suggested as a
        reference resource for this and future GUI creation.

    As an extension, consider adding rotation controls, to enable rotating the
        polygon about the reference point as well as scaling.
'''

class Model(object):
    ''' '''
    def __init__(self):
        ''' '''
        pass

class View(object):
    ''' '''
    def __init__(self, master):
        ''' '''
        pass

class Controller(object):
    ''' '''
    def __init__(self, master):
        ''' '''
        pass
    




'''
    When you're done, click Run or F5 to check that you've followed the
    instructions. Example solutions can be found at the bottom of the exercise
    checker file.

    The code below isn't for editing, it's used to run the test file when this
    program is run. (Also runs your GUI afterwards)
'''

if __name__ == '__main__':
    # These tests just check that widgets exist with correct values and
    #   placement. Try to follow the specified functionality as best you can,
    #   and feel free to improve the application by adding additional features.
    from L9_2_exercise_checker import L9Tests
    L9Tests = L9Tests()
    # run the tests (with feedback) before running the GUI
    L9Tests.run_tests(verbose=True)

    # run the GUI
    root = tk.Tk()
    C1 = Controller(root)
    root.mainloop()
