#!/usr/bin/env python3
################################################################################
# This file contains a function used to test the LN_1_examples file.             #
################################################################################

# imports all the variables/functions/classes from L9_1_examples
from L9_1_examples import *
import sys
sys.path.append('..')
from TestRun import TestRun

import tkinter as tk

class L9Tests(TestRun):
    # class existence
    def test_classes_exist(self):
        ''' Testing for existence of relevant classes. '''
        for class_name in ['Model','View','Controller']:
            try:
                test = eval('{}()'.format(class_name))
            except NameError:
                assert False, "Class {} does not exist".format(class_name)

    # required setup methods
    def test_setup_controls(self):
        ''' Testing for existence of _setup_io in MyGUI. '''
        assert '_setup_controls' in dir(View), 'Controls not set up with ' +\
               '_setup_controls method.'

    def test_setup_canvas(self):
        ''' Testing for existence of _setup_canvas in MyGUI. '''
        assert '_setup_canvas' in dir(View), 'Canvas not set up with ' +\
               '_setup_canvas method.'

    def test_setup_menubar(self):
        ''' Testing for existence of _setup_menubar in MyGUI. '''
        assert '_setup_menubar' in dir(View), 'Menubar not set up with ' +\
               '_setup_menubar method.'


#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    import random
    class View(object):
        # class variables
        SELECT_SCALE_POINT = 'ssp'
        
        def __init__(self, master):
            self._master = master
            self._setup_controls()
            self._setup_canvas()
            self._setup_menubar()
            
        def _setup_controls(self):
            # creation
            control_frame = tk.Frame(self._master)
            self._label = tk.Label(control_frame, text='Scale Controls')
            self._entry = tk.StringVar()
            self._entry.set('Scale Value')
            entry = tk.Entry(control_frame, textvariable=self._entry)
            button = tk.Button(control_frame, text='Scale',
                               command=self._scale_binding)

            # geometry management
            control_frame.grid(row=0, column=1)
            self._label.grid()
            entry.grid()
            button.grid()

        def _setup_canvas(self):
            # creation
            canvas_frame = tk.Frame(self._master)
            self._canvas = tk.Canvas(canvas_frame)
            button = tk.Button(canvas_frame, text='Select Scale Point',
                               command=lambda: self._change_mode(
                                   View.SELECT_SCALE_POINT))

            # geometry management
            canvas_frame.grid(row=0,column=0)
            self._canvas.grid()
            button.grid()

        def _scale_point(self):
            ''' '''
                               

        def _setup_menubar(self):
            # creation
            menubar = tk.Menu(self._master)
            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Clear All", command=self._clear_all)

            # add to the menubar
            menubar.add_cascade(label="File", menu=filemenu)

        def _clear_all(self):
            pass

    L9 = L9Tests()
    L9.run_tests(verbose=True)

    root = tk.Tk()
    GUI = MyGUI(root)
    root.mainloop()
