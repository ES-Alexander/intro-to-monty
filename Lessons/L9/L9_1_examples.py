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

    canvas, draw rectangle, select scaling point, scale entry, button to apply
        scale (scale based off original drawn shape), model stores shape info
        and calculates new info when scaling applied, label for scale entry,
        filemenu for clear canvas to redraw rectangle and clear scale entry.
        Extension -> Add rotation entry/label/functionality about scale point.
        

    Output user input:
        Set this up with the method 'self._setup_io()'
        Create a Frame widget for storing this section. Use the grid geometry
            manager to place it on the left hand side of the master window. The
            following widgets should be put into a grid as you desire, inside
            this outer frame.
        Create a Label widget for display purposes.
        Create an Entry widget which allows a user to type an arbitrary input.
        Create a Button widget, which, when pressed, sets the Label's text to
            the current value in the Entry widget. The button text can be
            anything you want.
            
    Shapes on a Canvas:
        Set this up with the method 'self._setup_canvas()'
        Create a Frame widget for storing this section. Use grid to place the
            frame on the right hand side of the master window. The following
            widgets should be put into place as you desire, inside this outer
            frame.
        Create a Canvas widget which allows you to create a red rectangle by
            clicking and dragging the mouse to signify the start (on mouse
            press) and end (on mouse release) corners of the rectangle. Further
            clicks are reserved for the circle (see Button below), until the
            Canvas is reset/cleared (see Menubar).
        Create a Button widget which, when pressed, creates a blue circle of
            random size, at a random position inside the Canvas, such that the
            circle would fit within the red rectangle but does not touch the
            rectangle. Clicking on the canvas should make the circle move
            to a random position within the rectangle. Clicking the button
            after its first click should move the circle to a new position
            outside the rectangle. You will need to import the random module
            for this section.
        
    Menubar:
        Set this up with the method 'self._setup_menubar()'
        Create a menubar with a drop-down File menu. This menu should contain
            at least a button with label 'Clear All', which should set the Label
            text to '', the Entry text to 'User Input', and reset the Canvas to
            contain no shapes, with the user able to create a new rectangle.

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

    root = tk.Tk()          # initialise main window
    GUI = MyGUI(root)       # set up GUI
    root.mainloop()         # run the GUI (turn over to event handler)
