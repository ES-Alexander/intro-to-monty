#!/usr/bin/env python3
################################################################################
# As practice, please fill out the following examples below the appropriate    #
# comment, and click run when complete, using either the menu-bar at the top,  #
# or the F5 key on your keyboard.                                              #
################################################################################

import tkinter as tk
# Getting Started
'''
    Implement the GUI below. The desired functionality is:

    Shape on a Canvas:
        Set this up with the method 'self._setup_canvas()'.
        Create a Frame widget for storing this section. Use the grid geometry
            manager to place it on the right hand side of the master window. The
            following widgets should be put into a grid as you desire, inside
            this outer frame.
        Create a Canvas widget. Clicking on the blank canvas should add the
            first point of a polygon. Subsequent clicks should add the remainder
            of the polygon, until the user double-clicks, at which point the
            last clicked point should be joined to the first point. Double-
            clicking before there are three points should print an error (see
            Controls), and add no point. Once the polygon is completed, the
            canvas should change to scale-point selecting mode for the next
            click - which defines the point about which the polygon should be
            scaled.
        Create a Button widget with text "Select Scale Point". Clicking this
            should only work when a polygon is in the canvas, and should allow
            the user to change the scaling point.

    Controls:
        Set this up with the method 'self._setup_controls()'.
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
        Set this up with the method 'self._setup_menubar()'.
        Create a menubar with a drop-down File menu. This menu should contain
            at least a button with label 'Clear All', which should set the Entry
            text to '', and reset the Canvas to be blank, and ready to draw a
            new polygon.

    The Model class should store the relevant information for the polygon, and
        should perform the scaling calculations.

    The Controller class should initialise the GUI internally.

    The following resources may be useful, along with their main websites:
        https://tkdocs.com/tutorial/canvas.html
        http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        http://www.scoberlin.de/content/media/http/informatik/tkinter/
            x9170-window-related-information.htm
        
    The GUI Example provided with this course also provides examples of using
        all the specified widgets (in the View class), and is suggested as a
        reference resource for this and future GUI creation.
'''

class Model(object):

class View(object):

class Controller(object):
    




'''
    When you're done, click Run or F5 to check that you've followed the
    instructions. Example solutions can be found at the bottom of the example
    checker file.

    The code below isn't for editing, it's used to run the test file when this
    program is run.
'''

if __name__ == '__main__':
    from L9_example_checker import L9Tests
    L9Tests().run_tests()   # run tests before running GUI
    C1 = Controller()       # run the GUI
