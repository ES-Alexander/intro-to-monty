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
from tkinter import *

class L9Tests(TestRun):
    # class existence
    def test_class_exists(self):
        ''' Testing for existence of class MyGUI.

        L9Tests.run_test('test_class_exists') -> None
        
        '''
        try:
            test = MyGUI
        except NameError:
            assert False, "Class 'MyGUI' does not exist"

    # required setup methods
    def test_setup_io(self):
        ''' Testing for existence of _setup_io in MyGUI.

        L9Tests.run_test('test_setup_io') -> None
        
        '''
        assert '_setup_io' in dir(MyGUI), 'User I/O not set up with ' +\
               '_setup_io method.'

    def test_setup_canvas(self):
        ''' Testing for existence of _setup_canvas in MyGUI.

        L9Tests.run_test('test_setup_canvas') -> None

        '''
        assert '_setup_canvas' in dir(MyGUI), 'Canvas not set up with ' +\
               '_setup_canvas method.'

    def test_setup_menubar(self):
        ''' Testing for existence of _setup_menubar in MyGUI.

        L9Tests.run_test('test_setup_menubar') -> None

        '''
        assert '_setup_menubar' in dir(MyGUI), 'Menubar not set up with ' +\
               '_setup_menubar method.'


#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    import random
    class MyGUI(object):
        def __init__(self, master):
            self._master = master
            self._setup_io()
            self._setup_canvas()
            self._setup_menubar()
            
        def _setup_io(self):
            # creation
            io_frame = tk.Frame(self._master)
            self._label = tk.Label(io_frame, text='')
            self._entry = tk.StringVar()
            self._entry.set('User Input')
            entry = tk.Entry(io_frame, textvariable=self._entry)
            button = tk.Button(io_frame, text='My Button',
                               command=lambda: \
                               self._label.config('text', self._entry.get()))

            # geometry management
            io_frame.grid(row=0, column=1)
            self._label.grid()
            entry.grid()
            button.grid()

        def _setup_canvas(self):
            # creation
            canvas_frame = tk.Frame(self._master)
            self._canvas = tk.Canvas(canvas_frame)
            button = tk.Button(canvas_frame, text='Canvas Button',
                               command=self._create_circ)

            # geometry management
            canvas_frame.grid(row=0,column=0)
            self._canvas.grid()
            button.grid()

        def _create_circ(self):
            pass

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
